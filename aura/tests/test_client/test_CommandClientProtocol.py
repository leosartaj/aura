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
from aura.client.protocol.CommandClientFactory import CommandClientFactory
from aura import command as cmd
from aura.tests import helpers

class TestCommandClientProtocol(unittest.TestCase):
    """
    tests the command client protocol
    """
    from os import linesep as delimiter # os supported delimiter

    def setUp(self):
        self.name = 'testing'
        self.factory = CommandClientFactory(self.name)

    def _prepare(self, data):
        return data + self.delimiter

    def test_setName(self):
        proto, tr = helpers.connect(self.factory)
        self.assertEqual(proto.name, self.name)
        expected = self._prepare(cmd.servercmd('reg', self.name))
        self.assertEqual(tr.value(), expected)
