*„Batteries included“*
======================

In Python, a library can consist of several components, including built-in data
types and constants that can be used without an import statement, such as
:doc:`/types/numbers` and :doc:`/types/lists`, as well as some built-in
:doc:`/functions/index` and :doc:`/control-flows/exceptions`. The largest part
of the library is an extensive collection of :doc:`/modules/index`. If you have
Python installed, there are also several libraries available for you to use.

* :ref:`data-types`
* :ref:`files-storage`
* :ref:`os`
* :ref:`internet`
* :ref:`dev-debug`

.. _data-types:

Managing data types
-------------------

The standard library naturally contains support for the types built into Python.
In addition, there are three categories in the standard library that deal with
different data types: Modules for strings, datatypes and numbers.

String modules
~~~~~~~~~~~~~~

.. include:: ../types/strings.rst
   :start-after: string-modules

Modules for data types
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-------------------------------------------------------------------------------+
| Module                | Description                                                                   |
+=======================+===============================================================================+
| :py:mod:`datetime`,   | Time and calendar operations                                                  |
| :py:mod:`calendar`    |                                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`collections` | Container data types                                                          |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`enum`        | allows the creation of enumeration classes that bind symbolic names to        |
|                       | constant values                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`array`       | Efficient arrays of numeric values                                            |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`sched`       | Event scheduler                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`queue`       | Synchronised queue class                                                      |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`copy`        | Shallow and deep copy operations                                              |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`pprint`      | prints Python data structures „pretty“.                                       |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`typing`      | supports commenting code with hints about the types of objects, especially    |
|                       | function parameters and return values                                         |
+-----------------------+-------------------------------------------------------------------------------+

Modules for numbers
~~~~~~~~~~~~~~~~~~~

.. include:: ../types/numbers.rst
   :start-after: number-modules

.. _files-storage:

Changing files
--------------

.. include:: ../types/files.rst
   :start-after: file-modules

.. _os:

Interacting with the operating system
-------------------------------------

+-------------------------------+-------------------------------------------------------------------------------+
| Module                        | Description                                                                   |
+===============================+===============================================================================+
| :py:mod:`os`                  | Various operating system interfaces                                           |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`platform`            | Access to the identification data of the underlying platform                  |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`time`                | Time access and conversions                                                   |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`io`                  | Tools for working with data streams                                           |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`select`              | Waiting for I/O completion                                                    |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`optparse`            | Parser for command line options                                               |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`curses`              | Terminal handling for character cell displays                                 |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`getpass`             | Portable password entry                                                       |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`ctypes`              | provides C-compatible data types                                              |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`threading`           | high-level threading interface                                                |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`multiprocessing`     | Process-based threading interface                                             |
+-------------------------------+-------------------------------------------------------------------------------+
| :doc:`subprocess              | Management of subprocesses                                                    |
| <python3:library/subprocess>` |                                                                               |
+-------------------------------+-------------------------------------------------------------------------------+

.. _internet:

Use of Internet protocols
-------------------------

+-----------------------------------+-------------------------------------------------------------------------------+
| Module                            | descriptiong                                                                  |
+===================================+===============================================================================+
| :py:mod:`socket`,                 | Low-level network interface and SSL wrapper for socket objects                |
| :py:mod:`ssl`                     |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`email`                   | Email and MIME processing package                                             |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`mailbox`                 | Manipulation of mailboxes in various formats                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`cgi`,                    | Common Gateway Interface support                                              |
| :py:mod:`cgitb`                   |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`wsgiref`                 | WSGI utilities and reference implementation                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`urllib.request`,         | Open and parse URLs                                                           |
| :py:mod:`urllib.parse`            |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`ftplib`,                 | Clients for various Internet protocols                                        |
| :py:mod:`poplib`,                 |                                                                               |
| :py:mod:`imaplib`,                |                                                                               |
| :py:mod:`nntplib`,                |                                                                               |
| :py:mod:`smtplib`,                |                                                                               |
| :py:mod:`telnetlib`               |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`socketserver`            | Framework for network servers                                                 |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`http.server`             | HTTP server                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`xmlrpc.client`,          | XML-RPC client and server                                                     |
| :py:mod:`xmlrpc.server`           |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+


.. _dev-debug:

Developing and debugging
------------------------

+-----------------------------------+-------------------------------------------------------------------------------+
| Module                            | Description                                                                   |
+===================================+===============================================================================+
| :py:mod:`pydoc`                   | Documentation generator and online help system                                |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`doctest`                 | Test examples from Python docstrings                                          |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`unittest`                | Framework for unittests, see also :doc:`/test/unittest`                       |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`test.support`            | Utility functions for tests                                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`trace`                   | traces the execution of Python statements                                     |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`pdb`                     | Python debugger                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`logging`                 | logging function for Python                                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`timeit`                  | measures the execution time of small code snippets                            |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`profile`,                | Python profiler                                                               |
| :py:mod:`cProfile`                |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`sys`                     | System-specific parameters and functions                                      |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`gc`                      | Functions of the Python garbage collector                                     |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`inspect`                 | inspects objects live                                                         |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`atexit`                  | exit handler                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`__future__`              | Future statement definitions                                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`imp`                     | allows access to the import internals                                         |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`zipimport`               | imports modules from zip archives                                             |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`modulefinder`            | finds modules used by a script                                                |
+-----------------------------------+-------------------------------------------------------------------------------+
