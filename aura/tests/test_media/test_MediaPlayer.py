#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
import time
import pyglet
from pyglet.media import procedural
from aura import media

class TestMediaPlayer(unittest.TestCase):
    """
    tests the MediaPlayer Class in media module
    """
    def setUp(self):
        self.player = media.MediaPlayer()

    def _sample(self, time=0.5):
        source = procedural.WhiteNoise(time)
        return source

    def test_seekto(self):
        player = self.player
        source = self._sample(1)
        player.playFile(source, source=True)
        old = player.time
        player.seekto(.1)
        diff = abs(old + 0.1 - player.time)
        self.assertTrue(diff < 0.001)

    def test_playFile_no_seek(self):
        player = self.player
        source = self._sample()
        player.playFile(source, source=True)
        player.play()
        old = player.time
        start = time.time()
        while time.time() - start < 0.5:
            player.dispatch_events()
        diff = abs(old - player.time)
        self.assertTrue(diff < 0.001)

    def test_playFile_seek(self):
        player = self.player
        source = self._sample()
        player.playFile(source, seek=0.1, source=True)
        player.play()
        old = player.time
        start = time.time()
        while time.time() - start < 0.5:
            player.dispatch_events()
        diff = abs(old - player.time)
        self.assertTrue(diff < 0.001)
