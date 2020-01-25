"""Account's models module."""

from datetime import date

from src.config.database import Model, SurrogatePK, column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship

from . import KG_TO_LB, M_TO_FT


class BioMetric(SurrogatePK, Model):
    """
    Accounts metrics.

    This holds all the biometrics information of User
    """

    __tablename__ = "biometrics"

    height = column(db.Float())  # height in Meters
    weight = column(db.Float())  # weight in KiloGrams

    @property
    def bmi(self) -> float:
        """Users body mass index."""
        return self.weight / pow(self.height, 2)

    @property
    def age(self) -> int:
        """Users age."""
        today, dob = date.today(), self.account.dob
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    @property
    def height_in_feet(self) -> float:
        """Impirical form of users height (Feet)."""
        return self.height * M_TO_FT

    @property
    def weight_in_pounds(self) -> float:
        """Impirical form of users weight (pounds)."""
        return self.weight * KG_TO_LB


class Account(SurrogatePK, Model):
    """A user account."""

    __tablename__ = "accounts"

    user_id = reference_col(tablename="users", nullable=True)
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
