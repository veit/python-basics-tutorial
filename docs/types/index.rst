Data types
==========

Python has several built-in data types, from scalars such as numbers and boolean
values to more complex structures such as sequences, sets, dictionaries and
strings.

+-----------------------+-----------------------------------------------+
| Data type             | Examples                                      |
+=======================+===============================================+
| Numeric types         | :class:`int`, :class:`float`, :class:`complex`|
+-----------------------+-----------------------------------------------+
| Boolean type          | :class:`bool`                                 |
+-----------------------+-----------------------------------------------+
| Sequences             | :class:`list`, :class:`tuple`                 |
+-----------------------+-----------------------------------------------+
| Sets                  | :class:`set`, :class:`frozenset`              |
+-----------------------+-----------------------------------------------+
| Mappings              | :class:`dict`                                 |
+-----------------------+-----------------------------------------------+
| Strings               | :class:`str`                                  |
+-----------------------+-----------------------------------------------+
| Files                 | :func:`open <open>`                           |
+-----------------------+-----------------------------------------------+

These data types can be manipulated using language operators, built-in
functions, library functions or a data type’s own methods.

You can also define your own classes and create your own class instances. For
these class instances, you can define methods as well as manipulate them using
the language operators and built-in functions for which you have defined the
appropriate special method attributes.

.. note::
   In the Python documentation and in this book, the term *object* is used for
   instances of any Python data type, not just what many other languages would
   call class instances. This is because all Python objects are instances of one
   class or another.

Python has several built-in data types, from scalars like numbers and boolean
values to more complex structures like lists, dictionaries and files.

.. toctree::
   :titlesonly:
   :hidden:

   numbers/index
   sequences-sets/index
   dicts
   strings/index
   none
