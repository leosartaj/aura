"""
Helper functions related to server stuff
"""

# Twisted Imports
from twisted.internet import reactor
from twisted.internet import error

# factory/protocol imports
from protocol.CommandServerFactory import CommandServerFactory
from protocol.CommandServerProtocol import CommandServerProtocol

def listen(host, port):
    """
    Starts the server listening
    on the host and port
    returns True if server is setup
    otherwise returns False
    """
    factory = CommandServerFactory() # initialize factory
    factory.protocol = CommandServerProtocol 
    try:
        listener = reactor.listenTCP(port, factory, interface=host)
    except error.CannotListenError:
        return None, None # could not start
    return listener, factory