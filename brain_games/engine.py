"""Game engine."""

import prompt

ROUNDS_COUNT = 3


def start_game(game):
    """Run provided game.

    Args:
        game: a game module from ./games.
            Should contain function generate_round and constant OBJECTIVE
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.OBJECTIVE)

    current_round = 0
    while current_round < ROUNDS_COUNT:
        current_round += 1
        (question, answer) = game.generate_round()
        print('Question: {0}'.format(question))
        player_answer = prompt.string('Your answer: ')

        if player_answer != answer:
            print('{0} is wrong answer ;(. Correct answer was {1}'.format(
                player_answer,
                answer,
            ))
            print("Let's try again, {0}!".format(name))
            return

        print('Correct!')

    print('Congratulations, {0}!'.format(name))
