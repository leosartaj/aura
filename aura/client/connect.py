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

# factory
from protocol.CommandClientFactory import CommandClientFactory

def connect(host, port, name='default'):
    """
    Starts the factory
    """
    factory = CommandClientFactory(name) # setting up the factory
    reactor.connectTCP(host, port, factory)
