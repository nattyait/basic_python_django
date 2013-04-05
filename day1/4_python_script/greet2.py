from getopt import getopt, GetoptError
from greet import greet
import sys

USAGE = """Usage: greet2 [OPTION]... NAME
Greet NAME.

Mandatory arguments to long options are mandatory for short options too.
  -n, --name=NAME   name to greet

Exit status:
 0  if OK,
 1  if minor problems (e.g., missing argument),
 2  if serious trouble (e.g., machine blows up!).
"""

def greet(name):
    return 'Hi %s!' % name

def echo(message):
    print message

def main(argv=[]):
    arguments = argv[1:] or sys.argv[1:]
    
    try:
        names = list()
        opts, args = getopt(arguments, 'n:', ['name='])
        for option, value in opts:
            if option in ('-n', '--name'): 
                names.append(value)
        for arg in args:
            names.append(arg)
    except GetoptError:
        pass
    if not names:
        echo(USAGE)
        return 1
    message = greet(",".join(names))
    echo(message)
    return 0

