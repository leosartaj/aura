"""
Development script
To run without actually installing
Picks up local changes
"""

# system imports
import sys

# twisted imports
from twisted.internet import reactor

# Other imports
import main
from server import startserver as start
from client import connect

if __name__ == '__main__':
    main.startLogging(sys.stdout)
    if sys.argv.pop() == 's':
        start.listen('127.0.0.1', 9001)
    else:
        connect.connect('127.0.0.1', 9001)


    reactor.run()

