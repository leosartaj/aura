#!/usr/bin/env python2

##
# PyChat
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# system import
import os

# twisted imports
from twisted.protocols import basic
from twisted.python import log

class CommandClientProtocol(basic.LineReceiver):
    """
    Implements the client interaction protocol
    """
    from os import linesep as delimiter # os supported delimiter

    def connectionMade(self):
        self.peer = self.transport.getPeer()
        log.msg('Connected to server at %s' % (self.peer)) # logs the connection

        #self.name = setName = cmd.servercmd('reg', self.factory.name)
        #self.sendLine(setName) # register with server
        self.sendLine('hi')

    def send(self, text):
        """
        Logs and sends the messages
        """
        log.msg('me %s' % (text))
        self.sendLine(text)

    def lineReceived(self, line):
        """
        Handles recieved line
        """
        log.msg('%s' % (line))
