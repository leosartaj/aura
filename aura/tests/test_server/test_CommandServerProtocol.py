#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import os
from twisted.trial import unittest
from aura.server.protocol.CommandServerFactory import CommandServerFactory
from aura.tests.test_server import helpers
from aura import command as cmd

class TestCommandServerProtocol(unittest.TestCase):
    """
    tests the command server protocol
    """
    from os import linesep as delimiter # os supported delimiter

    def setUp(self):
        self.factory = CommandServerFactory()
        self.proto, self.tr = helpers.connect(self.factory)

    def _prepare(self, data):
        return data + self.delimiter
        
    def test_register_client(self):
        name = 'testing'
        data = self._prepare(cmd.servercmd('reg', name))
        self.proto.dataReceived(data)
        self.assertEqual(name, self.proto.peername)

    def test_relay(self):
        proto2, tr2 = helpers.connect(self.factory)
        send = 'testing'
        proto2.relay(send)
        self.assertEqual(self.tr.value(), self._prepare(send))
