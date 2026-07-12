Files and Directories
=====================

:mod:`python3:pathlib` implements path operations using
:class:`python3:pathlib.PurePath` and :class:`python3:pathlib.Path` objects. The
:mod:`python3:os` and :mod:`python3:os.path` modules, on the other hand, provide
functions that work at a low level with ``str`` and ``bytes``, which is more in
line with a procedural approach. We consider :mod:`python3:pathlib`’s
object-oriented style to be more readable and will therefore cover it in greater
detail here.

.. seealso::
   * :pep:`428`: The pathlib module – object-oriented filesystem paths
   * :ref:`os-comparison`
   * `Why you should be using pathlib <https://treyhunner.com/2018/12/why-you-should-be-using-pathlib>`_
   * `No really, pathlib is great <https://treyhunner.com/2019/01/no-really-pathlib-is-great>`_

Reading and Writing Files
-------------------------

In Python, you can open and read a file using the :class:`python3:pathlib.Path`
class and various built-in read operations:

:meth:`python3:pathlib.Path.read_text`
    returns the decoded contents of the file pointed to by the pointer as a
    string.
:meth:`python3:pathlib.Path.write_text`
    opens the specified file in text mode, writes to it and then closes the
    file. An existing file with the same name will be overwritten.

.. note::
   You do not need to use a :doc:`with <../control-flow/with>` statement, as the
   file is already opened using a context manager.

.. tip::
   However, when opening, reading and writing a file, you should always specify
   the character encoding explicitly, as Python versions prior to 3.15 will
   otherwise select a platform-dependent default encoding. An incorrect encoding
   can, however, trigger an :doc:`exception <../control-flow/exceptions>` or
   result in garbled text:

.. code-block:: pycon
   :linenos:

   >>> from pathlib import Path
   >>> p = Path("docs", "save-data", "python.txt")
   >>> p.write_text("🐍", encoding="utf-8")
   1
   >>> p.read_text(encoding="cp1252")
   Traceback (most recent call last):
     File "<python-input-3>", line 1, in <module>
       p.read_text(encoding="cp1252")
       ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
     File "/Users/veit/Library/Application Support/uv/python/cpython-3.14.6-macos-aarch64-none/lib/python3.14/pathlib/__init__.py", line 788, in read_text
       return f.read()
              ~~~~~~^^
     File "/Users/veit/Library/Application Support/uv/python/cpython-3.14.6-macos-aarch64-none/lib/python3.14/encodings/cp1252.py", line 23, in decode
       return codecs.charmap_decode(input,self.errors,decoding_table)[0]
              ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2: character maps to <undefined>

Line 2:
    The arguments passed to :class:`python3:pathlib.Path` are path segments,
    either as :class:`PosixPath <pathlib.PosixPath>` or :class:`WindowsPath
    <pathlib.WindowsPath>`. In the previous example, you open a file that you
    assume is located at :file:`docs/save-data/python.txt`, relative to where
    you are calling the function.

    The following example specifies an absolute path –
    :file:`C:\\Users\\Veit\\My Documents\\python.txt`:

    .. code-block:: pycon
       :lineno-start: 2

       >>> p = Path("C:/", "Users", "Veit", "My Documents", "python.txt")

We can suppress this exception using the ``errors`` argument. The default value
for ``errors`` is ``strict``, which causes an exception to be raised.

Any faulty byte can be replaced with the corresponding Unicode replacement
character (``U+FFFD``, �):

.. code-block:: pycon

   >>> p.read_text(encoding="cp1252", errors="replace")
   'ðŸ��'

.. version-added:: 3.15
   From Python 3.15 onwards, UTF-8 is used by default everywhere. Only once
   support for Python 3.14 and earlier versions is discontinued will specifying
   the ``encoding`` for UTF-8 files become optional.

Alternatively, errors can also be ignored:

.. code-block:: pycon

   >>> p.read_text(encoding="cp1252", errors="ignore")
   'ðŸ'

Or you can replace the bytes with an escape character:

.. code-block:: pycon

   >>> p.read_text(encoding="cp1252", errors="backslashreplace")
   'ðŸ\\x90\\x8d'

The pure numerical byte value is specified by the hexadecimal digits following
``\\x``.

.. note::
   The ``errors`` argument is only useful if decoding fails. Reading a file with
   the wrong encoding **can** raise a ``UnicodeDecodeError``. However, it can
   also simply result in garbled text without any error message if decoding with
   the wrong encoding appears to succeed, meaning that seemingly valid
   characters are displayed instead of an exception being raised. The ``errors``
   argument cannot fix garbled text.

If you prefer to use `open()` – whether with a :doc:`context manager
<../control-flow/with>` or otherwise – you can use the :meth:`pathlib.Path.open`
method of your :class:`pathlib.Path` object instead:

.. code-block:: pycon
   :linenos:

   >>> with p.open(encoding="utf-8") as f:
   ...     f.readline()
   ...
   '🐍'

Line 1:
    :meth:`python3:pathlib.Path.open` does not read anything from the file, but
    returns a file object that you can use to access the opened file. It keeps
    track of a file and how much of it has been read or written. All file
    operations in Python are carried out using file objects rather than file
    names.

Line 2:
    The first call to :meth:`readline() <codecs.StreamReader.readline>` returns
    the first line of the file object, that is, everything up to and including
    the first line break, or the entire file if there is no line break in the
    file; the next call to :func:`readline` returns the second line, if it
    exists, and so on. When there is nothing left to read, :meth:`readline()
    <codecs.StreamReader.readline>` returns an empty string.

This behaviour of :meth:`readline() <codecs.StreamReader.readline>` makes it
easy, for example, to determine the number of lines in a file:

.. code-block:: pycon

   >>> with p.open(encoding="utf-8") as f:
   ...     lc = 0
   ...     while f.readline() != "":
   ...         lc = lc + 1
   ...     print(lc)
   ...
   1

A quicker way to count all the lines is to use the built-in :meth:`readlines()
<codecs.StreamReader.readlines>` method, which reads all the lines of a file and
returns them as a list of strings, with one string per line:

.. code-block:: pycon

   >>> with p.open(encoding="utf-8") as f:
   ...     print(len(f.readlines()))
   ...
   1

However, if you are counting all the lines in a large file, this method may
cause the buffer to overflow, as the entire file is read in one go. It is also
possible for the buffer to overflow when using :meth:`readline()
<codecs.StreamReader.readline>` if you attempt to read a line from a large file
that contains no line-break characters. To better handle such situations, both
methods have an optional argument that controls the amount of data read at any
one time. Another way to iterate through all the lines of a file is to treat the
file object as an iterator within a :ref:`for-loop`:

.. code-block:: pycon

   >>> with p.open(encoding="utf-8") as f:
   ...     lc = 0
   ...     for l in f:
   ...         lc = lc + 1
   ...     print(lc)
   ...
   1

The advantage of this method is that the lines are read into memory as and when
required, so there is no risk of running out of memory, even with large files.
Another advantage of this method is that it is simpler and easier to read.

However, a potential problem with the read method can arise when working on
Windows and macOS in text mode, if you use the :func:`open` command in text
mode, meaning without appending a ``b``. In text mode, macOS converts every
``\r`` to ``\n``, whilst Windows converts ``\r\n`` pairs to ``\n``. You can
specify how line breaks are handled by using the newline parameter when opening
the file and setting ``newline="\n"``, ``\r`` or ``\r\n``, which ensures that
only that character sequence is used as a line break:

.. code-block:: pycon

   >>> with p.open(encoding="utf-8", newline="\r\n") as f:
   ...     lc = 0
   ...

In this example, only ``\n`` is treated as a line break. However, if the file is
opened in binary mode, the ``encoding`` and ``newline`` arguments are
meaningless, as all bytes are returned exactly as they appear in the file:

.. code-block:: pycon

   >>> with p.open(mode="rb") as f:
   ...     print(len(f.readlines()))
   ...
   1

Reading directories
-------------------

:meth:`python3:pathlib.Path.iterdir`
    If the path points to a directory, the path objects representing the
    directory’s contents are returned:

    .. code-block:: pycon

       >>> p = Path("docs", "save-data")
       >>> for child in p.iterdir():
       ...     child
       ...
       PosixPath('docs/save-data/index.rst')
       PosixPath('docs/save-data/minidom_example.py')
       PosixPath('docs/save-data/pickle.rst')
       PosixPath('docs/save-data/xml.rst')
       PosixPath('docs/save-data/books.xml')
       PosixPath('docs/save-data/files.rst')

The child objects are returned in any order, and the special entries ``.`` and
``..`` are not included. If the path is not a directory or is otherwise
inaccessible, an :exc:`python3:OSError` is raised.

:meth:`python3:pathlib.Path.glob`
    finds the specified relative pattern in the directory represented by this
    path and returns all matching files:

    .. code-block:: pycon

       >>> sorted(p.glob("*.rst"))
       [PosixPath('docs/save-data/files.rst'), PosixPath('docs/save-data/index.rst'), PosixPath('docs/save-data/pickle.rst'), PosixPath('docs/save-data/xml.rst')]

    .. seealso::
       :ref:`python3:pathlib-pattern-language`

:meth:`python3:pathlib.Path.rglob`
    recursively matches the specified relative pattern. This is equivalent to
    calling the function with ``**/`` before the pattern.

:meth:`python3:pathlib.Path.walk`
    generates the filenames within a directory structure by traversing the
    structure either top-down or bottom-up. It returns a 3-tuple consisting of
    (``dirpath, dirnames, filenames``).

    With the default setting for the optional argument ``top_down=True``, the
    tuple for a directory is generated before the tuples for its subdirectories.

    When ``follow_symlinks=True``, symlinks are resolved and placed in
    ``dirnames`` and ``filenames`` according to their targets.

    The following example displays the sizes of the files in a directory,
    ignoring  :file:`__pycache__` directories:

    .. code-block:: pycon

       >>> for root, dirs, files in p.walk():
       ...     print(
       ...         root,
       ...         "consumes",
       ...         sum((root / file).stat().st_size for file in files),
       ...         "bytes in",
       ...         len(files),
       ...         "non-directory files",
       ...     )
       ...     if "__pycache__" in dirs:
       ...         dirs.remove("__pycache__")
       ...
       docs/save-data consumes 88417 bytes in 13 non-directory files
       docs/save-data/sqlite consumes 35187 bytes in 19 non-directory files

    The next example is a simple implementation of
    :func:`python3:shutil.rmtree`, whereby the directory tree must be traversed
    from the bottom up, as :meth:`python3:pathlib.Path.rmdir` only allows a
    directory to be deleted once it is empty:

    .. code-block:: pycon

       >>> for root, dirs, files in p.walk(top_down=False):
       ...     for name in files:
       ...         (root / name).unlink()
       ...     for name in dirs:
       ...         (root / name).rmdir()
       ...

Creating files and directories
------------------------------

:meth:`python3:pathlib.Path.touch`
    creates a file at the specified path. The ``mode`` parameter can be used to
    specify the file mode and access flags. If the file already exists, the
    modification time is updated to the current time provided that
    ``exist_ok=True``; otherwise, a :class:`python3:FileExistsError` is raised.

    .. note::
      :meth:`python3:pathlib.Path.open` or :meth:`pathlib.Path.write_text` are
      also frequently used to create files.

:meth:`python3:pathlib.Path.mkdir`
    creates a new directory at the specified path. The parameters ``mode`` and
    ``exist_ok`` function as described in :meth:`python3:pathlib.Path.touch`.

    If ``parents=True``, any missing parent directories in the path are created
    as required with the default permissions. With the default setting of
    ``parents=False``, however, a :class:`python3:FileNotFoundError` is raised.

Move, Copy and Delete
---------------------

:meth:`python3:pathlib.Path.rename`
    renames the file or directory to the specified destination and returns a new
    :class:`python3:pathlib.Path` instance that points to the destination. On
    Unix, provided the destination exists and is a file, it is simply
    overwritten; on Windows, :class:`python3:FileExistsError` is raised.

    .. code-block:: pycon

       >>> myfile = Path("docs", "save-data", "myfile.txt")
       >>> newfile = Path("docs", "newdir", "newfile.txt")
       >>> myfile.rename(newfile)
       PosixPath('docs/newdir/newfile.txt')

.. version-added:: 3.14
   Python 3.14 introduces the methods :meth:`pathlib.Path.copy`,
   :meth:`pathlib.Path.copy_into`, :meth:`pathlib.Path.move` and
   :meth:`pathlib.Path.move_into`.

   .. seealso::
      `Python 3.14 Changelog
      <https://docs.python.org/3.14/whatsnew/3.14.html#pathlib>`_

Permissions and Ownership
-------------------------

:meth:`python3:pathlib.Path.owner`
    returns the name of the person who owns the file. By default, symbolic links
    are followed; however, if you wish to determine who owns the symbolic link,
    add ``follow_symlinks=False``. If the user ID (UID) of the file cannot be
    found, a :class:`python3:KeyError` is raised.

:meth:`python3:pathlib.Path.group`
    returns the name of the group that owns the file. The behaviour with regard
    to symbolic links is the same as that of :meth:`python3:pathlib.Path.owner`.
    If the group ID (GID) of the file cannot be found, a
    :class:`python3:KeyError` is also raised.

:meth:`python3:pathlib.Path.chmod`
    changes the file mode and permissions. By default, it follows symbolic
    links. To change the permissions of symbolic links, you can use
    ``follow_symlinks=False`` or :meth:`python3:pathlib.Path.lchmod`.

.. _os-comparison:

Comparison with ``os`` and ``os.path``
--------------------------------------

* :mod:`pathlib` implements objects with :class:`pathlib.PurePath` and
  :class:`pathlib.Path`, while :mod:`os` and :mod:`os.path` work more
  procedurally with low-level ``str`` and ``bytes``.
* Many functions in :mod:`os` and :mod:`os.path` support paths relative to
  directory descriptors. These functions are not available in :mod:`pathlib`.
* ``str`` and ``bytes``, as well as parts of :mod:`python3:os-os` and
  :mod:`python3:os.path`, are written in C and are very fast. :mod:`pathlib`, on
  the other hand, is written in Python and is often slower, but this does not
  always matter.

Despite the differences, many os functions can be translated into corresponding
:class:`python3:pathlib.Path` or :class:`python3:pathlib.PurePath` functions:

=====================================   ==============================================================
:mod:`os`                               :mod:`pathlib`
=====================================   ==============================================================
:func:`os.chmod`                        :meth:`pathlib.Path.chmod`
:func:`os.lstat`                        :meth:`pathlib.Path.lstat`
:func:`os.listdir`                      :meth:`pathlib.Path.iterdir`
:func:`os.getcwd`                       :meth:`pathlib.Path.cwd`
:func:`os.lchmod`                       :meth:`pathlib.Path.lchmod`
:func:`os.link`                         :meth:`pathlib.Path.hardlink_to`
:func:`os.mkdir`, :func:`os.makedirs`   :meth:`pathlib.Path.mkdir`
:func:`os.path.abspath`                 :meth:`pathlib.Path.absolute`
:func:`os.path.basename`                :attr:`pathlib.PurePath.name`
:func:`os.path.dirname`                 :attr:`pathlib.PurePath.parent`
:func:`os.path.exists`                  :meth:`pathlib.Path.exists`
:func:`os.path.expanduser`              :meth:`pathlib.Path.expanduser`
:func:`os.path.isabs`                   :meth:`pathlib.PurePath.is_absolute`
:func:`os.path.isdir`                   :meth:`pathlib.Path.is_dir`
:func:`os.path.isfile`                  :meth:`pathlib.Path.is_file`
:func:`os.path.isjunction`              :meth:`pathlib.Path.is_junction`
:func:`os.path.islink`                  :meth:`pathlib.Path.is_symlink`
:func:`os.path.ismount`                 :meth:`pathlib.Path.is_mount`
:func:`os.path.join`                    :meth:`pathlib.PurePath.joinpath`
:func:`os.path.realpath`                :meth:`pathlib.Path.resolve`
:func:`os.path.relpath`                 :meth:`pathlib.PurePath.relative_to`
:func:`os.path.samefile`                :meth:`pathlib.Path.samefile`
:func:`os.path.splitext`                :attr:`pathlib.PurePath.stem`, :attr:`pathlib.PurePath.suffix`
:func:`os.readlink`                     :meth:`pathlib.Path.readlink`
:func:`os.remove`, :func:`os.unlink`    :meth:`pathlib.Path.unlink`
:func:`os.rename`                       :meth:`pathlib.Path.rename`
:func:`os.replace`                      :meth:`pathlib.Path.replace`
:func:`os.rmdir`                        :meth:`pathlib.Path.rmdir`
:func:`os.stat`                         :meth:`pathlib.Path.stat`
:func:`os.symlink`                      :meth:`pathlib.Path.symlink_to`
:func:`os.walk`                         :meth:`pathlib.Path.walk`
=====================================   ==============================================================

Checks
------

* Uses the functions of the  :mod:`python3:pathlib` module to take a path to a
  file named :file:`example.log` and create a new file path in the same
  directory for a file named :file:`example.log1`.

* Open a file :file:`my_file.txt` and insert additional text at the end of the
  file. Which command would you use to open :file:`my_file.txt`? Which command
  would you use to reopen the file and read it from the beginning?

* If you look at the `man page for the wc utility
  <https://linux.die.net/man/1/wc>`_, you will see two command line options:

  ``-c``
      counts the bytes in the file
  ``-m``
      counts the characters, which in the case of some Unicode characters can be
      two or more bytes long

  Also, if a file is specified, our module should read from and process that
  file, but if no file is specified, it should read from and process ``stdin``.

* If a context manager is used in a script that reads and/or writes multiple
  files, which of the following approaches do you think would be best?

  #. Put the entire script in a block managed by a ``with`` statement.
  #. Use one ``with`` statement for all reads and another for all writes.
  #. Use a ``with`` statement every time you read or write a file, that is, for
     every line.
  #. Use a ``with`` statement for each file you read or write.

* Archive :file:`*.txt` files from the current directory in the :file:`archive`
  directory as :file:`*.zip` files with the current date as the file name.

  * Which modules do you need for this?
  * Write a possible solution.
