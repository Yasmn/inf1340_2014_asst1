__author__ = 'user'

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """
    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        if grade in ("A+", "A", "A-", "B+", "b+", "B-", "B", "FZ"):
            letter_grade = grade
            # check that the grade is one of the accepted values
            # assign grade to letter_grade
        else:
            raise ValueError("Parameter is out of range")

    elif type(grade) is int:

        if (grade >= 90) and (grade <= 100):
            grade = str("A+")
            letter_grade = str(grade)
        elif (grade >= 85) and (grade <= 89):
            grade = str("A")
            letter_grade = str(grade)
        elif (grade >= 80) and (grade <= 84):
            grade = str("A-")
            letter_grade = str(grade)
        elif (grade >= 77) and (grade <= 79):
            grade = str("B+")
            letter_grade = str(grade)
        elif (grade >= 73) and (grade <= 76):
            grade = str("B")
            letter_grade = str(grade)
        elif (grade >= 70) and (grade <= 72):
            grade = str("B-")
            letter_grade = str(grade)
        elif (grade >= 0) and (grade <= 69):
            grade = str("FZ")
            letter_grade = str(grade)
        else:
            raise ValueError("Parameter is out of range")
    # check that grade is in the accepted range
    # convert the numeric grade to a letter grade
    # assign the value to letter_grade
    # hint: letter_grade = mark_to_letter(grade)
    else:
        # raise a TypeError exception
        print("error")
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7

    elif letter_grade == "B+":
        gpa = 3.3

    elif letter_grade == "B":
        gpa = 3.0

    elif letter_grade == "B-":
        gpa = 2.7

    elif letter_grade == "FZ":
        gpa = 0.0

    return gpa

