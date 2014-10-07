#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    input_type = True
    par_length = True
    correct = True
    not_correct = False

    if type(upc) is str:
        input_type = True
    else:
        print("error")
        raise TypeError("Invalid type passed as parameter")
        # check type of input
        # raise TypeError if not string

    if len(upc) == 12:
        par_length = True
    elif len(upc) < 12:
        raise ValueError({12 - len(upc): "parameter length is "})
    elif len(upc) > 12:
        raise ValueError({len(upc) - 12: "parameter length is "})
        # check length of string
        # raise ValueError if not 12

    # convert string to array
    # hint: use the list function
    upc_list = list(upc)

    #convert list to integers
    int_list = [int(i) for i in upc_list]
    odd_digits = int_list[0] + int_list[2] + int_list[4] + int_list[6] + int_list[8] + int_list[10]
    # calculate the twelfth digit
    odd_digits *= 3
    even_digits = int_list[1] + int_list[3] + int_list[5] + int_list[7] + int_list[9]
    result = odd_digits + even_digits
    result %= 10
    check_sum = 10 - result

    if check_sum == int_list[11]:
        return True
        # generate checksum using the first 11 digits provided
        # check against the the twelfth digit
        # return True if they are equal, False otherwise
    else:
        return False
