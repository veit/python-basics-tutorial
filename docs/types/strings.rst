Strings
=======

String processing is one of Python’s strengths. There are many options for
delimiting strings:

.. code-block:: python

    "A string in double quotes can contain 'single quotes'."
    'A string enclosed in single quotes may contain "double quotes".'
    '''\tA string that begins with a tab and ends with a newline character.\n'''
    """This is a string of characters in triple double quotes, the
    only string that contains true newlines."""

Strings can be separated by single i(``' '``), double (``" "``), triple single
(``''' '''``) or triple double (``""" """``) quotes and can contain tab (``\t``)
and newline (``\n``) characters. In general, backslashes ``\`` can be used as
escape characters. For example, ``\\`` can be used for a single backslash and
``\"`` can be used for a single quote, making it not terminate the string:

.. code-block:: python

    "You don't need a backslash here."
    'However, this wouldn\'t work without a backslash.'

A normal string cannot be split across multiple lines. The following code will
not work:

.. code-block::

    "This is an erroneous attempt to insert a newline in
    a string without using \n."

However, Python provides strings in triple quotes (``"""``) that allow this and
can contain single and double quotes without backslashes.

Strings are also immutable. The operators and functions that work with them
return new strings derived from the original. The operators (``in``, ``+`` and
``*``) and built-in functions (``len``, ``max`` and ``min``) work with strings
in the same way as with lists and tuples.

.. code-block:: python

    >>> welcome = "Hello pythonistas!\n"
    >>> 2 * welcome
    'Hello pythonistas!\nHello pythonistas!\n'
    >>> welcome + welcome
    'Hello pythonistas!\nHello pythonistas!\n'
    >>> 'python' in welcome
    True
    >>> max(welcome)
    'y'
    >>> min(welcome)
    '\n'

Index and slice notation work in the same way to get elements or slices:

.. code-block:: python

    >>> welcome[0:5]
    'Hello'
    >>> welcome[6:-1]
    'pythonistas!'

However, index and slice notation cannot be used to add, remove or replace
elements:

.. code-block:: python

    >>> welcome[6:-1] = 'everybody!'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

``string``
----------

For strings, there are several methods in the standard Python library
:doc:`string <python3:library/string>` to work with their content, including
:py:meth:`str.split`, :py:meth:`str.replace` and :py:meth:`str.strip`:

.. code-block:: python

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
    >>> welcome.split(' ')
    ['hello', 'pythonistas!\n']
    >>> chunks = [snippet.strip() for snippet in welcome.split(' ')]
    >>> chunks
    ['hello', 'pythonistas!']
    >>> ' '.join(chunks)
    'hello pythonistas!'
    >>> welcome.replace('\n', '')
    'hello pythonistas!'

The following is an overview of the most common :ref:`string methods
<python3:string-methods>`:

+---------------------------+---------------------------------------------------------------+
| Method                    | Description                                                   |
+===========================+===============================================================+
| :py:meth:`str.count`      | returns the number of non-overlapping occurrences of the      |
|                           | string.                                                       |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.endswith`   | returns ``True`` if the string ends with the suffix.          |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.startswith` | returns ``True`` if the string starts with the prefix.        |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.join`       | uses the string as a delimiter for concatenating a sequence   |
|                           | of other strings.                                             |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.index`      | returns the position of the first character in the string if  |
|                           | it is found in the string; raises a R``ValueError`` Rif it is |
|                           | Rnot found.                                                   |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.find`       | returns the position of the first character of the first      |
|                           | occurrence of the substring in the string; like ``index``,    |
|                           | but returns ``-1`` if nothing was found.                      |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.rfind`      | returns the position of the first character of the last       |
|                           | occurrence of the substring in the string; returns ``-1`` if  |
|                           | nothing was found.                                            |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.replace`    | replaces occurrences of a string with another string.         |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.strip`,     | trim spaces, including line breaks.                           |
| :py:meth:`str.rstrip`,    |                                                               |
| :py:meth:`str.lstrip`     |                                                               |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.split`      | splits a string into a list of substrings using the passed    |
|                           | separator.                                                    |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.lower`      | converts alphabetic characters to lower case.                 |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.upper`      | converts alphabetic characters to upper case.                 |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.casefold`   | converts characters to lower case and converts all            |
|                           | region-specific variable character combinations to a common   |
|                           | comparable form.                                              |
+---------------------------+---------------------------------------------------------------+
| :py:meth:`str.ljust`,     | left-justified or right-justified; fills the opposite side of |
| :py:meth:`str.rjust`      | the string with spaces (or another fill character) to obtain  |
|                           | a string with a minimum width.                                |
+---------------------------+---------------------------------------------------------------+

In addition, there are some methods that can be used to check the property of a
string:

+-------------------+---------------+---------------+---------------+---------------+---------------+
| Method            | ``[!#$%…]``   | ``[a-zA-Z]``  | ``[¼½¾]``     | ``[¹²³]``     | ``[0-9]``     |
+===================+===============+===============+===============+===============+===============+
| ``isprintable()`` | ✅            | ✅            | ✅            | ✅            | ✅            |
+-------------------+---------------+---------------+---------------+---------------+---------------+
| ``isalnum()``     | ❌            | ✅            | ✅            | ✅            | ✅            |
+-------------------+---------------+---------------+---------------+---------------+---------------+
| ``isnumeric()``   | ❌            | ❌            | ✅            | ✅            | ✅            |
+-------------------+---------------+---------------+---------------+---------------+---------------+
| ``isdigit()``     | ❌            | ❌            | ❌            | ✅            | ✅            |
+-------------------+---------------+---------------+---------------+---------------+---------------+
| ``isdecimal()``   | ❌            | ❌            | ❌            | ❌            | ✅            |
+-------------------+---------------+---------------+---------------+---------------+---------------+

``re``
------

The Python standard library :doc:`re <python3:library/re>` also contains
functions for working with strings. Here, ``re`` offers more sophisticated
possibilities for pattern extraction and substitution than ``string``.

.. code-block:: python

    >>> import re
    >>> re.sub('\n', '', welcome)
    'Hello pythonistas!'

Here, the regular expression is first compiled and then its
:py:meth:`re.Pattern.sub` method is called for the passed text. You can compile
the aud expression itself with :py:func:`re.compile` to form a reusable regex
object that reduces CPU cycles when applied to different strings:

.. code-block:: python

    >>> regex = re.compile('\n')
    >>> regex.sub('', welcome)
    'Hello pythonistas!'

If instead you want to get a list of all patterns that match the ``regex``
object, you can use the :py:meth:`re.Pattern.findall` method:

.. code-block:: python

    >>> regex.findall(welcome)
    ['\n']

.. note::
   To avoid the awkward escaping with ``\`` in a regular expression, you can use
   raw string literals like ``r'C:\PATH\TO\FILE'`` instead of the corresponding
   ``'C:\\PATH\\TO\\FILE'``.

:py:meth:`re.Pattern.match` and :py:meth:`re.Pattern.search` are closely related
to :py:meth:`re.Pattern.findall`. While ``findall`` returns all matches in a
string, ``search`` returns only the first match and ``match`` returns only
matches at the beginning of the string. As a less trivial example, consider a
block of text and a regular expression that can identify most email addresses:

.. code-block:: python

    >>> addresses = """Veit <veit@cusy.io>
    ... Veit Schiele <veit.schiele@cusy.io>
    ... cusy GmbH <info@cusy.io>
    ... """
    >>> pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
    >>> regex = re.compile(pattern, flags=re.IGNORECASE)
    >>> regex.findall(addresses)
    ['veit@cusy.io', 'veit.schiele@cusy.io', 'info@cusy.io']
    >>> regex.search(addresses)
    <re.Match object; span=(6, 18), match='veit@cusy.io'>
    >>> print(regex.match(addresses))
    None

``regex.match`` returns ``None`` because the pattern only matches if it is at
the beginning of the string.

Suppose you want to find email addresses and at the same time split each address
into its three components:

#. Person name
#. Domain name
#. Domain suffix

To do this, you first put round brackets ``()`` around the parts of the pattern
to be segmented:

.. code-block:: python

    >>> pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
    >>> regex = re.compile(pattern, flags=re.IGNORECASE)
    >>> match = regex.match('veit@cusy.io')
    >>> match.groups()
    ('veit', 'cusy', 'io')

:py:meth:`re.Match.groups` returns a tuple containing all subgroups of the
match.

:py:meth:`re.Pattern.findall` returns a list of tuples if the pattern contains
groups:

.. code-block:: python

    >>> regex.findall(addresses)
    [('veit', 'cusy', 'io'), ('veit.schiele', 'cusy', 'io'), ('info', 'cusy', 'io')]

Groups can also be used in where ``\1`` stands for the first matching group,
``\2`` for the second and so on:

.. code-block:: python

    >>> regex.findall(addresses)
    [('veit', 'cusy', 'io'), ('veit.schiele', 'cusy', 'io'), ('info', 'cusy', 'io')]
    >>> print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', addresses))
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
|                       | ``match`` object; unlike ``match``, the match can be anywhere in the string,  |
|                       | not just at the beginning.                                                    |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.split`   | splits the string into parts each time the pattern occurs.                    |
+-----------------------+-------------------------------------------------------------------------------+
| :py:func:`re.sub`,    | replaces all (``sub``) or the first ``n`` occurences (``subn``) of the        |
| :py:func:`re.subn`    | pattern in the string with a replacement expression; uses the symbols ``\1``, |
|                       | ``\2``, …, to refer to the elements of the match group.                       |
+-----------------------+-------------------------------------------------------------------------------+

.. seealso::
   * :doc:`../appendix/regex`
   * :doc:`python3:howto/regex`
   * :doc:`python3:library/re`

``print()``
-----------

The function :func:`print` outputs strings whereby other Python data types can
easily be converted into strings and formatted, for example:

.. code-block:: python

    >>> import math
    >>> pi = math.pi
    >>> d = 28
    >>> u = pi * d
    >>> print("Pi is", pi, "and the circumference at a diameter of", d, "inches is", u, "inches.")
    Pi is 3.141592653589793 and the circumference at a diameter of 28 nches is 87.96459430051421 inches.
    >>> print(f"The value of Pi is {pi:.3f}.")
    The value of Pi is 3.142.

Objects are automatically converted to strings for printing, with string
literals prefixed with ``f`` providing additional formatting options.

However, the index and slice notation cannot be used to add, remove or replace elements:

In ``{pi:.3f}``, the format specification ``f`` is used to limit the number Pi
to three decimal places. For more information on the format specificationeb see
`Format Specification Mini-Language
<https://docs.python.org/3/library/string.html#format-specification-mini-language>`_.

.. seealso::
   * :ref:`python3:f-strings`
   * `PEP 498 – Literal String Interpolation
     <https://peps.python.org/pep-0498/>`_

Built-in modules for strings
----------------------------

The Python standard library contains a number of built-in modules that you can
use to manage strings:

.. _string-modules:

+-----------------------+-------------------------------------------------------------------------------+
| Module                | Description                                                                   |
+=======================+===============================================================================+
| :py:mod:`string`      | compares with constants like  :py:data:`string.digits` or                     |
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
