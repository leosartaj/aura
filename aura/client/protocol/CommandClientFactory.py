#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# twisted imports
from twisted.python import log
from twisted.internet.protocol import ClientFactory

# user imports
from CommandClientProtocol import CommandClientProtocol

class CommandClientFactory(ClientFactory):
    """
    Implements the client factory
    """
    protocol = CommandClientProtocol

    def __init__(self, name):
        self.name = name

    def clientConnectionFailed(self, connector, reason):
        log.err(reason.getErrorMessage())

    def clientConnectionLost(self, connector, reason):
        log.err(reason.getErrorMessage())
