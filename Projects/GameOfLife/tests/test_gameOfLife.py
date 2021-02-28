## File to be run to test - currently two test pass and one fails
## ran using pytest test_gameOfLife.py on console

import sys
import os

from Projects.GameOfLife.src.gameOfLife import GameOfLife

test_obj=GameOfLife(3,1)

def test_initial_grid_creation():
    assert test_obj.make_grid() == [[1, 0, 1], [1, 0, 1], [1, 0, 1]]

def test_game_of_life():
    assert test_obj.play()==[[0, 0, 0], [1, 0, 1], [0, 0, 0]]

# failure case of test
def test_game_of_life_failure():
    assert test_obj.play() != [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
