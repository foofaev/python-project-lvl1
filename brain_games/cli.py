"""Initial cli module. Ignore it."""

import prompt


def welcome_user():
    """Welcomes user to the set of games."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
