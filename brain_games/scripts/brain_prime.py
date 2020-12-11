#!/usr/bin/env python

"""Prime game start script."""


from brain_games import engine
from brain_games.games import brain_prime


def main():
    """Run a game."""
    engine.start_game(brain_prime)


if __name__ == '__main__':
    main()
