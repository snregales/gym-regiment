# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from src.config.extensions import BCRYPT
from src.config.database import (
    COLUMN,
    DB,
    RELATIONSHIP,
    Model,
    SurrogatePK,
    reference_col,
)


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = "roles"
    name = COLUMN(DB.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = RELATIONSHIP("User", backref="roles")

    def __init__(self, name: str, **kwargs):
        """
        Create instance.

        :param name :type str: name of the user
        """
        DB.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Role({name})>".format(name=self.name)


class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = "users"
    username = COLUMN(DB.String(80), unique=True, nullable=False)
    email = COLUMN(DB.String(80), unique=True, nullable=False)
    #: The hashed password
    password = COLUMN(DB.LargeBinary(128), nullable=True)
    created_at = COLUMN(DB.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = COLUMN(DB.String(30), nullable=True)
    last_name = COLUMN(DB.String(30), nullable=True)
    active = COLUMN(DB.Boolean(), default=False)
    is_admin = COLUMN(DB.Boolean(), default=False)

    def __init__(self, username: str, email: str, password: str = None, **kwargs):
        """
        Create instance.

        :param username :type str: username of the user instance
        :param email :type str:  email of the user instance
        :param password :type str: none hashed version of user instance's password :default None
        """
        DB.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password: str):
        """
        Set hashed password.

        :param password :type str: none hashed version of user's password
        """
        self.password = BCRYPT.generate_password_hash(password)

    def check_password(self, value) -> bool:
        """
        Compare value against user's password.

        :param value :type str: value string to be compaired
        :return :type bool: True if they match
        """
        return BCRYPT.check_password_hash(self.password, value)

    @property
    def full_name(self) -> str:
        """
        Users full name.

        :return :type str
        """
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """
        Represent instance as a unique string.

        :return :type str
        """
        return f"<User({self.username!r})>"
