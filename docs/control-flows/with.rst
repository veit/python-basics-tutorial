Context management with ``with``
================================

A more rational way to encapsulate the ``try``-``except``-``finally`` pattern is
to use the keyword ``with`` and a context manager. Python defines context
managers for things like accessing :doc:`files </save-data/files>` and custom
context managers. One advantage of context managers is that they can define
cleanup actions that are always executed, regardless of whether an exception
occurs or not.

.. seealso::
   :doc:`python3:library/contextlib`

Opening and closing files
-------------------------

The following list shows the opening and reading of a file using ``with`` and a
context manager.

.. literalinclude:: with.py
   :linenos:

A context manager is set up here, which encloses the :func:`open` function and
the subsequent block. The predefined clean-up action of the context manager
closes the file, even if an exception occurs. As long as the expression in the
first line is executed without triggering an exception, the file is always
closed. This code is equivalent to this code:

.. literalinclude:: with_alt.py
   :linenos:

.. seealso::
   * :doc:`../save-data/files`

Locking
-------

:class:`threading.Lock` can be used with ``try``-``finally``:

.. code-block:: Python

   lock = threading.Lock()

   try:
       print("a Job")
       print("another Job")
   finally:
       lock.release()

However, using the context manager is more elegant:

.. code-block:: Python

   with lock:
      print("a Job")
      print("another Job")

.. seealso::
   `Careful threading with locks
   <https://www.python4data.science/en/latest/performance/threading-example.html#Careful-threading-with-locks>`_

Suppressing exceptions
----------------------

Context managers can also be used to suppress the output of :doc:`exceptions`
and continue execution.

.. code-block:: Python

   try:
       os.remove("somefile.tmp")
   except FileNotFoundError:
       pass

This can be written more elegantly as:

.. code-block:: Python

   from contextlib import suppress

   with suppress(FileNotFoundError):
       os.remove("somefile.tmp")
