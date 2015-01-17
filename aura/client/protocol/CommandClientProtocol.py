#!/usr/bin/env python2

##
# Aura
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

# User imports
import command as cmd
import media

SERVER_PREFIX = cmd.SERVER_PREFIX

class CommandClientProtocol(basic.LineReceiver):
    """
    Implements the client interaction protocol
    """
    from os import linesep as delimiter # os supported delimiter

    def connectionMade(self):
        self.peer = self.transport.getPeer()
        log.msg('Connected to server at %s' % (self.peer)) # logs the connection

        self.player = media.MediaPlayer()

        self.name = self.factory.name
        setName = cmd.servercmd('reg', self.name)
        self.sendLine(setName) # register with server

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
        line = self._parse(line)
        if line:
            log.msg('%s' % (line))

    def _parse(self, line):
        """
        Parse line for commands
        """
        comd, value = cmd.parse(line, SERVER_PREFIX)
        player = self.player
        if comd == 'play':
            if not player.playing:
                player.play()
            audio, seek = cmd.separate(value)
            player.playFile(audio, seek=float(seek))
            newline = 'Player started playing %s' %(value)
        elif comd == 'seek':
            value = float(value)
            player.seekto(value)
            newline = 'Forwared to %d seconds' %(value)
        elif comd == 'pause':
            player.pause()
            newline = 'Player Paused'
        elif comd == 'volume':
            value = float(value)
            player.volume = value
            newline = 'Volume changed to %d' %(value)
        else:
            return line
        return newline
