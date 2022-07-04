Context management with ``with`` 
================================

A more rational way to encapsulate the ``try-except-finally`` pattern is to use
the keyword ``with`` and a context manager. Python defines context managers for
things like :doc:`file </types/files>` access and custom context managers. One
advantage of context managers is that they can define default clean-up actions
that are always executed, whether an exception occurs or not.

The following listing shows opening and reading a file using ``with`` and a
context manager.

.. literalinclude:: with.py
   :linenos:

A context manager is set up here that encloses the ``open`` function and the
block that follows it. The predefined clean-up action of the context manager
closes the file even if an exception occurs. As long as the expression in the
first line is executed without throwing an exception, the file is always closed.
This code is equivalent to this code:

.. literalinclude:: with_alt.py
   :linenos:
