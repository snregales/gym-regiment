"""Account Module."""

from enum import Enum

M_TO_FT: float = 3.2808398950131
KG_TO_LB: float = 2.2046226218488


class Sex(Enum):
    """Binary genetic sex choices."""

    male = 1
    female = 2


Sex.male.label = u"Male"
Sex.female.label = u"Female"
