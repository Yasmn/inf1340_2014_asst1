#!/usr/bin/env python3
__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs give the correct result
    """
    assert decide_rps('Rock', 'Paper') == 2
    assert decide_rps('Scissors', 'Scissors') == 0
    assert decide_rps('Rock', 'Scissors') == 1
    assert decide_rps('Rock', 'Rock') == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Scissors", "Rock") == 2


def test_input():
    """ Inputs are one of the valid choices
    """
    with pytest.raises(TypeError):
        decide_rps("roc", "scissors")

    with pytest.raises(TypeError):
        decide_rps("paper","stone")

    with pytest.raises(TypeError):
        decide_rps(1, 2)

    with pytest.raises(TypeError):
        decide_rps(3, "rock")