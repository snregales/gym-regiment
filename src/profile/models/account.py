"""Account model module."""

from src.config.database import PKModel as Model
from src.config.database import column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship


class Account(Model):
    """A user account."""

    __tablename__ = "accounts"

    user_id = reference_col(tablename="users")
    user = relationship("User", backref="account")

    biometric_id = reference_col(tablename="biometrics", nullable=True)
    biometric = relationship("BioMetric", backref="account", uselist=False)

    first_name = column(db.String(30))
    last_name = column(db.String(30))
    dob = column(db.Date)
    phone_number = nullable(db.Integer())

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
