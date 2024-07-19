Packages and programmes
=======================

.. _wheels:

wheels
------

The current standard format for distributing Python libraries and programs is
the use of :term:`wheels <wheel>`. wheels are designed to make the installation
of Python code more reliable and to make dependency management easier. However,
the details of creating wheels are beyond the scope of this section, but full
details of the requirements and process for creating wheels can be found in
:doc:`distribution`.

.. seealso::
   * Pradyun Gedam: `Thoughts on the Python packaging ecosystem
     <https://pradyunsg.me/blog/2023/01/21/thoughts-on-python-packaging/>`_

``py2exe`` and ``py2app``
-------------------------

`py2exe <https://www.py2exe.org/>`_ creates standalone Windows applications and
`py2app <https://py2app.readthedocs.io/en/latest/>`_ does the same for macOS. In
both cases, these are single executables that can run on machines that do not
have Python installed. In many ways, however, standalone executables are not
ideal, as they tend to be larger and less flexible than native Python
applications, but in some situations they can also be the best or only solution.

``freeze``
----------

The ``freeze`` tool also creates an executable Python programme that runs on
computers that do not have Python installed. If you want to use the ``freeze``
tool, you will probably need to download the Python source code.

*Freezing* a Python program creates C files that are then compiled and linked
with a C compiler that you must have installed on your system. The application
thus frozen will only run on platforms for which the C compiler used provides
its executables.

.. seealso::

    * `Tools/freeze <https://github.com/python/cpython/tree/main/Tools/freeze>`_

PyInstaller and PyOxidizer
--------------------------

`PyInstaller <https://pyinstaller.org/en/stable/index.html#>`_ and `PyOxidizer
<https://pyoxidizer.readthedocs.io/en/pyoxidizer-0.17/index.html>`_ bundle a
Python application and all its dependencies into a single package.

.. _briefcase:

Briefcase
---------

`Briefcase <https://beeware.org/project/projects/tools/briefcase/>`__ is a tool
for converting a Python project into a stand-alone native application for Mac,
Windows, Linux, iPhone/iPad and Android.

.. _beeware:

BeeWare
-------

`BeeWare <https://beeware.org>`__ converts your Python project into a standalone
iOS, Android, Windows, MacOS, Linux, Web and tvOS app.
