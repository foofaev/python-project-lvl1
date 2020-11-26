"""Game engine."""

import prompt

ROUNDS_COUNT = 3

negative_message = """
'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}
"""

positive_message = 'Correct!'


def start_game(game):
    """Run provided game."""
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
            print(negative_message.format(player_answer, answer, name))
            return

        print(positive_message)

    print('Congratulations, {0}'.format(name))
