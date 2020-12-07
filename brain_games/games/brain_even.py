"""Mini-game "is even". Player should answer yes if number is even."""

from random import randint

OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """Predicate that checks if provided number is even.

    :param number: number to check if it's even
    """
    return number % 2 == 0


def generate_round():
    """Generate question and correct answer for game round."""
    number = randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return (question, answer)
