#!/usr/bin/env python

"""Progression game start script."""


from brain_games import engine
from brain_games.games import brain_progression


def main():
    """Run a game."""
    engine.start_game(brain_progression)


if __name__ == '__main__':
    main()
