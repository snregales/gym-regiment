# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from src.config.database import PKModel as Model
from src.config.database import column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship
from src.config.database import unique_column as unique
from src.config.extensions import bcrypt

from .utils import generate_reset_key, has_expired


class Role(Model):
    """A role for a user."""

    __tablename__ = "roles"

    name = unique(db.String(80))

    user_id = reference_col(tablename="users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name: str, **kwargs) -> None:
        """
        Create instance.

        :param name :type str: name of the user
        """
        db.Model.__init__(self, name=name, **kwargs)

    def __str__(self) -> str:
        """
        String representation.

        :return :type str
        """

        return self.name

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<{self.__class__.__name__}({self.__str__()!r})>"


class Voucher(Model):
    """
    Voucher Class.

    Contains all off users secret credentials for authentication purposes.
    """

    __tablename__ = "vouchers"

    password = nullable(db.LargeBinary(128))
    password_last_set = nullable(db.DateTime)
    reset_key = nullable(db.String(16), unique=True)
    key_generated_date = nullable(db.DateTime)

    def __init__(self, password: str = None, **kwargs):
        """Voucher constructor."""
        db.Model.__init__(self, **kwargs)
        if password:
            self.set_password(password)

    @property
    def has_reset_key_expired(self) -> bool:
        """Has reset key expired."""
        return has_expired(self.key_generated_date)

    def set_reset_key(self) -> None:
        """Reset key setter."""
        self.reset_key = generate_reset_key()
        self.key_generated_date = dt.datetime.now()

    def set_password(self, password: str) -> None:
        """
        Set hashed password, and password creation date.

        :param password :type str: none hashed version of user's password
        """
        self.password = bcrypt.generate_password_hash(password)
        self.password_last_set = dt.datetime.now()

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
        return self.id

    def __repr__(self) -> str:
        """
        Object instance representation.

        :return :type str
        """

        return f"<{self.__class__.__name__}({self.__str__()!r})>"


class User(UserMixin, Model):
    """User Model class."""

    __tablename__ = "users"
    email = unique(db.String(80))

    voucher_id = reference_col(tablename="vouchers", nullable=True)
    voucher = relationship("Voucher", backref="user", uselist=False)

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
            self.voucher = Voucher(password)

    @property
    def _password(self) -> str:
        if self.voucher:
            return self.voucher.password
        return None

    @property
    def has_password(self) -> bool:
        """Does User instance have a password."""
        password = self._password
        return not (password is None or password == "")

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
