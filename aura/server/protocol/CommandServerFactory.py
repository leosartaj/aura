#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# Twisted imports
from twisted.python import log
from twisted.internet.protocol import ServerFactory
from twisted.internet import reactor

# user Imports
from CommandServerProtocol import CommandServerProtocol
from aura import media

class CommandServerFactory(ServerFactory):
    """
    Implements the server factory
    """
    protocol = CommandServerProtocol

    def __init__(self):
        self.clients = [] # connected clients
        self.player = media.MediaPlayer()
        self.player.play()
        self.player.playFile('tests/bach.mp3')

    def updateClients(self, client):
        """
        Adds protocol instances of connected clients
        """
        self.clients.append(client)

    def getClients(self):
        """
        returns list of protocol instances of connected clients
        """
        return self.clients

    def disconnect(self):
        """
        Disconnects from all the clients
        """
        for client in self.clients:
            client.transport.loseConnection()
        self.clients = []

    def removeClients(self, client):
        """
        removes protocol instances of connected clients
        """
        index = self.clients.index(client)
        del self.clients[index]
