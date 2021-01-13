"""
Product details.
"""
# Author: Fred Pashley
# License: MIT
# Date of creation: 12/01/2021
# Current Version: 1.0.2

"""
Product version.
This is the current version, and not always the latest.
"""
VERSION = '1.0.2'

"""
All imports.
Imports are prefered to be whole modules/packages, not sub-modules.
This is to prevent errors with code and text later.
System installes any modules that are not available on local machine.
"""
import os
import sys
import time
try:
    import pytz
except ImportError:
    os.system('pip install pytz')

"""
Gets current directory of CmdPy file.
"""
CURRENTDIR = str(os.path.dirname(os.path.realpath(__file__)))
COMMANDS = ['HELP', 'EXIT', 'VERSION', 'CLEAR']
COMMANDS_SORTED = sorted(COMMANDS)

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
    Splits the entire string to check for arguments into a list.
    """
    i = raw_cmd.split()

    """
    Checks if there are arguments specified.
    Or checks if no arguments specified.
    Sets ARGUMENTS list respectively.
    """
    if len(i) > 1:
        ARGUMENTS = []
        for item in i[1:]:
            ARGUMENTS.append(item.upper())
    elif len(i) == 1:
        ARGUMENTS = []
    elif len(i) == 0:
        pass

    """
    Gets command not arguments.
    """
    if len(i) > 0:
        COMMAND = str(i[0]).upper()
    else:
        pass

    """
    Checks for command.
    """
    if COMMAND in COMMANDS:
        if COMMAND == 'HELP':
            if ARGUMENTS == []:
                print('For more information on a command, type HELP command-name.\n')
                for item in COMMANDS_SORTED:
                    print(item.upper())
                print('\nYou can also check the online documentation for a more detailed\nexplanation of a command, or if you are having any issues.')
            else:
                """
                Gets the first arguments and assigns it as the command the user needs help with.
                This is already in upper-form, as when the ARGUMENTS list is created each argument is appended as upper.
                """
                help_command = ARGUMENTS[0]
                
                """
                Checks for command.
                """
                if help_command == 'HELP':
                    print('Provides help information for CmdPy commands.\n\nSyntax: HELP command-name')
                
                elif help_command == 'EXIT':
                    print('Exits CmdPy.\n\nSyntax: EXIT')

                elif help_command == 'VERSION':
                    print('Provides the version of CmdPy you are using.\n\nSyntax: VERSION')

                elif help_command == 'CLEAR':
                    print('Clears the screen.\n\nSyntax: CLEAR')

        elif COMMAND == 'EXIT':
            quit()

        elif COMMAND == 'VERSION':
            print(VERSION)

        elif COMMAND == 'CLEAR':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

    else:
        print(f"'{COMMAND.lower()}' is not recognised as a command.\nIf this is unexpected, please check the online documentation for help.")
