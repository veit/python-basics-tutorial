tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating virtualenv environment
management and testing with multiple interpreter configurations.

#. Installation

   .. tabs::

      .. tab:: Linux/MacOS

         .. code-block:: console

            $ bin/python -m pip install tox

      .. tab:: Windows

         .. code-block:: ps1con

            C:> Scripts\python -m pip install tox

#. Configuration

   With tox you can configure complex multi-parameter test matrices via a simple
   configuration file in the `INI <https://en.wikipedia.org/wiki/INI_file>`_ style,
   for example:

   .. literalinclude:: tox.ini
      :language: ini
      :lineno-start: 1
