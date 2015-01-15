#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##
import pyglet

class MediaPlayer(pyglet.media.Player):
    """
    Media Player functions
    """
    def __init__(self, audio=[]):
        self.audio = audio
        super(MediaPlayer, self).__init__()

    def _load(self, audio):
        """
        Adds a file to the queue
        """
        load = pyglet.media.load(audio, streaming=False)
        self.queue(load)

    def load_files(self, audio):
        """
        save the files to be played
        """
        for file in audio:
            self.audio.append(file)

    def moveto(self, seek):
        """
        Move to a particular time
        """
        if self.playing:
            self.pause()
        self.seek(seek)
        if not self.playing:
            self.play()

    def playFile(self, audio=None, seek=None):
        """
        Play a file
        """
        self._load(audio)
        self.next
        if self.seek:
            self.moveto(seek)

def startLoop():
    """
    Start the event loop
    """
    pyglet.app.run()
