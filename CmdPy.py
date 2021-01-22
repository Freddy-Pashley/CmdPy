
import os
from datetime import datetime as dt

VERSION = '1.0.0'

print('CmdPy [Version {}]\n(c) 2021 Fred Pashley. All rights reserved.\n'.format(VERSION))

class Command:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = list(arguments)

COMMANDS = ['help']

HelpCommand = Command('help', ['help'])

while True:

    rawUserCommand = input('{}>'.format(str(os.path.dirname(os.path.realpath(__file__)))))

    UserArguments = []
    if len(rawUserCommand.split()) > 1:
        UserCommand = rawUserCommand.split()[0]
        for item in rawUserCommand.split()[1:]:
            UserArguments.append(item.lower())
    else:
        UserCommand = rawUserCommand.split()[0].lower()

    if UserCommand in COMMANDS:
        if UserCommand == HelpCommand.name:
            print('help')
    elif UserCommand == '':
        pass
    else:
        print("'{}' is not recognised as a command.".format(rawUserCommand[0]))