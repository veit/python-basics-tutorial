Packages
========

Wheels
~~~~~~

The current standard format for distributing Python modules and applications is
to use `Wheels <https://pythonwheels.com/>`_. Wheels were developed to make the
installation of Python code more reliable and to make dependency management
easier. However, the details of creating wheels are beyond the scope of this
section, but full details of the requirements and the process for creating
wheels can be found in doc:`jupyter-tutorial:productive/packaging/distribution`.

``py2exe`` and ``py2app``
~~~~~~~~~~~~~~~~~~~~~~~~~

`py2exe <https://www.py2exe.org/>`_ creates standalone Windows applications and
`py2app <https://py2app.readthedocs.io/en/latest/>`_ does the same for macOS. In
both cases, these are single executables that can run on machines that do not
have Python installed. In many ways, however, standalone executables are not
ideal, as they tend to be larger and less flexible than native Python
applications, but in some in some situations they can also be the best or only
solution.

``freeze``
~~~~~~~~~~

The ``freeze`` tool also creates an executable Python programme that runs on
computers that do not have Python installed. If you want to use the ``freeze``
tool, you will probably need to download the Python source code.

*Freezing* a Python program creates C files that are then compiled and linked
with a C compiler that you must have installed on your system. The application
thus frozen will only run on platforms for which the C compiler used provides
its executables.

.. seealso::

    * `Tools/freeze <https://github.com/python/cpython/tree/main/Tools/freeze>`_
