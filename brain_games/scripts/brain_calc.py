#!/usr/bin/env python

"""Calc game start script."""


from brain_games import engine
from brain_games.games import brain_calc


def main():
    """Run a game."""
    engine.start_game(brain_calc)


if __name__ == '__main__':
    main()
