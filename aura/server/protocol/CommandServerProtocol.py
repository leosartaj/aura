#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# system imports
import os

# twisted imports
from twisted.protocols import basic
from twisted.python import log

# user imports
from aura import command as cmd

CLIENT_PREFIX = cmd.CLIENT_PREFIX

class CommandServerProtocol(basic.LineReceiver):
    """
    Implements the server interaction protocol
    """
    from os import linesep as delimiter # os supported delimiter

    def connectionMade(self):
        self.peer = self.transport.getPeer()
        self.player = self.factory.player
        self.peername = 'unregistered'
        self.factory.updateClients(self)
        log.msg('Connected to %s' %(self.peer))
        self.tell_client()

    def tell_client(self):
        player = self.player
        volume = str(player.volume)
        volumecmd = cmd.clientcmd('volume', volume)
        self.sendLine(volumecmd)
        if player.playing:
            playing = player.now
            seek = str(player.time)
            value = cmd.join([playing, seek])
            playcmd = cmd.clientcmd('play', value)
            self.sendLine(playcmd)

    def lineReceived(self, line):
        """
        Handle received lines
        """
        if not self._parse(line):
            log.msg('Received %s from %s' %(line, self.peername))

    def _parse(self, line):
        """
        Parse line for commands
        returns True if line contains a command
        and calls the command
        otherwise simply returns False
        """
        comd, value = cmd.parse(line, CLIENT_PREFIX)
        if comd == 'reg':
            self.peername = value
            log.msg('PeerName of %s is %s' %(self.peer, self.peername))
        else:
            return False
        return True

    def sendcmd(self, comd, value):
        """
        sends a command to the client
        """
        tosend = cmd.clientcmd(comd, value)
        self.sendLine(tosend)

    def relay(self, line):
        """
        relay the message to other clients
        """
        for client in self.factory.getClients():
            if client != self:
                client.sendLine(line)

    def connectionLost(self, reason):
        """
        safely disconnect user
        """
        self.factory.removeClients(self)
        self._logConnectionLost(reason)

    def _logConnectionLost(self, reason):
        """
        log when connection is lost
        """
        line = 'Disconnected from %s' %(self.peer)
        log.msg(line)
        log.msg(reason.getErrorMessage())
