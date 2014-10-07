#!/usr/bin/env python3
__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"
# this is to designate the results for each entry


def decide_rps(player1, player2):
    """ Returns the winner of rock, paper, scissors game for a given choice

    :param:
        player1, player2: players' choices (string)

    :return:
    0: if it's a tie
    1: if player 1 wins
    2: if player 2 wins

    :raises:
        TypeError if parameter is not a string
        Invalid input if parameter is not one of the choices
    """
    # check the input
    # raise error if not one of the valid choices (rock, paper,scissors)

    if player1 and player2 in ("Rock", "Paper", "Scissors"):
        # add players choices in a data dictionary
        result_check = {"Rock" "Paper": 2, "Rock" "Scissors": 1, "Rock" "Rock": 0, "Scissors" "Paper": 1,
                        "Scissors" "Rock": 2, "Scissors" "Scissors": 0, "Paper" "Scissors": 2, "Paper" "Rock": 1,
                        "Paper" "Paper": 0}
        # check the result against players' choices
        result = player1 + player2
        return result_check[result]
    else:
        raise TypeError("invalid input passed as a parameter")




