"""
Mini-game "greatest common divisor".

Player should find gcd for two provided numbers.
"""

from random import randint

OBJECTIVE = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1: int, number2: int) -> int:
    """Find greatest common divisor, using Euclidean algorithm (oldest one).

    Args:
        number1 (int): first number, should be greater or equal than 1
        number2 (int): second number, should be greater or equal than 1

    Returns:
        int: greatest common divisor
    """
    (bigger, smaller) = (max(number1, number2), min(number1, number2))
    if smaller == bigger:
        return bigger
    return get_gcd(smaller, bigger - smaller)


def generate_round():
    """Generate question and correct answer for game round.

    Returns:
        tuple of question and answer
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer = str(get_gcd(number1, number2))
    question = '{0} {1}'.format(number1, number2)
    return (question, answer)
