None
====

In addition to the standard types such as :doc:`strings` and :doc:`numbers`,
Python has a special data type that defines a single special data object called
``None``. As the name suggests, ``None`` is used to represent an empty value. It
appears in various forms in Python.

``None`` is often useful in everyday Python programming as a placeholder to
indicate a data structure where meaningful data can eventually be found, even if
that data has not yet been calculated.

The presence of ``None`` is easy to check, as there is only one instance of
``None`` in Python (all references to ``None`` point to the same object), and
``None`` is only identical to itself:

.. code-block:: python

   >>> MyType = type(None)
   >>> MyType() is None
   True

:class:`None` is falsy
----------------------

In Python, we often rely on the fact that :class:`None` is falsy:

.. code-block:: python

   >>> bool(None)
   False

For example, we can check whether :doc:`../types/strings` are empty in an
:doc:`if statement <../control-flows/if-elif-else>`:

.. code-block:: python

   >>> myval = ""
   >>> if not myval:
   ...     print("No value was specified.")
   ...
   No value was specified.

:class:`None` stands for emptiness
----------------------------------

.. code-block:: python

   >>> titles = {7.0: "Data Types", 7.1: "Lists", 7.2: "Tuples"}
   >>> third_title = titles.get("7.3")
   >>> print(third_title)
   None

The default return value of a function is :class:`None`
-------------------------------------------------------

For example, a procedure in Python is just a function that does not explicitly
return a value, which means that it returns ``None`` by default:

.. code-block:: python

   >>> def myfunc():
   ...     pass
   ...
   >>> print(myfunc())
   None
