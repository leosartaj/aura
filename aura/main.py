#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Main module
Contains wrapper functions
"""

# system imports
import sys

# twisted imports
from twisted.python import log

# Other imports
from server import startserver

def startLogging(handle):
    """
    Starts the logging
    """
    log.startLogging(handle)

def run(clientname, handle=sys.stdout, addresses=[]):
    """
    Runs the Gui
    address is a list of tuples(host, port, server)
    host:port is the ip:port to connect to
    server is a boolean definig whether to start a server or not
    """
    pass
