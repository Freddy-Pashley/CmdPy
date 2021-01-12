"""
Product details.
"""
# Author: Fred Pashley
# License: MIT
# Date of creation: 12/01/2021
# Current Version: 1.0.1

"""
Product version.
This is the current version, and not always the latest.
"""
VERSION = '1.0.1'

"""
All imports.
Imports are prefered to be whole modules/packages, not sub-modules.
This is to prevent errors with code and text later.
"""
import os
import sys
import time

"""
Gets current directory of CmdPy file.
"""
CURRENTDIR = str(os.path.dirname(os.path.realpath(__file__)))
COMMANDS = ['HELP', 'EXIT']

"""
Prints welcome and copyright.
Version automatically updates from VERSION variable above.
"""
print(f'CmdPy [Version {VERSION}] | (c) 2021 Fred Pashley\nThis product is protected my a MIT license | All rights reserved')

"""
Stops the program from quitting after command.
"""
while True:

    """
    Gets command from user.
    """
    raw_cmd = input(f'\n{CURRENTDIR}>')

    """
    Splits the entire string for arguments.
    """
    i = raw_cmd.split()

    """
    Checks if the command sent was empty.
    If empty, passes and repeats.
    If there are arguments, saves to a list.
    """
    if i == []:
        pass
    elif len(i) > 1:
        ARGUMENTS = []
        for item in i[1:]:
            ARGUMENTS.append(item)

    """
    Gets command not arguments.
    """
    COMMAND = str(i[0]).upper()

    """
    Checks for command.
    """
    if COMMAND in COMMANDS:
        if COMMAND == 'HELP':
            print('For more information on a command, type HELP command-name.\n')
            for item in COMMANDS:
                print(item.upper())
            print('\nYou can also check the online documentation for a more detailed\nexplanation of a command, or if you are having any issues.')

        elif COMMAND == 'EXIT':
            quit()

    else:
        print(f"'{COMMAND.lower()}' is not recognised as a command.\nIf this is unexpected, please check the online documentation for help.")