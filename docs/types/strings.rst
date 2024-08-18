Strings
=======

The processing of character strings is one of Python’s strengths. There are many
options for delimiting character strings:

.. code-block:: python

   "A string in double quotes can contain 'single quotes'."
   'A string in single quotes can contain "double quotes"'
   """\tA string that starts with a tab and ends with a newline character.\n"""
   """This is a string in triple double quotes, the only string that contains
   real line breaks."""

Strings can be separated by single (``' '``), double (``" "``), triple single
(``''' '''``) or triple double (``""" """``) quotes and can contain tab (``\t``)
and newline (``\n``) characters. In general, backslashes ``\`` can be used as
escape characters. For example  ``\\`` can be used for a single backslash and
``\'`` for a single quote, whereby it does not end the string:

.. blacken-docs:off

.. code-block:: python

   "You don't need a backslash here."
   'However, this wouldn\'t work without a backslash.'

.. blacken-docs:on

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

A normal string cannot be split into multiple lines. The following code will not
work:

.. code-block::

   "This is an incorrect attempt to insert a newline into a string without
   using \n."

However, Python provides strings in triple quotes (``"""``) that allow this and
can contain single and double quotes without backslashes.

Strings are also immutable. The operators and functions that work with them
return new strings derived from the original. The operators (``in``, ``+`` and
``*``) and built-in functions (``len``, ``max`` and ``min``) work with strings
in the same way as with lists and tuples.

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

The index and slice notation works in the same way to obtain elements or slices:

.. code-block:: pycon

   >>> welcome[0:5]
   'Hello'
   >>> welcome[6:-1]
   'pythonistas!'

However, the index and slice notation cannot be used to add, remove or replace
elements:

.. code-block:: pycon

   >>> welcome[6:-1] = "everybody!"
   raceback (most recent call last):
    File "<stdin>", line 1, in <module>
   ypeError: 'str' object does not support item assignment

``string``
----------

For strings, the standard Python library :doc:`string <python3:library/string>`
contains several methods for working with their content, including
:py:meth:`str.split`, :py:meth:`str.replace` and :py:meth:`str.strip`:

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

In addition, there are several methods with which the property of a character
string can be checked:

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

:py:meth:`str.isspace` checks for spaces:
``[ \t\n\r\f\v\x1c-\x1f\x85\xa0\u1680…]``.

``re``
------

The Python standard library :doc:`re <python3:library/re>` also contains
functions for working with strings. However, ``re`` offers more sophisticated
options for pattern extraction and replacement than ``string``.

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
to :py:meth:`re.Pattern.findall`. While findall returns all matches in a string,
``search`` only returns the first match and ``match`` only returns matches at
the beginning of the string. As a less trivial example, consider a block of text
and a regular expression that can identify most email addresses:

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

:py:meth:`re.Match.groups` returns a :doc:`tuples` that contains all subgroups
of the match.

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
   * :doc:`../../appendix/regex`
   * :doc:`python3:howto/regex`
   * :doc:`python3:library/re`

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

.. seealso::
   * :doc:`Manipulation of strings with pandas
     <Python4DataScience:workspace/pandas/string-manipulation>`

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

* Suppose you have a string with punctuation marks, inverted commas and line
  breaks. How can these be removed from the string?

* What use cases can you imagine in which the :mod:`python3:struct` module would
  be useful for reading or writing binary data?

  * when reading and writing a binary file
  * when reading from an external interface, where the data should be stored
    exactly as it was transmitted

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

* Which regular expression would you use to find hexadecimal values?
