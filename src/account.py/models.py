"""Account's models module."""

from src.config.database import Model, SurrogatePK, column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship


class Account(SurrogatePK, Model):
    """A user account."""

    __tablename__ = "accounts"

    user_id = reference_col(tablename="users", nullable=True)
    user = relationship("User", backref="account")

    first_name = column(db.String(30))
    last_name = column(db.String(30))
    phone_number = nullable(db.Integer(14))

    def __init__(self, name: str, **kwargs) -> None:
        """
        Create instance.

        :param name :type str: name of the user
        """
        db.Model.__init__(self, name=name, **kwargs)

    @property
    def fullname(self) -> str:
        """Users fullname."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """
        String representation.

        :return :type str
        """

        return self.first_name

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<{self.__class__.__name__}({self.__str__()!r})>"
