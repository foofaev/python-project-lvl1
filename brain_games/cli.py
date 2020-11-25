"""brain_games cli script."""

import prompt


def welcome_user():
    """Welcomes new user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
