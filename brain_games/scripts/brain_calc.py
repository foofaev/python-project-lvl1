#!/usr/bin/env python

"""Calc game start script."""


from brain_games import engine
from brain_games.games import brain_calc


def main():
    """Run a game."""
    engine.play_game(brain_calc)


if __name__ == '__main__':
    main()
