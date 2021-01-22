
import os
from datetime import datetime as dt

VERSION = '1.0.0'

print('CmdPy [Version {}]\n(c) 2021 Fred Pashley. All rights reserved.'.format(VERSION))

class Command:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = list(arguments)

def invalid_line(command):
    print("When using the '{}' command, you provided an invalid command line.".format(command))



HelpCommand = Command('help', ['help', 'ping'])
PingCommand = Command('ping', [])

COMMANDS = []
for item in HelpCommand.arguments:
    COMMANDS.append(item)

while True:

    rawUserCommand = input('\n{}>'.format(str(os.path.dirname(os.path.realpath(__file__)))))

    UserArguments = []
    if len(rawUserCommand.split()) > 1:
        UserCommand = rawUserCommand.split()[0]
        for item in rawUserCommand.split()[1:]:
            UserArguments.append(item.lower())
    else:
        UserCommand = rawUserCommand.split()[0].lower()

    if UserCommand in COMMANDS:
        if UserCommand == HelpCommand.name:
            if UserArguments == []:
                print('For more information on a specific command, type HELP command-name')
                for item in COMMANDS:
                    print(item.upper())
            elif UserArguments[0] in HelpCommand.arguments:
                if UserArguments[0] == 'help':
                    print('Basic help command for CmdPy.\n\nSyntax: HELP command-name\n\nLeave command-name blank for list of commands,\nor specify a command for more detail.')
                elif UserArguments[0] == 'ping':
                    print('Pings the specified host. Returns the average time in milli-seconds.\n\nSyntax: PING host\n\nHost is a required field.')
            else:
                invalid_line('help')
        elif UserCommand == PingCommand.name:
            if UserArguments == []:
                invalid_line('ping')
            else:
                print(os.system(f'ping {UserArguments[0]}'))
    elif UserCommand == '':
        pass
    else:
        print("'{}' is not recognised as a command.".format(rawUserCommand[0]))