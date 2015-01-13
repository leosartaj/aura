#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from twisted.trial import unittest
from aura.server.protocol.CommandServerFactory import CommandServerFactory
from aura.tests.test_server import helpers

class TestCommandServerFactory(unittest.TestCase):
    """
    tests the command server factory
    """
    def setUp(self):
        self.factory = CommandServerFactory()
        self.num = 10

    def _test_connections(self, num):
        connected = len(self.factory.getClients())
        self.assertEqual(num, connected)

    def test_num_clients(self):
        helpers.connect_multiple(self.factory, self.num)
        self._test_connections(self.num)

    def test_disconnect(self):
        helpers.connect_multiple(self.factory, self.num)
        self._test_connections(self.num)
        self.factory.disconnect()
        self._test_connections(0)

    def test_disconnect_partial(self):
        helpers.connect_multiple(self.factory, self.num)
        self._test_connections(self.num)
        proto, tr = helpers.connect(self.factory)
        tr.loseConnection()
        self._test_connections(self.num)
