"""Mini-game "is prime". Player should answer yes if number is prime."""

from random import randint

OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Predicate that checks if provided number is prime.

    Args:
        number (int): number to check if it's prime

    Returns:
        A boolean value indicating that number is prime
    """
    if number <= 1:
        return False

    index = 2
    while index < number:
        if number % index == 0:
            return False
        index += 1

    return True


def generate_round():
    """Generate question and correct answer for game round.

    Returns:
        tuple of question and answer
    """
    number = randint(0, 100)
    answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return (question, answer)
