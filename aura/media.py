#!/usr/bin/env python2

##
# PyChat
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import pyglet

def getPlayer(queue=[]):
    """
    returns a player
    """
    player = pyglet.media.Player()
    return player

def addAudio(player, queue=[]):
    """
    Adds files to queue on the player
    """
    for audio in queue:
        load = pyglet.media.load(audio, streaming=False)
        player.queue(load)

def playAudio(player, seek=None):
    """
    Play current source in a player
    optionally seek to a certain value
    """
    if seek:
        player.pause()
        player.seek(seek)
    if not player.playing:
        player.play()
