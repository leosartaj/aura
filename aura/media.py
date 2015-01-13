#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import pyglet

def getPlayer():
    """
    returns a player
    """
    player = pyglet.media.Player()
    return player

def addAudio(player, queue=[], streaming=False):
    """
    Adds files to queue on the player
    """
    if not queue:
        return
    if player.playing:
        player.pause()
    for audio in queue:
        load = pyglet.media.load(audio, streaming=False)
        player.queue(load)
    if not player.playing:
        player.play()

def playAudio(player, change=False, seek=None):
    """
    Play current source in a player
    optionally seek to a certain value
    """
    if change:
        player.next
    if seek:
        if player.playing:
            player.pause()
        player.seek(seek)
    if not player.playing:
        player.play()

def startLoop():
    """
    Start the event loop
    """
    pyglet.app.run()
