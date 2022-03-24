# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 22:06:33 2022

@author: brigh

The purpose of this file is to provide copy/paste solutions for error handling

"""


def int_only_input(inputString, varName):
    """


    Args:
        inputString (str): This will be displayed to the user and require a response
        varName (str): This is the name of the variable created by the user input

    Returns:
        a global variable with the name defined by varName

    """
    tryLoop = True
    while tryLoop == True:
        try:
            variable = varName
            globals()[variable] = int(input(inputString))
            tryLoop = False
        except ValueError:
            print("integers only")


def words_only_input(inputString, varName):

    tryLoop = True
    while tryLoop == True:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        try:
            variable = varName
            globals()[variable] = input(inputString)

            for character in globals()[variable]:
                if character in numbers:
                    raise ValueError
                else:
                    pass

            tryLoop = False

        except ValueError:
            print("Words only")
