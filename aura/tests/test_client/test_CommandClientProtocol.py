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
        self.dire = os.path.dirname(os.path.realpath(__file__))
        self.audio = os.path.join(self.dire + '/../', 'bach.mp3')
        self.factory = CommandClientFactory(self.name)
        self.proto, self.tr = helpers.connect(self.factory)

    def _prepare(self, data):
        return data + self.delimiter

    def test_setName(self):
        proto, tr = self.proto, self.tr
        self.assertEqual(proto.name, self.name)
        expected = self._prepare(cmd.servercmd('reg', self.name))
        self.assertEqual(tr.value(), expected)

    def test_play(self):
        proto, tr = self.proto, self.tr
        self.assertEqual(proto.player.now, None)
        playcmd = self._prepare(cmd.clientcmd('play', self.audio))
        proto.dataReceived(playcmd)
        self.assertEqual(proto.player.now, self.audio)

    def test_pause(self):
        proto, tr = self.proto, self.tr
        proto.player.play()
        self.assertTrue(proto.player.playing)
        pausecmd = self._prepare(cmd.clientcmd('pause'))
        proto.dataReceived(pausecmd)
        self.assertFalse(proto.player.playing)

    def test_volume(self):
        proto, tr = self.proto, self.tr
        volcmd = self._prepare(cmd.clientcmd('volume', '0.2'))
        proto.dataReceived(volcmd)
        self.assertEqual(proto.player.volume, 0.2)
