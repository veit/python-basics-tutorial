``re``
======

The Python standard library :doc:`re <python3:library/re>` also contains
functions for working with character strings. However, ``re`` offers more
sophisticated options for pattern extraction and replacement than the
:ref:`str <python3:textseq>` type.

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

:py:meth:`re.Match.groups` returns a :doc:`../../sequences-sets/tuples`
containing all subgroups of the match.

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

Checks
------

* Which regular expression would you use to find strings that represent the
  numbers between -3 and +3?

* Which regular expression would you use to find hexadecimal values?
