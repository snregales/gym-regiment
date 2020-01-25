"""Account's utils module."""

from datetime import date

from . import KG_TO_LB, M_TO_FT


def meter_to_feet(value: float) -> float:
    """Meter to Feet converter."""

    return value * M_TO_FT


def kilogram_to_pound(value: float) -> float:
    """Kilogram to Pound converter."""

    return value * KG_TO_LB


def body_mass_index(height: float, weight: float) -> float:
    """Body Mass Index calculator."""

    return weight / pow(height, 2)


def calculate_age(dob: date) -> int:
    """Calculate age from Date of Birth (dob)."""

    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
