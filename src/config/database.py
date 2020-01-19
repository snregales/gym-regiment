# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""

from functools import partial
from typing import Any

from src.config.extensions import db

# Alias common SQLAlchemy names
column = db.Column
relationship = db.relationship
null_column = partial(db.Column, nullable=True)
unique_column = partial(db.Column, unique=True)
primary_column = partial(db.Column, primary_key=True)


class CRUDMixin:
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs) -> "CRUDMixin":
        """
        Create a new record and save it the database.

        :return :type CRUDMixin
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit: bool = True, **kwargs) -> "CRUDMixin":
        """
        Update specific fields of a record.

        :param commit :type bool: commit operation to session :default True
        :return :type CRUDMixin
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True) -> "CRUDMixin":
        """
        Save the record.

        :param commit :type bool: commit operation to session :default True
        :return :type CRUDMixin
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True) -> bool:
        """
        Remove the record from the database.

        :param commit :type bool: commit operation to session :default True
        :return :type bool: is operation run successfully
        """
        db.session.delete(self)
        return commit and db.session.commit()


class Model(db.Model, CRUDMixin):
    """Abstract Base model class."""

    __abstract__ = True


# From Mike Bayer's "Building the app" talk
# https://speakerdeck.com/zzzeek/building-the-app
class SurrogatePK:
    """A mixin that adds a surrogate integer 'primary key' column named ``id`` to any declarative-mapped class."""

    __table_args__ = {"extend_existing": True}

    id = primary_column(db.Integer)

    @classmethod
    def get_by_id(cls, record_id: Any):
        """Get record by ID."""
        if any(
            [
                isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                isinstance(record_id, (int, float)),
            ]
        ):
            return cls.query.get(int(record_id))
        return None


def reference_col(
    tablename, nullable=False, pk_name="id", foreign_key_kwargs=None, column_kwargs=None
):
    """Column that adds primary key foreign key reference.

    Usage: ::

        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    foreign_key_kwargs = foreign_key_kwargs or {}
    column_kwargs = column_kwargs or {}

    return column(
        db.ForeignKey("{0}.{1}".format(tablename, pk_name), **foreign_key_kwargs),
        nullable=nullable,
        **column_kwargs
    )
