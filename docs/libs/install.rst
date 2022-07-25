Adding more Python libraries
============================

Although Python’ :doc:`batteries` philosophy means that you can already do a lot
with the default installation of Python, there will inevitably come a situation
where you need functionality that is not included in Python. This section gives
an overview of the options available to you.

If you are lucky, you will find the extra functionality you need in a package
for your operating system – with a Windows or macOS executable installer, or a
package for your Linux distribution.

This is one of the easiest ways to add a library to your Python installation, as
the installer or your package manager will take care of all the details to
correctly add the module to your system. In general, however, such pre-built
packages are not the norm for Python software.

Installing Python libraries with ``pip`` and ``venv``
-----------------------------------------------------

If you need a third-party module that is not pre-built for your platform, you
will have to turn to its source distribution. However, this brings two problems:

#. To install the source distribution, you need to find and download it.
#. Certain Python paths and permissions on your system are expected.

Python offers :term:`pip` as a current solution to both problems. ``pip`` tries
to find the module in the :term:`Python Package Index (PyPI)`, downloads it and
all dependencies, and takes care of the installation. The basic syntax of
``pip`` is quite simple: for example, to install the popular ``requests``
library from the command line, all you have to do is the following:

.. code-block:: console

    $ python3.8 -m pip install requests

If you want to specify a particular version of a package, you can simply append
the version numbers:

.. code-block:: console

    $ python3.8 -m pip install requests==2.28.1

or

.. code-block:: console

    $ python3.8 -m pip install requests>=2.28.0

Installing with the ``--user`` option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often, however, you will not be able or willing to install a Python package in
the main Python instance. Maybe you need a more recent version of a library, but
another application still needs an older version. Or maybe you don’t have
sufficient administrator rights to change the system’s default Python. In such
cases, one possibility is to install the library with the ``--user`` flag: this
installs the library in the home directory, where it can then only be used by
you:

.. code-block:: console

    $ python3.8 -m pip install --user requests

.. seealso::

   * :doc:`python3:installing/index`

Virtual environments
~~~~~~~~~~~~~~~~~~~~

However, there is an even better option if you want to avoid installing
libraries in the Python system. This option is called a *virtual environment*
(``virtualenv``). It is a self-contained directory structure that contains both
an installation of Python and the additional packages. Because the entire Python
environment is contained in the virtual environment, the libraries and modules
installed there cannot collide with those in the main system or in other virtual
environments, so different applications can use different versions of Python and
its packages. Creating and using a virtual environment is a two-step process:

#. First we create the environment:

   .. code-block:: console

      $ python3.8 -m venv myenv

   This creates the environment with Python and ``pip`` in a directory called
   ``myenv``.

#. You can then install Python packages for this virtual environment only:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ cd myenv
         $ bin/python3.8 -m pip install requests

   .. tab:: Windows

      .. code-block:: console

         > cd myenv
         > Scripts\python.exe -m pip install requests

   .. note::
      The Python version you used to create the environment is the default
      Python version for that environment, so you can just use ``python``
      instead of ``python3`` or ``python3.8``.

Virtual environments are very useful and common practice for managing projects
and their dependencies, especially for working on multiple projects. This is
also the reason why I don’t recommend activating a virtual environment: you can
easily lose track of which virtual environment is currently active.

.. seealso::
   * :doc:`python3:tutorial/venv`

PyPI
~~~~

The :term:`Python Package Index (PyPI)` is the standard package index, but by
no means the only repository for Python code. You can access it directly at
https://pypi.python.org and search for packages or filter the packages by
category.
