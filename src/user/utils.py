from datetime import datetime
from random import SystemRandom
from string import ascii_uppercase, digits

from . import KEY_LIFE


def generate_reset_key():
    return "".join(
        map(lambda x: SystemRandom().choice(ascii_uppercase + digits), range(16))
    )


def is_key_valid(generated_date: datetime):
    return 0 <= (datetime.now() - generated_date).days < KEY_LIFE