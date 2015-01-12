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
