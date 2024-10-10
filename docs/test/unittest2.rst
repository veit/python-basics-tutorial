``unittest2``
=============

`unittest2 <https://pypi.org/project/unittest2/>`_ is a backport of
:mod:`unittest`, with improved API and assertions than in previous Python
versions.

Example
-------

You may want to import the module under the name ``unittest`` to make it easier
to port code to newer versions of the module in the future:

.. code-block:: python

    import unittest2 as unittest


    class MyTest(unittest.TestCase):
        pass

This way, if you switch to a newer Python version and no longer need the
``unittest2`` module, you can simply change the import in your test module
without having to change any further code.

Installation
------------


    .. tab:: Linux/macOS

         .. code-block:: console

            $ python -m pip install unittest2

    .. tab:: Windows

         .. code-block:: ps1con

            C:> python -m pip install unittest2
