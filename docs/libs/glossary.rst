Glossary
========

.. glossary::

   built distribution
       A structure of files and metadata that only needs to be moved to the
       correct location on the target system during installation. :term:`wheel`
       is such a format, but not *distutilâ€™s* :term:`source distributions
       <source distribution (sdist)>` that require a build step.

   conda
       Package management tool for the `Anaconda
       <https://docs.continuum.io/anaconda/index.html>`_ distribution from
       `Continuum Analytics <https://www.anaconda.com/>`_. Itâ€™s specifically
       aimed at the scientific community, particularly Windows, where installing
       binary extensions is often difficult.

       Conda does not install packages from PyPI and can only install from the
       official Continuum repositories or from `anaconda.org
       <https://anaconda.org/>`_ or local ( e.g. intranet) package servers.
       Note, however, that Pip can be installed in conda and can work side by
       side to manage distributions of PyPI.

       .. seealso::
          * `Conda: Myths and Misconceptions
            <https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>`_
          * `Conda build variants
            <https://docs.conda.io/projects/conda-build/en/latest/resources/variants.html>`_

   devpi
       `devpi <https://devpi.net/>`_ is a powerful PyPI compatible server and
       PyPI proxy cache with a command line tool to enable packaging, testing
       and publishing activities.

   distribution package
       A versioned archive file that contains Python :term:`packages <import
       package>`, :term:`modules <module>`, and other resource files used to
       distribute a :term:`release`.

   egg
       A :term:`built distribution` format introduced by :term:`setuptools`
       that is now being replaced by :term:`wheel`. For more information, see
       `The Internal Structure of Python Eggs
       <https://setuptools.readthedocs.io/en/latest/deprecated/python_eggs.html>`_
       and `Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_.

   import package
       A Python module that can contain other modules or recursively other
       packages.

   module
       The basic unit of code reusability in Python, which exists in one of two
       types:

       pure module
           A module written in Python contained in a single ``.py`` file (and
           possibly associated ``.pyc``- and/or ``.pyo`` files).

       extension module
           Usually a single dynamically loadable precompiled file, e.g. a common
           object file (``.so``).

   pip
       A tool for installing Python packages.


       `Docs <https://pip.pypa.io/>`__ |
       `GitHub <https://github.com/pypa/pip>`__ |
       `PyPI <https://pypi.org/project/pip/>`__ |

   pypi.org
       `pypi.org  <https://pypi.org/>`_ is the domain name for the Python
       Package Index (PyPI). In 2017 it replaced the old index domain name
       *pypi.python.org*. He is supported by :term:`warehouse`.

   Python Package Index (PyPI)
       `PyPI <https://pypi.org/>`_ is the standard package index for the Python
       community. All Python developers can use and distribute their
       distributions.

   Python Packaging Authority
   PyPA
       The `Python Packaging Authority <https://www.pypa.io/en/latest/>`_ is a
       working group that manages several software projects for packaging,
       distributing and installing Python libraries. However, the goals stated
       in `PyPA Goals <https://www.pypa.io/en/latest/future/>`_ were created
       during discussions around :pep:`516`, :pep:`517` and :pep:`518`, which
       allowed competing workflows with the :term:`pyproject.toml-based build
       system that do not need to be interoperable.

   release
       The snapshot of a project at a specific point in time, identified by a
       version identifier.

       One release can result in several :term:`Built Distributions
       <built distribution>`.

   setuptools
       setuptools (and ``easy_install``) is a collection of improvements to the
       Python Distutils that make it easier to create and distribute Python
       distributions, especially those that have dependencies on other packages.

   source distribution (sdist)
        A distribution format (typically generated using) ``python setup.py
        sdist``.

        It provides metadata and the essential source files required for
        installation with a tool like :term:`Pip` or for generating :term:`built
        distributions <built distribution>`.

   virtualenv
       An isolated Python environment that allows packages to be installed for a
       specific application rather than installing them system-wide.

       `Docs <https://docs.python.org/3/library/venv.html>`__ |
       `Creating Virtual Environments
       <https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ |

   Warehouse
       The current code base that powers the Python Package Index (PyPI). It is
       hosted on `pypi.org`_.

   wheel
       Distribution format introduced with `PEP 427
       <https://www.python.org/dev/peps/pep-0427/>`_. It is intended to replace
       the :term:`Egg` format and is supported by current :term:`pip`
       installations.

       C extensions can be provided as platform-specific wheels for Windows, Mac
       OS and Linux on PyPI. This has the advantage for the users of the package
       that they donâ€™t have to compile during the installation.

       `Home <https://pythonwheels.com/>`_ |
       `Docs <https://wheel.readthedocs.io/>`__ |
       `PEP <https://www.python.org/dev/peps/pep-0427/>`_ |
       `GitHub <https://github.com/pypa/wheel>`__ |
       `PyPI <https://pypi.org/project/wheel/>`__ |
