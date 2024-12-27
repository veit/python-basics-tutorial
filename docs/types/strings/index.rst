Strings
=======

The processing of character strings is one of Python’s strengths. There are many
options for limiting character strings:

.. code-block:: python

   "A string in double quotes can contain 'single quotes'."
   'A string in single quotes can contain "double quotes"'
   """\tA string that starts with a tab and ends with a newline character.\n"""
   """This is a string in triple double quotes, the only string that contains
   real line breaks."""

Character strings can be characterised by single (``' '``), double(``" "``),
triple single (``''' '''``) or triple double (``""" """``) quotation marks.

A normal character string cannot be split over several lines. The following code
will therefore not work:

.. code-block::

   "This is an incorrect attempt to insert a newline into a string without
   using \n."

They can also contain tab (``\t``) and newline characters (``\n``). In general,
backslashes ``\`` can be used as escape characters. For example ``\\`` can be used for a single backslash and ``\'`` for a single quote character, whereby it
does not end the string:

.. blacken-docs:off

.. code-block:: python

   "You don't need a backslash here."
   'However, this wouldn\'t work without a backslash.'

.. blacken-docs:on

However, Python also offers character strings in triple quotation marks
(``"""``), which make this possible and can contain single and double quotation
marks without backslashes ``\`` as escape characters.

.. toctree::
   :titlesonly:
   :hidden:

   encodings
   operators-functions
   built-in-modules/index
   print
   input

Checks
------

* What use cases can you imagine in which the :mod:`python3:struct` module would
  be useful for reading or writing binary data?

  * when reading and writing a binary file
  * when reading from an external interface, where the data should be stored
    exactly as it was transmitted

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

* Which regular expression would you use to find hexadecimal values?
