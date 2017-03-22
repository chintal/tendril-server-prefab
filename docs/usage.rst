=============
Usage Example
=============

Basic Usage Example
-------------------

.. literalinclude:: ../deploy/runserver.py


Self-contained Usage : Deploy using twistd and systemd
------------------------------------------------------

Twisted ``.tac`` file:

.. literalinclude:: ../deploy/prefab_server.tac

Systemd ``.service`` file:

.. literalinclude:: ../deploy/tendril_prefab_server.service
