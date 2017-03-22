#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2015 Chintalagiri Shashank
# Released under the MIT license.

"""

Simple Deployment Example
-------------------------

"""

from prefab_server.serve import get_resource
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import logging
logging.basicConfig(level=logging.DEBUG)


SERVER_PORT = 1081

if __name__ == '__main__':
    root = Resource()
    prefab_resource = get_resource(root)
    factory = Site(root)
    reactor.listenTCP(SERVER_PORT, factory)
    reactor.run()
