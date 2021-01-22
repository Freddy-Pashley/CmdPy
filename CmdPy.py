

import os
from datetime import datetime as dt

try:
    with open('debug.log', 'r') as debugfile:
        pass
except FileNotFoundError:
    with open('debug.log', 'x') as debugfile:
        debugfile.write(f'[{dt.now()}] debug.log file not found, creating in default directory.')

import time

VERSION = '1.0.1'

print('CmdPy [Version {}]\n(c) 2021 Fred Pashley. All rights reserved.'.format(VERSION))

class Command:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = list(arguments)

def invalid_line(command):
    print("When using the '{}' command, you provided an invalid command line.".format(command))



HelpCommand = Command('help', ['help', 'ping', 'timer'])
PingCommand = Command('ping', [])
TimerCommand = Command('timer', [])

COMMANDS = []
for item in HelpCommand.arguments:
    COMMANDS.append(item)

while True:

    CURRENTDIRECTORY = str(os.path.dirname(os.path.realpath(__file__)))

    rawUserCommand = input('\n{}>'.format(CURRENTDIRECTORY))

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
                elif UserArguments[0] == 'timer':
                    print('Sets a timer for a certain amount of time.\n\nSyntax: TIMER length\n\nLength    ... NumberUnit\nFor example, TIMER 10ms.\nValid units of time: ms, s, m, h')
            else:
                invalid_line('help')
        elif UserCommand == PingCommand.name:
            if UserArguments == []:
                invalid_line('ping')
            else:
                print(os.system(f'ping {UserArguments[0]}'))
        elif UserCommand == TimerCommand.name:
            if UserArguments == []:
                invalid_line('timer')
            elif len(UserArguments) > 1:
                invalid_line('timer')
            else:
                amount = UserArguments[0]
                numberstring = ''; unit = ''
                for char in amount:
                    if char in '0123456789':
                        if numberstring == '':
                            numberstring = char
                        else:
                            numberstring = f'{numberstring}{char}'
                    else:
                        if unit == '':
                            unit = char
                        else:
                            unit = f'{unit}{char}'
                amount = int(numberstring)
                if unit == 's':
                    print('Timing {} seconds...'.format(str(amount)))
                    time.sleep(amount)
                    print('Stopped!')
                elif unit == 'm':
                    print('Timing {} minutes...'.format(str(amount)))
                    amount = amount * 60
                    time.sleep(amount)
                    print('Stopped!')
                elif unit == 'h':
                    print('Timing {} hours...'.format(str(amount)))
                    amount = amount * 3600
                    time.sleep(amount)
                    print('Stopped!')
                elif unit == 'ms':
                    print('Timing {} milli-seconds...'.format(str(amount)))
                    amount = amount / 1000
                    time.sleep(amount)
                    print('Stopped!')
                else:
                    invalid_line('timer')
    elif UserCommand == '':
        pass
    else:
        print("'{}' is not recognised as a command.".format(rawUserCommand))