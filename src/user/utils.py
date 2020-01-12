from random import SystemRandom
from string import ascii_uppercase, digits


def generate_reset_key():
    return "".join(
        map(lambda x: SystemRandom().choice(ascii_uppercase + digits), range(16))
    )
