"""Mini-game "is even". Player should answer yes if number is even."""

from random import randint

OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """Predicate that checks if provided number is even.

    Args:
        number: number to check if it's even

    Returns:
        A boolean value indicating that number is even
    """
    return number % 2 == 0


def generate_round():
    """Generate question and correct answer for game round.

    Returns:
        tuple of question and answer
    """
    number = randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return (question, answer)
