Strings
=======

The processing of character strings is one of Python’s strengths. There are many
options for limiting character strings:

.. blacken-docs:off

.. code-block:: python

   "A string in double quotes can contain 'single quotes'."
   'A string in single quotes can contain "double quotes"'
   """\tA string that starts with a tab and ends with a newline character.\n"""
   """This is a string in triple double quotes, the only string that contains
   real line breaks."""

.. blacken-docs:on

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

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

* Which regular expression would you use to find hexadecimal values?
