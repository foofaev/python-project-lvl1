#!/usr/bin/env python

"""GCD game start script."""


from brain_games import engine
from brain_games.games import brain_gcd


def main():
    """Run a game."""
    engine.start_game(brain_gcd)


if __name__ == '__main__':
    main()
