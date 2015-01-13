#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

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

