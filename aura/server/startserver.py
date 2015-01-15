#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Helper functions related to server stuff
"""

# Twisted Imports
from twisted.internet import reactor
from twisted.internet import error

# factory/protocol imports
from protocol.CommandServerFactory import CommandServerFactory

def listen(host, port):
    """
    Starts the server listening
    on the host and port
    returns True if server is setup
    otherwise returns False
    """
    factory = CommandServerFactory() # initialize factory
    try:
        listener = reactor.listenTCP(port, factory, interface=host)
    except error.CannotListenError:
        return None, None # could not start
    return listener, factory
