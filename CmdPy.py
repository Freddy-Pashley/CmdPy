

import os
from datetime import datetime as dt

try:
    with open('debug.log', 'r') as debugfile:
        pass
except FileNotFoundError:
    with open('debug.log', 'x') as debugfile:
        debugfile.write(f'\n[{dt.now()}] debug.log file not found, creating in default directory.')

import time

VERSION = '1.1.2'

print('CmdPy [Version {}]\n(c) 2021 Fred Pashley. All rights reserved.'.format(VERSION))

class Command:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = list(arguments)

def invalid_line(command):
    print("When using the '{}' command, you provided an invalid command line.".format(command))

def debug(text):
    try:
        with open('debug.log', 'a') as debugfile:
            debugfile.write(f'\n[{dt.now()}] {text}')
    except FileNotFoundError:
        with open('debug.log', 'x') as debugfile:
            debugfile.write(f'\n[{dt.now()}] debug.log file not found, creating in default directory.')
            debugfile.write(f'\n[{dt.now()}] {text}')
    finally:
        print("An error occured. You can check for more details in the 'debug.log' file\nin the same directory as your CmdPy.")

HelpCommand = Command('help', ['help', 'ping', 'timer', 'open', 'exit', 'clear', 'dir', 'debug'])
PingCommand = Command('ping', [])
TimerCommand = Command('timer', [])
OpenCommand = Command('open', [])
ExitCommand = Command('exit', [])
ClearCommand = Command('exit', [])
DirCommand = Command('dir', [])
DebugCommand = Command('debug', ['clear', 'open'])

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
                sort = sorted(COMMANDS)
                for item in sort:
                    print(item.upper())
            elif UserArguments[0] in HelpCommand.arguments:
                if UserArguments[0] == 'help':
                    print('Basic help command for CmdPy.\n\nSyntax: HELP command-name\n\nLeave command-name blank for list of commands,\nor specify a command for more detail.')
                elif UserArguments[0] == 'ping':
                    print('Pings the specified host. Returns the average time in milli-seconds.\n\nSyntax: PING host\n\nHost is a required field.')
                elif UserArguments[0] == 'timer':
                    print('Sets a timer for a certain amount of time.\n\nSyntax: TIMER length\n\nLength    ... NumberUnit\nFor example, TIMER 10ms.\nValid units of time: ms, s, m, h')
                elif UserArguments[0] == 'open':
                    pass # Add help @MQXO
                elif UserArguments[0] == 'exit':
                    print('Exits CmdPy.\n\nSyntax: EXIT')
                elif UserArguments[0] == 'clear':
                    print('Clears the screen.\n\nSyntax: CLEAR')
                elif UserArguments[0] == 'dir':
                    pass
                elif UserArguments[0] == 'debug':
                    print('Debugging control panel.\n\nSyntax: DEBUG option\n\nOptions: clear    ... Clears the debug.log file\n         open    ... Opens the debug.log file')
            else:
                invalid_line('help')
                debug(f"'{UserArguments[0]}' was not found in the help database.")
        elif UserCommand == PingCommand.name:
            if UserArguments == []:
                invalid_line('ping')
                debug("'ping' requires at least one argument, received none")
            else:
                print(os.system(f'ping {UserArguments[0]}'))
        elif UserCommand == TimerCommand.name:
            if UserArguments == []:
                invalid_line('timer')
                debug("'time' requires at least one argument, received none.")
            elif len(UserArguments) > 1:
                invalid_line('timer')
                debug("'time' does not expect more than one argument.")
            else:
                amount = UserArguments[0]
                numberstring = ''; unit = ''
                try:
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
                except Exception as error:
                    debug(error)
                finally:
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
                        debug(f'invalid unit of time. expected [s, m h, ms] but received "{unit}" instead.')
        elif UserCommand == OpenCommand.name:
            if UserArguments == []:
                invalid_line('open')
                debug(f"'open' command requires at least 1 argument, but instead got none.")
            else:
                openstring = UserArguments[0]
                if '/' in openstring or '\\' in openstring:
                    directory = UserArguments[0]
                    try:
                        os.startfile(directory)
                    except FileNotFoundError:
                        invalid_line('open')
                        debug(f'invalid directory given to open')
                else:
                    try:
                        os.startfile(UserArguments[0])
                    except FileNotFoundError:
                        invalid_line('open')
                        debug(f'invalid directory given to open')
        elif UserCommand == ExitCommand.name:
            quit()
        elif UserCommand == ClearCommand.name:
            try:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
            except Exception as error:
                debug(error)
        elif UserCommand == DirCommand.name:
            pass
        elif UserCommand == DebugCommand.name:
            if UserArguments[0] in DebugCommand.arguments:
                if UserArguments[0] == 'clear':
                    with open('debug.log', 'w') as f:
                        pass
                elif UserArguments[0] == 'open':
                    try:
                        os.startfile('debug.log')
                    except FileNotFoundError:
                        print('File not found.')
                        debug('debug.log file not found.')
            else:
                invalid_line('debug')
                debug(f"'debug' requires one valid argument.")
    elif UserCommand == '':
        pass
    else:
        print("'{}' is not recognised as a command.".format(rawUserCommand))
        debug(f"'{rawUserCommand}' was not a valid command.")