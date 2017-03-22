#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2015 Chintalagiri Shashank
# Released under the MIT license.

"""
Sets up a :class:`twisted.web.resource.Resource` hierarchy containing the
available pre-assembled data elements.
"""

import jsonpickle
from fastjsonrpc.server import JSONRPCServer

from twisted.web.resource import Resource
from twisted.web import server
from twisted.application import internet
from twisted.python import log

from tendril.entityhub import supersets


SERVER_PORT = 1081


class PrefabEndpoint(JSONRPCServer):
    """

    A :class:`fastjsonrpc.server.JSONRPCServer` (and subsequently,
    :class:`twisted.web.resource.Resource` subclass), defining the
    interface to the pre-assembled data elements.

    """
    def setup(self):
        supersets.get_bom_superset()
        log.msg('prefab_server Resource Startup Complete')

    def jsonrpc_echo(self, data):
        return data

    def jsonrpc_get_symbol_inclusion(self, ident):
        inclusion = supersets.get_symbol_inclusion(ident, use_prefab=False)
        return jsonpickle.encode(inclusion, make_refs=False)


class PrefabServer(object):
    """
    The JSON-RPC resource tree, created on top of the provided ``root``. If
    no root is provided, one is created (returned by :func:`setup()`).
    """
    def __init__(self, root=None):
        log.msg("Initializing prefab_server Resource")
        self._root = root

    def setup(self):
        """
        Creates the actual resource tree, attaching the various
        filesystems to the provided root.

        :returns: the Root of the Resource tree
        """
        if not self._root:
            log.msg("Creating Site Root")
            self._root = Resource()
        log.msg("Adding JSON-RPC prefab_server Resource")
        ep = PrefabEndpoint()
        ep.setup()
        self._root.putChild('prefab', ep)
        return self._root


def get_resource(root=None):
    """
    Created and returns the resource tree containing the various
    XML-RPC pre-assembled data resources.

    :param root: Root on which the resource tree should be built.
    :return: The root on which the resource tree was built.
    """
    prefab_server = PrefabServer(root)
    root = prefab_server.setup()
    return root


def get_service(port=SERVER_PORT):
    """
    Return a service containing the resource suitable for creating
    an application object.
    """
    root = get_resource()
    prefab_factory = server.Site(root)
    return internet.TCPServer(port, prefab_factory)
