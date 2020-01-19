"""User Utils Module."""

from datetime import datetime
from random import SystemRandom
from string import ascii_uppercase, digits

from . import KEY_LIFE


def generate_reset_key():
    """Generate random 16 alpha numeric character uppercase string."""
    return "".join(
        map(lambda x: SystemRandom().choice(ascii_uppercase + digits), range(16))
    )


def has_expired(generated_date: datetime):
    """Has current the time passed the experation date."""
    return 0 <= (datetime.now() - generated_date).days < KEY_LIFE
