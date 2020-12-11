"""
Mini-game "arithmetic progression".

Player should find missing element of provided progression.
"""

from random import randint

OBJECTIVE = 'What number is missing in the progression?'

PROGESSION_SIZE = 10

MIN_STEP = 1
MAX_STEP = 10


def generate_question(first_element: int, step: int, index_of_missing: int):
    """Generate string representing arithmetic progression with missing element.

    Args:
        first_element (int): initial element of the progression
        step (int): Step of the progression
        index_of_missing (int): Index of missing element

    Returns:
        str: Description of return value
    """
    progression = ''
    index = 0
    while index < PROGESSION_SIZE:
        separator = '' if index == 0 else ', '
        next_element = (
            '..'
            if index_of_missing == index
            else first_element + index * step
        )
        progression += '{0}{1}'.format(separator, next_element)
        index += 1
    return progression


def generate_round():
    """Generate question and correct answer for game round.

    Returns:
        tuple of question and answer
    """
    first_element = randint(0, 100)
    index_of_missing = randint(0, PROGESSION_SIZE - 1)
    step = randint(MIN_STEP, MAX_STEP)
    missing_element = first_element + step * index_of_missing

    question = generate_question(first_element, step, index_of_missing)

    return (question, str(missing_element))
