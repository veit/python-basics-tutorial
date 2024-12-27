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

Special characters and escape sequences
---------------------------------------

``\n`` stands for the newline character and ``\t`` for the tab character.
Character sequences that begin with a backslash and are used to represent other
characters are called escape sequences. Escape sequences are generally used to
represent special characters, in other words, characters for which there is no
single-character printable representation.

Here are other characters you can get with the escape character:

+--------------------------+--------------------------+--------------------------+
| Escape sequence          | Output                   | Description              |
+==========================+==========================+==========================+
| ``\\``                   | ``\``                    | Backslash                |
+--------------------------+--------------------------+--------------------------+
| ``\'``                   | ``'``                    | single quote character   |
+--------------------------+--------------------------+--------------------------+
| ``\"``                   | ``"``                    | double quote character   |
+--------------------------+--------------------------+--------------------------+
| ``\b``                   |                          | Backspace (``BS``)       |
+--------------------------+--------------------------+--------------------------+
| ``\n``                   |                          | ASCII Linefeed ``(LF``)  |
+--------------------------+--------------------------+--------------------------+
| ``\r``                   |                          | ASCII Carriage Return    |
|                          |                          | (``CR``)                 |
+--------------------------+--------------------------+--------------------------+
| ``\t``                   |                          | Tabulator (``TAB``)      |
+--------------------------+--------------------------+--------------------------+
| :samp:`\u{00B5}`         | ``µ``                    | Unicode 16 bit           |
+--------------------------+--------------------------+--------------------------+
| :samp:`\U{000000B5}`     | ``µ``                    | Unicode 32 bit           |
+--------------------------+--------------------------+--------------------------+
| :samp:`\N{{SNAKE}}`      | ``🐍``                   | Unicode Emoji name       |
+--------------------------+--------------------------+--------------------------+

Lines 1–7
    The ASCII character set, which is used by Python and is the standard
    character set on almost all computers, defines a whole range of other
    special characters.
Lines 8–9
    Unicode escape sequences.
Line 10
    Unicode names for specifying a Unicode character.

Operators and functions
-----------------------

The operators and functions that work with character strings return new
character strings derived from the original. The operators (``in``, ``+`` and
``*``) and built-in functions (``len``, ``max`` and ``min``) work with character
strings in the same way as with lists and tuples.

.. code-block:: pycon

   >>> welcome = "Hello pythonistas!\n"
   >>> 2 * welcome
   'Hello pythonistas!\nHello pythonistas!\n'
   >>> welcome + welcome
   'Hello pythonistas!\nHello pythonistas!\n'
   >>> "python" in welcome
   True
   >>> max(welcome)
   'y'
   >>> min(welcome)
   '\n'

Indexing and slicing
--------------------

The index and slice notation works in the same way to obtain individual elements
or slices:

.. code-block:: pycon

   >>> welcome[0:5]
   'Hello'
   >>> welcome[6:-1]
   'pythonistas!'

However, the index and slice notation cannot be used to add, remove or replace
elements, as character strings are immutable:

.. code-block:: pycon

   >>> welcome[6:-1] = "everybody!"
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

String methods
--------------

Most of the Python :ref:`string methods <python3:string-methods>` are integrated
in the :ref:`str <python3:textseq>` type so that all ``str`` objects
automatically have them:

.. code-block:: pycon

   >>> welcome = "hello pythonistas!\n"
   >>> welcome.isupper()
   False
   >>> welcome.isalpha()
   False
   >>> welcome[0:5].isalpha()
   True
   >>> welcome.capitalize()
   'Hello pythonistas!\n'
   >>> welcome.title()
   'Hello Pythonistas!\n'
   >>> welcome.strip()
   'Hello pythonistas!'
   >>> welcome.split(" ")
   ['hello', 'pythonistas!\n']
   >>> chunks = [snippet.strip() for snippet in welcome.split(" ")]
   >>> chunks
   ['hello', 'pythonistas!']
   >>> " ".join(chunks)
   'hello pythonistas!'
   >>> welcome.replace("\n", "")
   'hello pythonistas!'

Below you will find an overview of the most common :ref:`string methods
<python3:string-methods>`:

+-----------------------------------+---------------------------------------------------------------+
| Method                            | Description                                                   |
+===================================+===============================================================+
| :py:meth:`str.count`              | returns the number of non-overlapping occurrences of the      |
|                                   | string.                                                       |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.endswith`           | returns ``True`` if the string ends with the suffix.          |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.startswith`         | returns ``True`` if the string starts with the prefix.        |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.join`               | uses the string as a delimiter for concatenating a sequence   |
|                                   | of other strings.                                             |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.index`              | returns the position of the first character in the string if  |
|                                   | it was found in the string; triggers a ``ValueError`` if it   |
|                                   | was not found.                                                |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.find`               | returns the position of the first character of the first      |
|                                   | occurrence of the substring in the string; like ``index``,    |
|                                   | but returns ``-1`` if nothing was found.                      |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.rfind`              | Returns the position of the first character of the last       |
|                                   | occurrence of the substring in the string; returns ``-1`` if  |
|                                   | nothing was found.                                            |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.replace`            | replaces occurrences of a string with another string.         |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.strip`,             | strip spaces, including line breaks.                          |
| :py:meth:`str.rstrip`,            |                                                               |
| :py:meth:`str.lstrip`             |                                                               |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.split`              | splits a string into a list of substrings using the passed    |
|                                   | separator.                                                    |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.lower`              | converts alphabetic characters to lower case.                 |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.upper`              | converts alphabetic characters to upper case.                 |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.casefold`           | converts characters to lower case and converts all            |
|                                   | region-specific variable character combinations to a common   |
|                                   | comparable form.                                              |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.ljust`,             | left-aligned or right-aligned; fills the opposite side of the |
| :py:meth:`str.rjust`              | string with spaces (or another filler character) in order to  |
|                                   | obtain a character string with a minimum width.               |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.removeprefix`       | In Python 3.9 this can be used to extract the suffix or file  |
| :py:meth:`str.removesuffix`       | name.                                                         |
+-----------------------------------+---------------------------------------------------------------+

``str.split`` and ``str.join``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While :meth:`python3:str.split` returns a list of strings,
:meth:`python3:str.join` takes a list of strings and joins them into a single
string. Normally :meth:`python3:str.split` uses whitespace as a delimiter for
the strings to be split, but you can change this behaviour with an optional
:doc:`parameter <../../functions/params>`.

.. warning::
   Concatenating strings with ``+`` is useful but not efficient when it comes to
   joining a large number of strings into a single string, as a new string
   object is created each time ``+`` is applied.  :samp:`"Hello" +
   "Pythonistas!"` creates two objects, of which one is immediately discarded.

If you join strings with :meth:`python3:str.join`, you can insert any characters
between the strings:

.. code-block:: pycon

   >>> " :: ".join(["License", "OSI Approved"])
   'License :: OSI Approved'

You can also use an empty string,  ``""``, for example for the CamelCase
notation of Python classes:

.. code-block:: pycon

   >>> "".join(["My", "Class"])
   'MyClass'

:meth:`python3:str.split` is mostly used to split strings at spaces. However,
you can also split a string at a specific other string by passing an optional
:doc:`parameter <../../functions/params>`:

.. code-block:: pycon

   >>> example = "1. You can have\n\twhitespaces, newlines\n   and tabs mixed in\n\tthe string."
   >>> example.split()
   ['1.', 'You', 'can', 'have', 'whitespaces,', 'newlines', 'and', 'tabs', 'mixed', 'in', 'the', 'string.']
   >>> license = "License :: OSI Approved"
   >>> license.split(" :: ")
   ['License', 'OSI Approved']

Sometimes it is useful to allow the last field in a string to contain arbitrary
text. You can do this by specifying an optional second :doc:`parameter
<../../functions/params>` for how many splits should be performed:

.. code-block:: pycon

   >>> example.split(" ", 1)
   ['1.', 'You can have\n\twhitespaces, newlines\n   and tabs mixed in\n\tthe string.']

If you want to use :meth:`python3:str.split` with the optional second argument,
you must first specify a first argument. To ensure that all spaces are split,
use :doc:`../none` as the first argument:

.. code-block:: pycon

   >>> example.split(None, 8)
   ['1.', 'You', 'can', 'have', 'whitespaces,', 'newlines', 'and', 'tabs', 'mixed in\n\tthe string.']

.. tip::
   I use :meth:`python3:str.split` and :meth:`python3:str.join` extensively,
   mostly for text files generated by other programmes. For writing
   :doc:`Python4DataScience:data-processing/serialisation-formats/csv/index` or
   :doc:`Python4DataScience:data-processing/serialisation-formats/json/index`
   files, however, I usually use the associated Python libraries.

Remove whitespace
~~~~~~~~~~~~~~~~~

:py:meth:`str.strip` returns a new string that differs from the original string
only in that all spaces at the beginning or end of the string have been removed.
:py:meth:`str.lstrip` and :py:meth:`str.rstrip` work similarly, but only remove
the spaces at the left or right end of the original string:

.. code-block:: pycon

   >>> example = "    whitespaces, newlines \n\tand tabs. \n"
   >>> example.strip()
   'whitespaces, newlines \n\tand tabs.'
   >>> example.lstrip()
   'whitespaces, newlines \n\tand tabs. \n'
   >>> example.rstrip()
   '    whitespaces, newlines \n\tand tabs.'

In this example, the newlines ``\n`` are regarded as whitespace. The exact
assignment may differ from operating system to operating system. You can find
out what Python considers to be whitespace by accessing the constant
:py:data:`string.whitespace`. For me, the following is returned:

.. code-block:: pycon

   >>> import string
   >>> string.whitespace
   ' \t\n\r\x0b\x0c'

The characters specified in hexadecimal format (``\x0b``, ``\x0c``) represent
the vertical tab and feed characters.

.. tip::
   Do not change the value of these variables to influence the functionality of
   :py:meth:`str.strip` :abbr:`etc (et cetera)`. You can pass characters as
   additional :doc:`parameters <../../functions/params>` to determine which
   characters these methods remove:

   .. code-block:: pycon

      >>> url = "https://www.cusy.io/"
      >>> url.strip("htps:/w.")
      'cusy.io'

Search in strings
~~~~~~~~~~~~~~~~~

:ref:`str <python3:textseq>` offer several methods for a simple search for
character strings: The four basic methods for searching strings are
:py:meth:`str.find`, :py:meth:`str.rfind`, :py:meth:`str.index` and
:py:meth:`str.rindex`. A related method, :py:meth:`str.count`, counts how many
times a string can be found in another string.

:py:meth:`str.find` requires a single :doc:`parameter <../../functions/params>`:
the substring being searched for; the position of the first occurrence is then
returned, or ``-1`` if there is no occurrence:

.. code-block:: pycon

   >>> hipy = "Hello Pythonistas!\n"
   >>> hipy.find("\n")
   18

:py:meth:`str.find`  can also accept one or two additional :doc:`parameters
<../../functions/params>`:

``start``
    The number of characters at the beginning of the string to be searched that
    should be ignored.
``end``
    The Number of characters at the end of the string to be searched that should
    be ignored.

In contrast to :py:meth:`find`, :py:meth:`rfind` starts the search at the end of
the string and therefore returns the position of the last occurrence.

:py:meth:`index` and :py:meth:`rindex` differ from :py:meth:`find` and
:py:meth:`rfind` in that a :class:`python3:ValueError` exception is triggered
instead of the return value ``-1``.

You can use two other :ref:`string methods <python3:string-methods>` to search
for strings: :py:meth:`str.startswith` and :py:meth:`str.endswith`. These
methods return ``True``- or ``False``, depending on whether the string to which
they are applied starts or ends with one of the strings specified as
:doc:`parameters <../../functions/params>`:

.. code-block:: pycon

   >>> hipy.endswith("\n")
   True
   >>> hipy.endswith(("\n", "\r"))
   True

There are also several methods that can be used to check the property of a
character string:

+---------------------------+---------------+---------------+---------------+---------------+---------------+
| Method                    | ``[!#$%…]``   | ``[a-zA-Z]``  | ``[¼½¾]``     | ``[¹²³]``     | ``[0-9]``     |
+===========================+===============+===============+===============+===============+===============+
| :py:meth:`str.isprintable`| ✅            | ✅            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isalnum`    | ❌            | ✅            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isnumeric`  | ❌            | ❌            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isdigit`    | ❌            | ❌            | ❌            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isdecimal`  | ❌            | ❌            | ❌            | ❌            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+

:py:meth:`str.isspace` checks for spaces.

Changing strings
~~~~~~~~~~~~~~~~

:ref:`str <python3:textseq>` are immutable, but they have several methods that
can return a modified version of the original string.

:py:meth:`str.replace` can be used to replace occurrences of the first
 :doc:`parameter <../../functions/params>` with the second, for example:

.. code-block:: pycon

   >>> hipy.replace("\n", "\n\r")
   'Hello Pythonistas!\n\r'

:py:meth:`str.maketrans` and :py:meth:`str.translate` can be used together to
translate characters in strings into other characters, for example:

.. code-block:: pycon
   :linenos:

   >>> hipy = "Hello Pythonistas!\n"
   >>> trans_map = hipy.maketrans(" ", "-", "!\n")
   >>> hipy.translate(trans_map)
   'Hello-Pythonistas'

Line 2
    :py:meth:`str.maketrans` is used to create a translation table from the two
    string arguments. The two arguments must each contain the same number of
    characters. Characters that are not to be returned are passed as the third
    argument.
Line 3
    The table generated by :py:meth:`str.maketrans` is passed to
    :py:meth:`str.translate`.

``re``
------

The Python standard library  :doc:`re <python3:library/re>` also contains
functions for working with character strings. However, ``re`` offers more
sophisticated options for pattern extraction and replacement than the :ref:`str
<python3:textseq>` type.

.. code-block:: pycon

   >>> import re
   >>> re.sub("\n", "", welcome)
   'Hello pythonistas!'

Here, the regular expression is first compiled and then its
:py:meth:`re.Pattern.sub` method is called for the passed text. You can compile
the expression itself with :py:func:`re.compile` to create a reusable regex
object that reduces CPU cycles when applied to different strings:

.. code-block:: pycon

   >>> regex = re.compile("\n")
   >>> regex.sub("", welcome)
   'Hello pythonistas!'

If you want to get a list of all patterns that match the ``regex`` object
instead, you can use the :py:meth:`re.Pattern.findall` method:

.. code-block:: pycon

   >>> regex.findall(welcome)
   ['\n']

.. note::
   To avoid the awkward escaping with ``\`` in a regular expression, you can use
   raw string literals such as ``r'C:\PATH\TO\FILE'`` instead of the
   corresponding ``'C:\\PATH\\TO\\FILE'``.

:py:meth:`re.Pattern.match` and :py:meth:`re.Pattern.search` are closely related
to :py:meth:`re.Pattern.findall`. While ``findall`` returns all matches in a
string, ``search`` only returns the first match and ``match`` only returns
matches at the beginning of the string. As a less trivial example, consider a
block of text and a regular expression that can identify most email addresses:

.. code-block:: pycon

   >>> addresses = """Veit <veit@cusy.io>
   ... Veit Schiele <veit.schiele@cusy.io>
   ... cusy GmbH <info@cusy.io>
   ... """
   >>> pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
   >>> regex = re.compile(pattern, flags=re.IGNORECASE)
   >>> regex.findall(addresses)
   ['veit@cusy.io', 'veit.schiele@cusy.io', 'info@cusy.io']
   >>> regex.search(addresses)
   <re.Match object; span=(6, 18), match='veit@cusy.io'>
   >>> print(regex.match(addresses))
   None

``regex.match`` returns ``None``, as the pattern only matches if it is at the
beginning of the string.

Suppose you want to find email addresses and at the same time split each address
into its three components:

#. personal name
#. domain name
#. domain suffix

To do this, you first place round brackets ``()`` around the parts of the
pattern to be segmented:

.. code-block:: pycon

   >>> pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
   >>> regex = re.compile(pattern, flags=re.IGNORECASE)
   >>> match = regex.match("veit@cusy.io")
   >>> match.groups()
   ('veit', 'cusy', 'io')

:py:meth:`re.Match.groups` returns a :doc:`../sequences-sets/tuples` containing
all subgroups of the match.

:py:meth:`re.Pattern.findall` returns a list of tuples if the pattern contains
groups:

.. code-block:: pycon

   >>> regex.findall(addresses)
   [('veit', 'cusy', 'io'), ('veit.schiele', 'cusy', 'io'), ('info', 'cusy', 'io')]

Groups can also be used in :py:meth:`re.Pattern.sub` where ``\1`` stands for the
first matching group, ``\2`` for the second and so on:

.. code-block:: pycon

   >>> regex.findall(addresses)
   [('veit', 'cusy', 'io'), ('veit.schiele', 'cusy', 'io'), ('info', 'cusy', 'io')]
   >>> print(regex.sub(r"Username: \1, Domain: \2, Suffix: \3", addresses))
   Veit <Username: veit, Domain: cusy, Suffix: io>
   Veit Schiele <Username: veit.schiele, Domain: cusy, Suffix: io>
   cusy GmbH <Username: info, Domain: cusy, Suffix: io>

The following table contains a brief overview of methods for regular
expressions:

+-----------------------+-------------------------------------------------------------------------------+
| Method                | Description                                                                   |
+=======================+===============================================================================+
| :py:func:`re.findall` | returns all non-overlapping matching patterns in a string as a list.          |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.finditer`| like ``findall``, but returns an iterator.                                    |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.match`   | matches the pattern at the beginning of the string and optionally segments    |
|                       | the pattern components into groups; if the pattern matches, a ``match``       |
|                       | object is returned, otherwise none.                                           |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.search`  | searches the string for matches to the pattern; in this case, returns a       |
|                       | ``match`` object; unlike ``match``, the match can be anywhere in the string   |
|                       | and not just at the beginning.                                                |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.split`   | splits the string into parts each time the pattern occurs.                    |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.sub`,    | replaces all (``sub``) or the first ``n`` occurrences (``subn``) of the       |
| :py:func:`re.subn`    | pattern in the string with a replacement expression; uses the symbols ``\1``, |
|                       | ``\2``, … to refer to the elements of the match group.                        |
+-----------------------+-------------------------------------------------------------------------------+

.. seealso::
   * :doc:`regex`
   * :doc:`python3:howto/regex`
   * :doc:`python3:library/re`

.. toctree::
   :titlesonly:
   :hidden:

   regex

Converting character strings into numbers
-----------------------------------------

You can use the :class:`python3:int` and :class:`python3:float` functions to
convert character strings into integer or floating point numbers. If a character
string is passed that cannot be interpreted as a number of the specified type,
these functions trigger a :class:`python3:ValueError` exception. Exceptions are
explained in more detail in :doc:`control flows
<../../control-flows/exceptions>`. You can also pass :class:`python3:int` an
optional second :doc:`parameter  <../../functions/params>` that specifies the
numerical base to be used when interpreting the string:

.. code-block:: pycon
   :linenos:

   >>> float("12.34")
   12.34
   >>> float("12e3")
   12000.0
   >>> int("1000")
   1000
   >>> int("1000", base=10)
   1000
   >>> int("1000", 8)
   512
   >>> int("1000", 2)
   8
   >>> int("1234", 2)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: invalid literal for int() with base 2: '1234'

Lines 5–8
    If no second :doc:`parameter <../../functions/params>` is specified,
    :class:`python3:int` calculates with a base of ``10``.
Lines 9, 10
    ``1000`` is interpreted as an `octal number
    <https://en.wikipedia.org/wiki/Octal>`_.
Lines 11, 12
    ``1000`` is interpreted as a `binary number
    <https://en.wikipedia.org/wiki/Binary_number>`_.
Lines 13–16
    ``1234`` cannot be specified as an integer on base ``2``. A
    :class:`python3:ValueError` exception is therefore triggered.

Changing character strings with list manipulations
--------------------------------------------------

Since :ref:`str <python3:textseq>` objects are immutable, there is no way to
change them directly like :doc:`lists <../sequences-sets/lists>`. However, you
can convert them into lists:

.. code-block:: pycon

   >>> palindromes = "lol level gag"
   >>> palindromes_list = list(palindromes)
   >>> palindromes_list.reverse()
   >>> "".join(palindromes_list)
   'gag level lol'

Converting objects into strings
-------------------------------

In Python, almost anything can be converted into a string using the built-in
:ref:`str <python3:textseq>` function:

.. code-block:: pycon

   >>> data_types = [(7, "Data types", 19), (7.1, "Numbers", 19), (7.2, "Lists", 23)]
   >>> (
   ...     "The title of chapter "
   ...     + str(data_types[0][0])
   ...     + " is «"
   ...     + data_types[0][1]
   ...     + "»."
   ... )
   'The title of chapter 7 is «Data types».'

The example uses :ref:`str <python3:textseq>` to convert an integer from the
``data_types`` list into a string, which is then concatenated again to form the
final string.

.. note::
   While :ref:`str <python3:textseq>` is mostly used to generate human readable
   text, :func:`python3:repr` is more commonly used for debugging output or
   status reports, for example to get information about the built-in Python
   function :func:`python3:len`:

   .. code-block:: pycon

      >>> repr(len)
      '<built-in function len>'

``print()``
-----------

The function :func:`print` outputs character strings, whereby other Python data
types can easily be converted into strings and formatted, for example:

.. code-block:: pycon

   >>> import math
   >>> pi = math.pi
   >>> d = 28
   >>> u = pi * d
   >>> print(
   ...     "Pi is",
   ...     pi,
   ...     "and the circumference with a diameter of",
   ...     d,
   ...     "inches is",
   ...     u,
   ...     "inches.",
   ... )
   Pi is 3.141592653589793 and the circumference with a diameter of 28 inches is 87.96459430051421 inches.

F-Strings
~~~~~~~~~

F-strings can be used to shorten numbers that are too detailed for a text:

.. code-block:: pycon

    >>> print(f"The value of Pi is {pi:.3f}.")
    The value of Pi is 3.142.

In ``{pi:.3f}``, the format specification ``f`` is used to truncate the number
Pi to three decimal places.

In A/B test scenarios, you often want to display the percentage change in a key
figure. F strings can be used to formulate them in an understandable way:

.. code-block:: pycon

   >>> metrics = 0.814172
   >>> print(f"The AUC has increased to {metrics:=+7.2%}")
   The AUC has increased to +81.42%

In this example, the variable ``metrics`` is formatted with ``=`` taking over
the contents of the variable after the ``+``, displaying a total of seven
characters including the plus or minus sign, ``metrics`` and the percent sign.
``.2`` provides two decimal places, while the ``%`` symbol converts the decimal
value into a percentage. For example, ``0.514172`` is converted to ``+51.42%``.

Values can also be converted into binary and hexadecimal values:

.. code-block:: pycon

   >>> block_size = 192
   >>> print(f"Binary block size: {block_size:b}")
   Binary block size: 11000000
   >>> print(f"Hex block size: {block_size:x}")
   Hex block size: c0

There are also formatting specifications that are ideally suited for :abbr:`CLI
(Command Line Interface)` output, for example:

.. code-block:: pycon

   >>> data_types = [(7, "Data types", 19), (7.1, "Numbers", 19), (7.2, "Lists", 23)]
   >>> for n, title, page in data_types:
   ...     print(f"{n:.1f} {title:.<25} {page: >3}")
   ...
   7.0 Data types...............  19
   7.1 Numbers..................  19
   7.2 Lists....................  23

In general, the format is as follows, whereby all information in square brackets
is optional:

:samp:`:[[FILL]ALIGN][SIGN][0b|0o|0x|d|n][0][WIDTH][GROUPING]["." PRECISION][TYPE]`

The following table lists the fields for character string formatting and their
meaning:

+-----------------------+-------------------------------------------------------+
| Field                 | Meaning                                               |
+=======================+=======================================================+
| :samp:`FILL`          | Character used to fill in :samp:`ALIGN`. The default  |
|                       | value is a space.                                     |
+-----------------------+-------------------------------------------------------+
| :samp:`ALIGN`         | Text alignment and fill character:                    |
|                       |                                                       |
|                       | | ``<``: left-aligned                                 |
|                       | | ``>``: right-aligned                                |
|                       | | ``^``: centred                                      |
|                       | | ``=``: Fill character after :samp:`SIGN`            |
+-----------------------+-------------------------------------------------------+
| :samp:`SIGN`          | Display sign:                                         |
|                       |                                                       |
|                       | | ``+``: Display sign for positive and negative       |
|                       |    numbers                                            |
|                       | | ``-``: Default value, ``-`` only for negative       |
|                       |   numbers or space for positive                       |
+-----------------------+-------------------------------------------------------+
| :samp:`0b|0o|0x|d|n`  | Sign for integers:                                    |
|                       |                                                       |
|                       | | ``0b``: Binary numbers                              |
|                       | | ``0o``: Octal numbers                               |
|                       | | ``0x``: Hexadecimal numbers                         |
|                       | | ``d``: Default value, decimal integer with base 10  |
|                       | | ``n``: uses the current ``locale`` setting to       |
|                       |   insert the corresponding number separators          |
+-----------------------+-------------------------------------------------------+
| :samp:`0`             | fills with zeros                                      |
+-----------------------+-------------------------------------------------------+
| :samp:`WIDTH`         | Minimum field width                                   |
+-----------------------+-------------------------------------------------------+
| :samp:`GROUPING`      | Number separator: [#]_                                |
|                       |                                                       |
|                       | | ``,``: comma as thousands separator                 |
|                       | | ``_``: underscore for thousands separator           |
+-----------------------+-------------------------------------------------------+
| :samp:`.PRECISION`    | | For floating point numbers, the number of digits    |
|                       |   after the point                                     |
|                       | | For non-numeric values, the maximum length          |
+-----------------------+-------------------------------------------------------+
| :samp:`TYPE`          | Output format as number type or string                |
|                       |                                                       |
|                       | … for integers:                                       |
|                       |                                                       |
|                       | | ``b``: binary format                                |
|                       | | ``c``: converts the integer to the corresponding    |
|                       |   Unicode character                                   |
|                       | | ``d``: default value, decimal character             |
|                       | | ``n``: same as ``d``, th the difference that it     |
|                       |   uses the current ``locale`` setting to insert the   |
|                       |   corresponding number separators                     |
|                       | | ``o``: octal format                                 |
|                       | | ``x``: Hexadecimal format in base 16, using         |
|                       |   lowercase letters for the digits above 9            |
|                       | | ``X``: Hexadecimal format based on 16, using        |
|                       |   capital letters for digits above 9                  |
|                       |                                                       |
|                       | … for floating point numbers:                         |
|                       |                                                       |
|                       | | ``e``: Exponent with ``e`` as separator between     |
|                       |   coefficient and exponent                            |
|                       | | ``E``: Exponent with ``E`` as separator between     |
|                       |   coefficient and exponent                            |
|                       | | ``g``: Standard value for floating point numbers,   |
|                       |   whereby the exponent has a fixed width for large    |
|                       |   and small numbers                                   |
|                       | | ``G``: Like ``g``, but changes to ``E`` if the      |
|                       |   number becomes too large. The representations       |
|                       |   of infinity and NaN are also written in capital     |
|                       |   letters                                             |
|                       | | ``n``: Like ``g`` with the difference that it uses  |
|                       |   the current ``locale`` setting to insert the        |
|                       |   corresponding number separators                     |
|                       | | ``%``: Percentage. Multiplies the number by 100     |
|                       |   and displays it in the fixed format ``f`` followed  |
|                       |   by a percent sign                                   |
+-----------------------+-------------------------------------------------------+

.. [#] The format identifier ``n`` formats a number in a locally customised way,
    for example:

    .. code-block:: pycon

       >>> value = 635372
       >>> import locale
       >>> locale.setlocale(locale.LC_NUMERIC, "en_US.utf-8")
       'en_US.utf-8'
       >>> print(f"{value:n}")
       635,372

.. tip::
   A good source for F-strings is the help function:

   .. code-block:: pycon

      >>> help()
      help> FORMATTING
      ...

   You can browse through the help here and find many examples.

   You can exit the help function again with :kbd:`:`–:kbd:`q` and :kbd:`⏎`.

.. seealso::
   * `PyFormat <https://pyformat.info>`_
   * :ref:`python3:f-strings`
   * :pep:`498`

Debugging F-Strings
:::::::::::::::::::

In Python 3.8, a specifier was introduced to help with debugging F-string
variables. By adding an equals sign ``=``, the code is included within the
F-string:

.. code-block:: pycon

   >>> uid = "veit"
   >>> print(f"My name is {uid.capitalize()=}")
   My name is uid.capitalize()='Veit'

Formatting date and time formats and IP addresses
:::::::::::::::::::::::::::::::::::::::::::::::::

:py:mod:`datetime` supports the formatting of strings using the same syntax as
the :py:meth:`strftime <datetime.datetime.strftime>` method for these objects.

.. code-block:: pycon

   >>> import datetime
   >>> today = datetime.date.today()
   >>> print(f"Today is {today:%d %B %Y}.")
   Today is 26 November 2023.

The :py:mod:`ipaddress` module of Python also supports the formatting of
``IPv4Address`` and ``IPv6Address`` objects.

Finally, third-party libraries can also add their own support for formatting
strings by adding a ``__format__`` method to their objects.

.. seealso::
   * :ref:`format-codes`
   * `Python strftime cheatsheet <https://strftime.org>`_

Built-in modules for strings
----------------------------

The Python standard library contains a number of built-in modules that you can
use to manage strings:

.. _string-modules:

+-----------------------+-------------------------------------------------------------------------------+
| Module                | Description                                                                   |
+=======================+===============================================================================+
| :py:mod:`string`      | compares with constants such as :py:data:`string.digits` or                   |
|                       | :py:data:`string.whitespace`                                                  |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`re`          | searches and replaces text with regular expressions                           |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`struct`      | interprets bytes as packed binary data                                        |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`difflib`     | helps to calculate deltas, find differences between strings or sequences and  |
|                       | create patches and diff files                                                 |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`textwrap`    | wraps and fills text, formats text with line breaks or spaces                 |
+-----------------------+-------------------------------------------------------------------------------+

.. _end-string-modules:

.. seealso::
   * :doc:`Manipulation of strings with pandas
     <Python4DataScience:workspace/pandas/string-manipulation>`
   * `humanize <https://humanize.readthedocs.io/en/stable/>`_

.. toctree::
   :titlesonly:
   :hidden:

   encodings

Checks
------

* For example, can you add or multiply a string with an integer, a floating
  point number or a complex number?


* How can you change a heading such as ``variables and expressions`` so that it
  contains hyphens instead of spaces and can therefore be better used as a file
  name?

* Which of the following strings cannot be converted into numbers and why?

 * ``int("1e2")``
 * ``int(1e+2)``
 * ``int("1+2")``
 * ``int("+2")``

* If you want to check whether a line begins with ``.. note::``, which method
  would you use? Are there any other options?

* Suppose you have a string with exclamation marks, quotation marks and line
  breaks. How can these be removed from the string?

* How can you change all spaces and punctuation marks from a string to a hyphen
  (``-``)?

* What use cases can you imagine in which the :mod:`python3:struct` module would
  be useful for reading or writing binary data?

  * when reading and writing a binary file
  * when reading from an external interface, where the data should be stored
    exactly as it was transmitted

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

* Which regular expression would you use to find hexadecimal values?
