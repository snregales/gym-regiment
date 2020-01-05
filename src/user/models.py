# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from src.config.database import Model, SurrogatePK, column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship
from src.config.database import unique_column as unique
from src.config.extensions import bcrypt


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = "roles"
    name = unique(db.String(80))
    user_id = reference_col(tablename="users", pk_name="email", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name: str, **kwargs) -> None:
        """
        Create instance.

        :param name :type str: name of the user
        """
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<{self.__class__.__name__}({self.name})>"


class User(UserMixin, SurrogatePK, Model):
    """User Model class."""

    __tablename__ = "users"
    email = unique(db.String(80))
    #: The hashed password
    password = nullable(db.LargeBinary(128))
    created_at = column(db.DateTime, default=dt.datetime.utcnow)
    is_active = column(db.Boolean(), default=False)
    is_admin = column(db.Boolean(), default=False)

    def __init__(self, email: str, password: str = None, **kwargs):
        """
        Create instance.

        :param email :type str:  email of the user instance
        :param password :type str: none hashed version of user instance's password :default None
        """
        db.Model.__init__(self, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password: str):
        """
        Set hashed password.

        :param password :type str: none hashed version of user's password
        """
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value) -> bool:
        """
        Compare value against user's password.

        :param value :type str: value string to be compaired
        :return :type bool: True if they match
        """
        return bcrypt.check_password_hash(self.password, value)

    def __str__(self) -> str:
        """
        String representation.

        :return :type str
        """
        return self.email

    def __repr__(self) -> str:
        """
        Object instance representation.

        :return :type str
        """

        return f"<{self.__class__.__name__}({self.__str__()!r})>"
