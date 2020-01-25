"""Test Account Utils."""
from datetime import date, timedelta

import pytest

from src.account.utils import (
    body_mass_index,
    calculate_age,
    kilogram_to_pound,
    meter_to_feet,
)


@pytest.mark.parametrize("meter, feet", [(1.85, 6.06955), (1.88976, 6.2)])
def test_meter_to_feet(meter: float, feet: float) -> None:
    """Test meter to feet conversion."""

    assert round(meter_to_feet(meter), 2) == round(feet, 2)


@pytest.mark.parametrize("kg, pound", [(85.0, 187.39292), (88.45051, 195.0)])
def test_kilogram_to_pound(kg: float, pound: float) -> None:
    """Test kilogram to pound conversion."""

    assert round(kilogram_to_pound(kg), 2) == round(pound, 2)


@pytest.mark.parametrize(
    "dob, age",
    [
        (date.today() - timedelta(days=30000), 82),
        (date.today() - timedelta(days=365), 1),
        (date.today() - timedelta(days=364), 0),
    ],
)
def test_calculate_age(dob: date, age: int) -> None:
    """Test calculate_age."""

    assert calculate_age(dob) == age


@pytest.mark.parametrize(
    "weight, height, bmi", [(85.0, 1.85, 24.8), (90.5, 1.83, 27.0)]
)
def test_body_mass_index(weight: float, height: float, bmi: float) -> None:
    """Test Body Mass Index calculator."""

    assert round(body_mass_index(height=height, weight=weight), 1) == bmi
