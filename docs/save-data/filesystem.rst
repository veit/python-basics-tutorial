File system
===========

To work with files, you often have to interact with the file system and the
different conventions depending on the operating system. For this I show you
:doc:`os <python3:library/os>` and especially :doc:`os.path
<python3:library/os.path>`.

Paths and path names
--------------------

All operating systems refer to files with strings called pathnames. Python
provides a number of functions to help you solve some problems. The semantics of
pathnames are very similar on all operating systems because the file system is
usually modelled as a tree structure, with a hard disk representing the root and
folders, subfolders, :abbr:`etc. (et cetera)` representing the branches and
subbranches; this means that most operating systems refer to a particular file
in a very similar way.

However, different operating systems have different conventions for path names.
The character used to separate consecutive file or directory names in a
Linux/macOS pathname is ``/``, while in a Windows pathname it is ``\``. Also,
the Linux file system has a single root directory referred to by a ``/``
character as the first character in the path name, while the Windows file system
has a separate root directory for each drive, referred to as :samp:`{C:\\}`, and
so on. Because of these differences, files have different path names on
different operating systems. A file named :samp:`{C:\\DATA\\MYFILE}` on Windows
could be :samp:`{/DATA/MYFILE}` on Linux and macOS. Python provides functions
and variables that allow you to perform common pathname manipulations without
having to worry about such syntactical details. With a little care, you can
write your Python programs to run correctly regardless of the underlying file
system.

Absolute and relative paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~

These operating systems allow two types of path names:

Absolute path names
    uniquely indicate the exact position of a file in the file system by listing
    the entire path to that file, starting with the root directory of the file
    system.

    Two absolute Windows path names are given here as examples:

    .. code-block:: ps1con

       C:\Program Files\Python 3.13\
       D:\backup\2022\06\

    And here are two absolute Linux path names and one absolute macOS path name:

    .. code-block:: console

       /bin/python3
       /cdrom/backup/2022/06/
       /Applications/Python\ 3.13/

Relative pathnames
    indicate the position of a file relative to another point in the file
    system, and this other point is not indicated in the relative path name
    itself.

    As example, a Windows relative pathname is given here:

    .. code-block:: ps1con

       save-data\filesystem.rst

    … and here a relative Linux/macOS pathname:

    .. code-block:: console

       save-data/filesystem.rst

    Relative paths therefore require a context in which they are anchored. This
    context is usually provided in one of two ways:

    * The relative path is appended to an existing absolute path, creating a new
      absolute path. If you have a Windows relative path
      :samp:`{Start Menu\\Programs\\Python 3.13}` and an absolute path
      :samp:`{C:\\Users\\Veit}`, then by appending the relative path a new
      absolute path: :samp:`C:\\Users\\Veit\\Start Menu\\Programs\\Python 3.13`
      can be created. If you append the same relative path to another absolute
      path (for example to :samp:`C:\\Users\\Tim`, you will get a new path
      referring to another :samp:`HOME` directory (:samp:`{Tim}`).
    * Relative paths can also be given a context by implicitly referring to the
      current working directory, that is the directory in which a Python
      programme is located at the time it is executed. Python commands can
      implicitly refer back to the current working directory if a relative path
      is passed to them as an argument. For example, if you use the
      :samp:`os.listdir('{RELATIVE/PATH}')` command with a relative path
      argument, the anchor for that relative path is the current working
      directory, and the result of the command is a list of the filenames in the
      directory whose path is formed by appending the current working directory
      to the relative path argument.

      The directory in which a Python file is located is called the current
      working directory. This directory will usually be different from the
      directory where the Python interpreter is located. To illustrate this,
      let’s start Python and use the command :func:`python3:os.getcwd` to find
      out the current working directory of Python:

      .. code-block:: pycon

         >>> import os
         >>> os.getcwd()
         '/home/veit'

      .. note::
         ``os.getcwd()`` is used as a function call without arguments to make it
         clear that the returned value is not a :term:`constant`, but changes
         when you change the value of the current working directory. In the
         example above, the result is the home directory on one of my Linux
         machines. On Windows machines, additional backslashes would be added to
         the path: ``C:\\Users\\Veit``, because Windows uses the backslash ``\``
         as a path separator, but it has a different meaning in
         :doc:`/types/strings/index`.

      To display the contents of the current directory, you can enter the
      following:

      .. code-block:: pycon

         >>> os.listdir(os.curdir)
         ['.gnupg', '.bashrc', '.local', '.bash_history', '.ssh', '.bash_logout', '.profile', '.idlerc', '.viminfo', '.config', 'Downloads', 'Documents', '.python_history']

      However, you can also change to another directory and then have the
      current working directory displayed:

      .. code-block:: pycon

         >>> os.chdir("Downloads")
         >>> os.getcwd()
         '/home/veit/Downloads'

Change path names
~~~~~~~~~~~~~~~~~

Python provides some ways to change pathnames with the :doc:`os.path
<python3:library/os.path>` submodule without having to explicitly use an
operating system-specific syntax.

:func:`python3:os.path.join`
    constructs path names for different operating systems, for example under
    Windows:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.join("save-data", "filesystem.rst"))
       save-data\filesystem.rst

    Here, the arguments are interpreted as a series of directory or file names
    to be joined into a single string that is understood by the underlying
    operating system as a relative path. Under Windows, this means that the
    names of the path components are connected with backslashes (``\``).

    If you do the same under Linux/macOS, on the other hand, you will get ``/``
    as the separator:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.join("save-data", "filesystem.rst"))
       save-data/filesystem.rst

    You can therefore use this method to create file paths independently of the
    operating system on which your programme is running.

    The arguments do not necessarily have to be individual directory or file
    names either; they can also be sub-paths that are then joined together to
    form a longer path name. The following example illustrates this under
    Windows, where either slashes (``/``) or double backslashes (``\\``) can be
    used in the strings:

    .. code-block:: pycon

       >>> import os
       >>> print(
       ...     os.path.join(
       ...         "python-basics-tutorial-de\\docs", "save-data\\filesystem.rst"
       ...     )
       ... )
       python-basics-tutorial-de\docs\save-data\filesystem.rst

:func:`os.path.split`
    returns a tuple with two elements that separates the base name of a path
    from the rest of the path, for example under macOS:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.split(os.getcwd()))
       ('/home/veit/python-basics-tutorial-de', 'docs')

:func:`python3:os.path.basename`
    returns only the base name of the path:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.basename(os.getcwd()))
       docs

:func:`python3:os.path.dirname`
    returns the path up to the base name:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.dirname(os.getcwd()))
       /home/veit/python-basics-tutorial-de

:func:`python3:os.path.splitext`
    outputs the dotted extension notation used by most file systems to indicate
    the file type:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.splitext("filesystem.rst"))
       ('filesystem', '.rst')

    The last element of the returned tuple contains the dotted extension of the
    specified file.

:func:`python3:os.path.commonpath`
    is a more specialised function to manipulate path names. It finds the common
    path for a group of paths and is thus good for finding the lowest level
    directory that contains each file in a group of files:

    .. code-block:: pycon

       >>> import os
       >>> print(os.path.commonpath(["save-data/filesystem.rst", "save-data/index.rst"]))
       save-data

:func:`python3:os.path.expandvars`
    expands environment variables in paths:

    .. code-block:: pycon

       >>> os.path.expandvars("$HOME/python-basics-tutorial")
       '/home/veit/python-basics-tutorial'

Useful variables and functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:data:`python3:os.name`
    returns the name of the Python module that was imported to handle the
    operating system specific details, for example:

    .. code-block:: pycon

       >>> import os
       >>> os.name
       'nt'

    .. note::
       Most versions of Windows, with the exception of Windows CE, are
       identified as ``nt``.

    On macOS and Linux, the answer is ``posix``. Depending on the platform, you
    can perform special operations with this answer:

    .. code-block:: pycon

       >>> import os
       >>> if os.name == "posix":
       ...     root_dir = "/"
       ... elif os.name == "nt":
       ...     root_dir = "C:\\"
       ... else:
       ...     print("The operating system was not recognised!")
       ...

Getting information about files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

File paths show files and directories on your hard disk. To find out more about
them, there are several Python functions, including

:func:`python3:os.path.exists`
    returns ``True`` if its argument is a path that matches a path that exists
    in the filesystem.
:func:`python3:os.path.isfile`
    returns ``True`` if and only if the given path points to a file, and returns
    ``False`` otherwise, including the possibility that the path argument points
    to nothing in the filesystem.
:func:`python3:os.path.isdir`
    returns ``True`` if and only if its path argument points to a directory;
    otherwise it returns ``False``.

Other similar functions provide more specific queries:

:func:`python3:os.path.islink`
    returns ``True`` if a path specifies a file that is a link. However, Windows
    link files with the extension ``.lnk`` are not real links in this sense and
    return ``False``. Links created only with ``mklink()`` also return ``True``.
:func:`python3:os.path.ismount`
    returns True on ``possix`` filesystems if the path is a mount point.
:func:`python3:os.path.samefile`
    returns ``True`` if the two path arguments point to the same file.
:func:`python3:os.path.isabs`
    returns ``True`` if its argument is an absolute path; otherwise returns
    ``False``.
:func:`python3:os.path.getsize`
    returns the size of the file or directory.
:func:`python3:os.path.getmtime`
    specifies the modification date of the file or directory.
:func:`python3:os.path.getatime`
    gives the last access time for a file or directory.

Other file system operations
----------------------------

Python has other very useful commands in the :mod:`python3:os` module: Below I
describe only some cross-operating system operations, but more specific file
system functions are also provided.

:func:`os.rename`
    names or moves a file or directory, for example

    .. code-block:: pycon

       >>> os.rename("filesystem.rst", "save-data/filesystem.rst")

:func:`os.remove`
    deletes files, for example

    .. code-block:: pycon

       >>> os.remove("filesystem.rst")

:func:`os.rmdir`
    deletes an empty directory. To remove non-empty directories, use
    :func:`shutil.rmtree`; this function recursively removes all files in a
    directory tree.

:func:`os.makedirs`
    creates a directory with all necessary intermediate directories, for example

    .. code-block:: pycon

       >>> os.makedirs("save-data/filesystem")

Processing all files in a directory
-----------------------------------

A useful function for recursively walking through directory structures is
:func:`os.walk`. You can use it to walk an entire directory tree and, for each
directory, return the path of that directory, a list of its subdirectories and a
list of its files. It can have three optional arguments: ``os.walk(directory,
topdown=True, onerror=None, followlinks= False)``.

``directory``
    is the path of the starting directory
``topdown``
    on ``True`` or not present, processes the files in each directory before the
    subdirectories, resulting in a listing that starts at the top and goes down;

    on ``False``, the subdirectories of each directory are processed first,
    resulting in a traversal of the tree from bottom to top.

``onerror``
    can be set to a function to handle errors resulting from calls to
    :func:`os.listdir`, which are ignored by default. Usually symbolic links are
    not followed unless you specify the parameter ``follow-links=True``.

.. code-block:: pycon
   :linenos:

   >>> import os
   >>> for root, dirs, files in os.walk(os.curdir):
   ...     print("{0} has {1} files".format(root, len(files)))
   ...     if ".ipynb_checkpoints" in dirs:
   ...         dirs.remove(".ipynb_checkpoints")
   ...
   . has 13 files
   ./control-flows has 13 files
   ./save-data has 30 files
   ./test has 15 files
   ./test/coverage has 3 files
   …

Line 4
    checks for a directory called ``.ipynb_checkpoints``.
Line 5
    removes ``.ipynb_checkpoints`` from the directory list.

:func:`shutil.copytree` recursively makes copies of all files in a directory and
all its subdirectories, preserving information about access and modification
times. :mod:`shutil` also has the already mentioned :func:`shutil.rmtree`
function for removing a directory and all its subdirectories, and several
functions for making copies of individual files.
