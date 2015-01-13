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

class CommandClientFactory(ClientFactory):
    """
    Implements the client factory
    """
    def __init__(self, name):
        self.name = name

    def buildProtocoll(self, addr):
        proto = ClientFactory.buildProtocol(self, addr)
        return proto

    def clientConnectionFailed(self, connector, reason):
        log.err(reason.getErrorMessage())

    def clientConnectionLost(self, connector, reason):
        log.err(reason.getErrorMessage())
