#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from twisted.test import proto_helpers

def connect(factory):
    proto = factory.buildProtocol(('127.0.0.1', 0))
    tr = proto_helpers.StringTransportWithDisconnection()
    tr.protocol = proto
    proto.makeConnection(tr)
    return proto, tr

def connect_multiple(factory, num=1):
    for dummy_cou in range(num):
        connect(factory)
