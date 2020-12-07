"""Mini-game "calc". Player should solve the task given."""

from random import choice, randint

OBJECTIVE = 'What is the result of the expression?'
OPERANDS = ('+', '-', '*')


def calculate(first_number: int, second_number: int, operand: str) -> int:
    """Calculate result of the expression defined by provided operand.

    Args:
        first_number (int): first arg of calc operation
        second_number (int): second arg of calc operation
        operand (str): operand to use in calc operation

    Returns:
        int: Result of math operation

    Raises:
        ValueError: If invalid operand type
    """
    if operand == '+':
        return first_number + second_number
    elif operand == '-':
        return first_number - second_number
    elif operand == '*':
        return first_number * second_number
    raise ValueError


def generate_round():
    """Generate question and correct answer for game round.

    Returns:
        Question and answer for game engine
    """
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operand = choice(OPERANDS)
    answer = str(calculate(first_number, second_number, operand))
    question = '{0} {1} {2}'.format(first_number, operand, second_number)
    return (question, answer)
