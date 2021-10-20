tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating virtualenv environment
management and testing with multiple interpreter configurations.

#. Installation

   .. code-block:: console

      $ python -m pip install tox

#. Configuration

   With tox you can configure complex multi-parameter test matrices via a simple
   configuration file in the `INI <https://en.wikipedia.org/wiki/INI_file>`_ style,
   for example:

   .. literalinclude:: tox.ini
      :language: ini
      :lineno-start: 1
