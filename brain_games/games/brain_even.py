"""Mini-game "is even". Player should answer yes if number is even."""

from random import randint

OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Predicate that returns if number is even."""
    return number % 2 == 0


def generate_round():
    """Generate round for game engine."""
    number = randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return (question, answer)
