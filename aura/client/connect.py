#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Handles connection related functionality
"""

# Twisted imports
from twisted.internet import defer
from twisted.internet import reactor

# protocol
from protocol.CommandClientFactory import CommandClientFactory
from protocol.CommandClientProtocol import CommandClientProtocol

def connect(host, port, name='default'):
    """
    Starts the factory
    """
    factory = CommandClientFactory(name) # setting up the factory
    factory.protocol = CommandClientProtocol
    reactor.connectTCP(host, port, factory)
