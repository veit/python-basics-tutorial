Files and directories
=====================

:mod:`python3:pathlib` implements path operations using
:class:`python3:pathlib.PurePath` and :class:`python3:pathlib.Path` objects. The
:mod:`python3:os`  and :mod:`python3:os.path` modules, on the other hand, offer
functions that work at a low level with ``str``- and ``bytes`` which is more in
line with a procedural approach. We consider the object-oriented style of
:mod:`python3:pathlib`  be more readable and therefore present it in more detail
here.

.. seealso::
   * :pep:`428`: The pathlib module – object-oriented filesystem paths
   * :ref:`os-comparison`
   * `Why you should be using pathlib <https://treyhunner.com/2018/12/why-you-should-be-using-pathlib>`_
   * `No really, pathlib is great <https://treyhunner.com/2019/01/no-really-pathlib-is-great>`_

Reading and writing files
-------------------------

In Python, you open and read a file by using the
:meth:`python3:pathlib.Path.open` function and various built-in read operations.
:meth:`python3:pathlib.Path.open` opens the file to which the path refers, as
the built-in :func:`python3:open` function does. The following short Python
programme reads a line from a text file named :file:`myfile.txt` in
:file:`docs/save-data/`:

.. code-block:: pycon
   :linenos:

   >>> from pathlib import Path
   >>> p = Path("docs", "save-data", "myfile.txt")
   >>> f = p.open()
   >>> headline = f.readline()

Line 2:
    The arguments of :class:`python3:pathlib.Path` are path segments, either as
    :class:`PosixPath <pathlib.PosixPath>` or :class:`WindowsPath
    <pathlib.WindowsPath>`. In the previous example, you open a file that you
    assume is located relative to your call in
    :file:`docs/save-data/myfile.txt`.

    The following example opens a file at an absolute location –
    :file:`C:\\My Documents\\myfile.txt`:

    .. code-block:: pycon
       :lineno-start: 2

       >>> p = Path("C:/", "Users", "Veit", "My Documents", "myfile.txt")
       >>> with p.open() as f:
       ...     f.readline()
       ...

    .. note::
       In this example, the keyword ``with`` is used, which means that the file
       is opened with a context manager, as explained in more detail in
       :doc:`/control-flow/with`. This way of opening files handles potential
       I/O errors better and should generally be preferred.

Line 3:
    :meth:`python3:pathlib.Path.open` does not read anything from the file, but
    returns a file object that you can use to access the opened file. It keeps
    track of a file and how much of the file has been read or written. All file
    operations in Python are performed with file objects, not file names.

Line 4:
    The first call to :meth:`readline() <codecs.StreamReader.readline>` returns
    the first line of the file object, that is, everything up to and including
    the first line break, or the entire file if there is no line break in the
    file; the next call to :func:`readline` returns the second line, if it
    exists, and so on. When there is nothing left to read, :meth:`readline()
    <codecs.StreamReader.readline>` returns an empty string.

This behaviour of :meth:`readline() <codecs.StreamReader.readline>` makes it
easy to determine, for example, the number of lines in a file:

.. code-block:: pycon

   >>> with p.open() as f:
   ...     lc = 0
   ...     while f.readline() != "":
   ...         lc = lc + 1
   ...     print(lc)
   ...
   2

A shorter way to count all lines is to use the built-in :meth:`readlines()
<codecs.StreamReader.readlines>` method, which reads all lines of a file and
returns them as a list of strings, with one string per line:

.. code-block:: pycon

   >>> with p.open() as f:
   ...     print(len(f.readlines()))
   ...
   2

However, if you count all lines in a large file, this method can cause memory to
overflow because the entire file is read at once. It is also possible for memory
to overflow with :meth:`readline() <codecs.StreamReader.readline>` if you try to
read a line from a large file that does not contain line break characters. To
better handle such situations, both methods have an optional argument that
affects the amount of data read at a time. Another way to iterate over all lines
of a file is to treat the file object as an iterator in a :ref:`for-loop`:

.. code-block:: pycon

   >>> with p.open() as f:
   ...     lc = 0
   ...     for l in f:
   ...         lc = lc + 1
   ...     print(lc)
   ...
   2

This method has the advantage that the lines are read into memory as needed, so
even with large files, there is no need to worry about running out of memory.
The other advantage of this method is that it is simpler and more readable.

However, a potential problem with the read method can arise if translations are
performed in text mode on Windows and macOS when you use the :func:`open`
command in text mode, in other words, without appending a ``b``. In text mode,
macOS converts every ``\r`` to ``\n``, while Windows converts ``\r\n`` pairs to
``\n``. You can specify how line breaks are handled by using the newline
parameter when opening the file and specifying ``newline="\n"``, ``\r`` or
``\r\n``, which will only use that string as a line break:

.. code-block:: pycon

   >>> with p.open(newline="\r\n") as f:
   ...     lc = 0
   ...

In this example, only ``\n`` is interpreted as a line break. However, if the
file was opened in binary mode, the ``newline`` parameter is not necessary, as
all bytes are returned exactly as they appear in the file.

:meth:`python3:pathlib.Path.read_text`
    returns the decoded content of the specified file as a string:

    .. code-block:: pycon

       >>> p.read_text()
       'This is the first line of myfile.\nAnd this is another line.\n'

:meth:`python3:pathlib.Path.write_text`
    opens the specified file in text mode, writes data to it, and closes the
    file:

    .. code-block:: pycon

       >>> p.write_text("New content")
       11
       >>> p.read_text()
       'New content'

    An existing file with the same name will be overwritten.

Reading directories
-------------------

:meth:`python3:pathlib.Path.iterdir`
    If the path refers to a directory, the path objects of the directory
    contents are returned:

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

The child objects are returned in arbitrary order, and the special entries ``.``
and ``..`` are not included. If the path is not a directory or is otherwise
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
    recursively finds the specified relative pattern. This corresponds to
    calling with ``**/`` before the pattern.

:meth:`python3:pathlib.Path.walk`
    generates the file names in a directory structure by traversing the
    structure either from top to bottom or from bottom to top. It returns a
    3-tuple consisting of ``(dirpath, dirnames, filenames)``.

    With the default setting of the optional argument ``top_down=True``, the
    triple for a directory is generated before the triples for its
    subdirectories.

    With ``follow_symlinks=True``, symlinks are resolved and placed in
    ``dirnames`` and ``filenames`` according to their targets.

    The following example shows the size of the files in a directory, ignoring
    :file:`__pycache__` directories:

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
    from bottom to top, as :meth:`python3:pathlib.Path.rmdir` only allows a
    directory to be deleted if it is empty:

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
    creates a file at the specified path. ``mode`` can be used to specify the
    file mode and access flags. If the file already exists, the modification
    time is updated to the current time if ``exist_ok=True``, otherwise a
    :class:`python3:FileExistsError` is raised.

    .. note::
       :meth:`python3:pathlib.Path.open` or :meth:`pathlib.Path.write_text`
       are also often used to create files.

:meth:`python3:pathlib.Path.mkdir`
    creates a new directory under the specified path. The parameters ``mode``
    and ``exist_ok`` work as specified in :meth:`python3:pathlib.Path.touch`.

    If ``parents=True``, missing parent directories of the path are created as
    needed with the default permissions. With the default setting
    ``parents=False``, however, :class:`python3:FileNotFoundError` is triggered.

Renaming, copying and deleting
------------------------------

:meth:`python3:pathlib.Path.rename`
    renames the file or directory to the specified destination and returns a new
    :class:`python3:pathlib.Path` instance that points to the destination. On
    Unix, if the destination exists and is a file, it is simply replaced; on
    Windows, a :class:`python3:FileExistsError` is raised.

    .. code-block:: pycon

       >>> myfile = Path("docs", "save-data", "myfile.txt")
       >>> newfile = Path("docs", "newdir", "newfile.txt")
       >>> myfile.rename(newfile)
       PosixPath('docs/newdir/newfile.txt')

.. versionadded:: 3.14
   The methods :meth:`pathlib.Path.copy`, :meth:`pathlib.Path.copy_into`,
   :meth:`pathlib.Path.move` and :meth:`pathlib.Path.move_into` are added.

   .. seealso::
      `Python 3.14 Changelog
      <https://docs.python.org/3.14/whatsnew/3.14.html#pathlib>`_

Permissions and ownership
-------------------------

:meth:`python3:pathlib.Path.owner`
    returns the name of the person who owns the file. Normally, symlinks are
    followed, but if you want to determine the person who owns the symlink, add
    ``follow_symlinks=False``. If the user ID (UID) of the file is not found, a
    :class:`python3:KeyError` is raised.

:meth:`python3:pathlib.Path.group`
    returns the name of the group that owns the file. The behaviour for symlinks
    is the same as for :meth:`python3:pathlib.Path.owner`. And if the group ID
    (GID) of the file is not found, a :class:`python3:KeyError` is also raised.

:meth:`python3:pathlib.Path.chmod`
    changes the file mode and permissions. Symlinks are normally followed. To
    change the symlink permissions, you can use ``follow_symlinks=False`` or
    :meth:`python3:pathlib.Path.lchmod`.

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
