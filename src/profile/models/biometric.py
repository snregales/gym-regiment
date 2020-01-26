"""BioMetric model module."""

from sqlalchemy_utils import ChoiceType

from src.config.database import PKModel as Model
from src.config.database import column, db
from src.profile import Sex
from src.profile.utils import (
    body_mass_index,
    calculate_age,
    kilogram_to_pound,
    meter_to_feet,
)


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
        """Is there an account attached to this metric."""
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
