Unicode and character encodings
===============================

There are dozens of character encodings. For an overview of Python's encodings,
see :ref:`python3:encodings-overview`.

The ``string`` module
---------------------

Python’s :doc:`string <python3:library/string>` module distinguishes the
following string constants, all of which fall into the ASCII character set:

.. code-block:: python

    # Some strings for ctype-style character classification
    whitespace = ' \t\n\r\v\f'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = '0123456789'
    hexdigits = digits + 'abcdef' + 'ABCDEF'
    octdigits = '01234567'
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    printable = digits + ascii_letters + punctuation + whitespace

Most of these constants should be self-explanatory in their identifier names.
``hexdigits`` and ``octdigits`` refer to the hexadecimal and octal values
respectively. You can use these constants for everyday string manipulation:

.. code-block:: python

    >>> import string
    >>> hepy = "Hello Pythonistas!"
    >>> hepy.rstrip(string.punctuation)
    'Hello Pythonistas'

However, the :doc:`string <python3:library/string>` module works with Unicode by
default, which is represented as binary data (bytes).

Unicode
-------

It is obvious that the ASCII character set is not nearly large enough to cover
all languages, dialects, symbols and glyphs; it is not even large enough for
English.

While ASCII is a complete subset of Unicode – the first 128 characters in the
Unicode table correspond exactly to ASCII characters – Unicode encompasses a
much larger set of characters. Unicode itself is not an encoding but is
implemented by various character encodings, with UTF-8 probably being the most
commonly used encoding scheme.

.. note::
   The Python help documentation has an entry for Unicode: enter ``help()`` and
   then ``UNICODE``. The various options for creating Python strings are
   described in detail.

.. seealso::
    * :ref:`python3:unicode-howto`
    * `What’s New In Python 3.0: Text Vs. Data Instead Of Unicode Vs. 8-bit
      <https://docs.python.org/3/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit>`_

Unicode and UTF-8
~~~~~~~~~~~~~~~~~

While Unicode is an abstract encoding standard, UTF-8 is a concrete encoding
scheme. The Unicode standard is a mapping of characters to code points and
defines several different encodings from a single character set. UTF-8 is an
encoding scheme for representing Unicode characters as binary data with one or
more bytes per character.

Encoding and decoding in Python 3
---------------------------------

The :ref:`str <python3:textseq>` type is intended for the representation of
human-readable text and can contain all Unicode characters. The :ref:`bytes
<python3:typebytes>` type, on the other hand, represents binary data that is not
inherently encoded. :meth:`python3:str.encode` and :meth:`python3:bytes.decode`
are the methods of transition from one to the other:

.. code-block:: python

    >>> "You’re welcome!".encode("utf-8")
    b'You\xe2\x80\x99re welcome!'
    >>> b"You\xe2\x80\x99re welcome!".decode("utf-8")
    'You’re welcome!'

The result of ``str.encode()`` is a :ref:`bytes <python3:typebytes>` object.
Both byte literals (such as ``b'You\xe2\x80\x99re welcome!'``) and
representations of bytes only allow ASCII characters. For this reason, when
calling ``"You’re welcome!".encode("utf-8")``, the ASCII-compatible ``'You'``
may be represented as it is, but the `’ <https://unicode-table.com/en/2019/>`_
becomes ``'\xe2\x80\x99'``. This chaotic looking sequence represents three
bytes, ``e2``, ``80`` and ``99`` as hexadecimal values.

.. tip::
    In ``.encode()`` and ``.decode()``, the encoding parameter is ``"utf-8"`` by
    default; however, it is recommended to specify it explicitly.

With :meth:`python3:bytes.fromhex` you can convert the hexadecimal values into
bytes:

.. code-block:: python

    >>> bytes.fromhex('e2 80 99')
    b'\xe2\x80\x99'

UTF-16 and UTF-32
~~~~~~~~~~~~~~~~~

The difference between these and UTF-8 is considerable in practice. In the
following, I would like to show you only briefly by means of an example that a
round-trip conversion can simply fail here:

.. code-block:: python

    >>> hepy = "Hello Pythonistas!"
    >>> hepy.encode("utf-8")
    b'Hello Pythonistas!'
    >>> len(hepy.encode("utf-8"))
    18
    >>> hepy.encode("utf-8").decode("utf-16")
    '效汬\u206f祐桴湯獩慴ⅳ'
    >>> len(hepy.encode("utf-8").decode("utf-16"))
    9

Encoding Latin letters in UTF-8 and then decoding them in UTF-16 resulted in a
text that also contains characters from the Chinese, Japanese or Korean language
areas as well as Roman numerals. Decoding the same byte object can lead to
results that are not even in the same language or contain the same number of
characters.

Python 3 and Unicode
--------------------

Python 3 relies fully on Unicode and specifically on UTF-8:

* Python 3 source code is assumed to be UTF-8 by default.
* Texts (:ref:`str <python3:textseq>`) are Unicode by default. Encoded Unicode
  text is represented as binary data (:ref:`Bytes <python3:typebytes>`)
  dargestellt.
* Python 3 accepts many Unicode code points in :ref:`identifiers <identifiers>`.
* Python’s :doc:`re module <python3:library/re>` uses the ``re.UNICODE`` flag by
  default, not ``re.ASCII``. This means that, for example, ``r"\w"`` matches
  Unicode word characters, not just ASCII letters.
* The default encoding in ``str.encode()`` and ``bytes.decode()`` is UTF-8.

The only exception could be :func:`open() <python3:open>`, which is platform
dependent and therefore depends on the value of
:func:`python3:locale.getpreferredencoding`:

.. code-block:: python

    >>> import locale
    >>> locale.getpreferredencoding()
    'UTF-8'

Built-in Python Functions
-------------------------

Python has a number of built-in functions that relate to character encodings in
some way:

:func:`python3:ascii`, :func:`python3:bin`, :func:`python3:hex`, :func:`python3:oct`
    output a string.
:class:`python3:bytes`, :class:`python3:str`, :class:`python3:int`
    are class constructors for their respective types, converting the input to
    the desired type.
:func:`python3:ord`, :func:`python3:chr`
    are inverses of each other in that the Python function ``ord()`` converts an
    ``str`` character to its ``base=10`` code point, while ``chr()`` does the
    opposite.

Below is a more detailed look at each of these nine functions:

+-----------------------+---------------+---------------------------------------+
| Function              | RReturn type  | Description                           |
+=======================+===============+=======================================+
| :func:`python3:ascii` | ``str``       | ASCII representation of an object,    |
|                       |               | escaping non-ASCII characters.        |
+-----------------------+---------------+---------------------------------------+
| :func:`python3:bin`   | ``str``       | binary representation of an integer   |
|                       |               | with the prefix ``0b``                |
+-----------------------+---------------+---------------------------------------+
| :func:`python3:hex`   | ``str``       | hexadecimal representation of an      |
|                       |               | integer with the prefix ``0x``        |
+-----------------------+---------------+---------------------------------------+
| :func:`python3:oct`   | ``str``       | octal representation of an integer    |
|                       |               | with the prefix ``0o``                |
+-----------------------+---------------+---------------------------------------+
| :class:`python3:bytes`| ``bytes``     | converts the input to                 |
|                       |               | :ref:`bytes type <python3:typebytes>` |
+-----------------------+---------------+---------------------------------------+
| :class:`python3:str`  | ``str``       | converts the input to                 |
|                       |               | :ref:`str type <python3:textseq>`     |
+-----------------------+---------------+---------------------------------------+
| :class:`python3:int`  | ``int``       | converts the input to                 |
|                       |               | :class:`int type <python3:int>`       |
+-----------------------+---------------+---------------------------------------+
| :func:`python3:ord`   | ``int``       | converts a single Unicode character   |
|                       |               | to its integer code point             |
+-----------------------+---------------+---------------------------------------+
| :func:`python3:chr`   | ``str``       | converts an integer code point into a |
|                       |               | single Unicode character              |
+-----------------------+---------------+---------------------------------------+
