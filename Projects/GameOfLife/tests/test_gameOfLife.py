## File to be run to test - currently two test pass and one fails
## ran using pytest test_gameOfLife.py on console

import sys
import os

from Projects.GameOfLife.GameOfLife import GameOfLife

test_obj = GameOfLife(3, 1, 0)


def test_initial_grid_creation():
    test_obj.make_grid()
    assert test_obj.grid == [[1, 0, 1], [1, 0, 1], [1, 0, 1]]


def test_game_of_life():
    test_obj.play()
    assert test_obj.grid == [[0, 0, 0], [1, 0, 1], [0, 0, 0]]


# failure case of test
def test_game_of_life_failure():
    test_obj.play()
    assert test_obj.grid == [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
