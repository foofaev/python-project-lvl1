#!/usr/bin/env python

"""Even game start script."""

from brain_games import engine
from brain_games.games import brain_even


def main():
    """Run a game."""
    engine.start_game(brain_even)


if __name__ == '__main__':
    main()
