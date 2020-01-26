"""Account's models module."""

from sqlalchemy_utils import ChoiceType

from src.config.database import PKModel as Model, column, db
from src.config.database import null_column as nullable
from src.config.database import reference_col, relationship

from . import Sex
from .utils import body_mass_index, calculate_age, kilogram_to_pound, meter_to_feet


class BioMetric(Model):
    """
    Accounts metrics.

    This holds all the biometrics information of User
    """

    __tablename__ = "biometrics"

    height = column(db.Float())  # height in Meters
    weight = column(db.Float())  # weight in KiloGrams
    sex = column(ChoiceType(Sex, impl=db.Integer()))

    @property
    def has_account(self) -> bool:
        return bool(self.account)

    @property
    def bmi(self) -> float:
        """Users body mass index."""
        return body_mass_index(weight=self.weight, height=self.height)

    @property
    def age(self) -> int:
        """Users age."""
        return calculate_age(self.account.dob) if self.has_account else -1

    @property
    def height_in_feet(self) -> float:
        """Impirical form of users height (Feet)."""
        return meter_to_feet(self.height)

    @property
    def weight_in_pounds(self) -> float:
        """Impirical form of users weight (pounds)."""
        return kilogram_to_pound(self.weight)


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
