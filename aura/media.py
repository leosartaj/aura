#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Handles the media related functionality
"""

import pyglet

def startLoop():
    """
    Start the event loop
    """
    pyglet.app.run()

class MediaPlayer(pyglet.media.Player):
    """
    Media Player 
    """
    def __init__(self):
        self.now = None
        super(MediaPlayer, self).__init__()

    def _load(self, audio, source=False):
        """
        Adds a file to the queue
        """
        if not source:
            audio = pyglet.media.load(audio, streaming=False)
        self.queue(audio)

    def seekto(self, seek):
        """
        Seek to a particular time in the current audio
        """
        if self.playing:
            self.pause()
        self.seek(seek)
        if not self.playing:
            self.play()

    def playFile(self, audio, seek=None, source=False):
        """
        Play a file
        """
        self._load(audio, source)
        self.next
        self.now = audio
        if seek:
            self.seekto(seek)
