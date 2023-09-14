Glossary
========

.. glossary::

   build
       ``build`` is a :pep:`517`-compatible Python package builder. It provides
       a CLI for building packages and a Python API.

       `Docs <https://pypa-build.readthedocs.io/en/stable/index.html>`__ |
       `GitHub <https://github.com/pypa/build>`__ |
       `PyPI <https://pypi.org/project/build>`__

   built distribution
   bdist
       A structure of files and metadata that only needs to be moved to the
       correct location on the target system during installation. :term:`wheel`
       is such a format, but not *distutils* :term:`Source Distribution` that
       require a build step.

   cibuildwheel
       :doc:`/libs/cibuildwheel` is a Python package that creates :term:`wheels
       <wheel>` for all common platforms and Python versions on most CI systems.

       `Docs <https://cibuildwheel.readthedocs.io/>`__ |
       `GitHub <https://github.com/pypa/cibuildwheel>`__ |
       `PyPI <https://pypi.org/project/cibuildwheel>`__

       .. seealso::
          :term:`multibuild`

   conda
       Package management tool for the `Anaconda
       <https://docs.continuum.io/anaconda/index.html>`_ distribution from
       `Continuum Analytics <https://www.anaconda.com/>`_. It’s specifically
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
       `devpi <https://devpi.net/>`_ is a powerful :term:`PyPI` compatible
       server and PyPI proxy cache with a command line tool to enable packaging,
       testing and publishing activities.

       `Docs <http://doc.devpi.net/latest/>`__ |
       `GitHub <https://github.com/devpi/devpi>`__ |
       `PyPI <https://pypi.org/project/devpi>`__

   distribution package
       A versioned archive file that contains Python :term:`packages <import
       package>`, :term:`modules <module>`, and other resource files used to
       distribute a :term:`release`.

   distutils
       Python standard library package that provides support for bootstrapping
       :term:`pip` into an existing Python installation or :term:`virtual
       environment`.

       `Docs <https://docs.python.org/3/library/ensurepip.html>`__ |
       `GitHub <https://github.com/pypa/distutils>`__

   egg
       A :term:`built distribution` format introduced by :term:`setuptools`
       that is now being replaced by :term:`wheel`. For more information, see
       `The Internal Structure of Python Eggs
       <https://setuptools.readthedocs.io/en/latest/deprecated/python_eggs.html>`_
       and `Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_.

   enscons
       enscons is a Python packaging tool based on `SCons <http://scons.org/>`_.
       It builds :term:`pip`-compatible :term:`source distributions <source
       distribution>` and :term:`wheels <wheel>` without using :term:`distutils`
       or :term:`setuptools`, including distributions with C extensions. enscons
       has a different architecture and philosophy than :term:`distutils`, as it
       adds Python packaging to a general build system. enscons can help you
       build :term:`sdists <sdist>` and :term:`wheels <wheel>`.

       `GitHub <https://github.com/dholth/enscons>`__ |
       `PyPI <https://pypi.org/project/enscons>`__

   Flit
       Flit provides an easy way to build pure Python packages and modules and
       upload them to the :term:`Python Package Index`. Flit can generate a
       configuration file to quickly set up a project, create a :term:`source
       distribution` and :term:`wheel`, and upload them to PyPI.

       Flit uses :term:`pyproject.toml` to configure a project. Flit does not
       rely on tools like :term:`setuptools` to create distributions, or on
       :term:`twine` to upload them to :term:`PyPI`.

       `Docs <https://flit.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/pypa/flit>`__ |
       `PyPI <https://pypi.org/project/flit>`__

   Hatch
       Hatch is a command line tool that you can use to configure and version
       packages, specify dependencies and with the build backend Hatchling also
       publish to the :term:`Python Package Index`. The plug-in system allows
       easy extension of the functionalities.

       `Docs <https://hatch.pypa.io/latest/>`__ |
       `GitHub <https://github.com/pypa/hatch>`__ |
       `PyPI <https://pypi.org/project/hatch>`__

   import package
       A Python module that can contain other modules or recursively other
       packages.

   meson-python
       Build backend that uses the `Meson <https://mesonbuild.com>`_ build
       system. It supports a variety of languages, including C, and is able to
       meet the requirements of most complex build configurations.

       `Docs <https://meson-python.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/mesonbuild/meson-python>`__ |
       `PyPI <https://pypi.org/project/meson-python/>`__

   module
       The basic unit of code reusability in Python, which exists in one of two
       types:

       pure module
           A module written in Python contained in a single ``.py`` file (and
           possibly associated ``.pyc``- and/or ``.pyo`` files).

       extension module
           Usually a single dynamically loadable precompiled file, for example a
           common object file (``.so``).

   multibuild
       ``multibuild`` is a set of CI scripts for building and testing Python
       :term:`wheels <wheel>` for Linux, macOS and Windows.

       .. seealso::
          :term:`cibuildwheel`

   pdm
       Python package manager with :pep:`582` support. It installs and manages
       packages without the need to create a :term:`virtual environment`. It
       also uses :term:`pyproject.toml` to store project metadata as defined in
       :pep:`621`.

       `Docs <https://pdm.fming.dev/>`__ |
       `GitHub <https://github.com/pdm-project/pdm/>`__ |
       `PyPI <https://pypi.org/project/pdm>`__

   pex
       Bibliothek und Werkzeug zur Erzeugung von Python EXecutable
       (:file:`.pex`)-Dateien, die eigenständige Python-Umgebungen sind.
       .pex-Dateien sind Zip-Dateien mit ``#!/usr/bin/env python`` und einer
       speziellen :file:`__main__.py`-Datei, die das Deployment von
       Python-Applikationen stark vereinfachen können.

       `Docs <https://pex.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/pantsbuild/pex/>`__ |
       `PyPI <https://pypi.org/project/pex>`__

   pip
       Popular tool for installing Python packages included in new versions of
       Python.

       It provides the essential core functions for searching, downloading and
       installing packages from the :term:`Python Package Index` and other
       Python package directories, and can be integrated into a variety of
       development workflows via a command line interface (CLI).

       `Docs <https://pip.pypa.io/>`__ |
       `GitHub <https://github.com/pypa/pip>`__ |
       `PyPI <https://pypi.org/project/pip/>`__

   pip-tools
       Set of tools that can keep your builds deterministic and still up to date
       with new versions of your dependencies.

       `Docs <https://pip-tools.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/jazzband/pip-tools/>`__ |
       `PyPI <https://pypi.org/project/pip-tools/>`__

   Pipenv
       Pipenv bundles :term:`Pipfile`, :term:`pip` and :term:`virtualenv` into a
       single toolchain. It can automatically import the ``requirements.txt``
       and also check the environment for CVEs using `safety
       <https://pyup.io/safety>`_. Finally, it also facilitates the
       uninstallation of packages and their dependencies.

       `Docs <https://pipenv.pypa.io/en/latest/>`__ |
       `GitHub <https://github.com/pypa/pipenv>`__ |
       `PyPI <https://pypi.org/project/pipenv>`__

   Pipfile
   Pipfile.lock
       ``Pipfile`` and ``Pipfile.lock`` are a higher-level, application-oriented
       alternative to :term:`pip`’s ``requirements.txt`` file. The :pep:`PEP 508
       Environment Markers <508#environment-markers>` are also supported.

       `Docs <https://pipenv.pypa.io/en/latest/pipfile/>`__ |
       `GitHub <https://github.com/pypa/pipfile>`__

   pipx
       pipx helps you avoid dependency conflicts with other packages installed
       on the system.

       `Docs <https://pypa.github.io/pipx/>`__ |
       `GitHub <https://github.com/pypa/pipx>`__ |
       `PyPI <https://pypi.org/project/pipx/>`__

   piwheels
       Website and underlying software that fetches :term:`source distribution`
       packages from :term:`PyPI` and compiles them into binary :term:`wheels
       <wheel>` optimised for installation on Raspberry Pis.

       `Home <https://www.piwheels.org/>`__ |
       `Docs <https://piwheels.readthedocs.io/en/latest/index.html>`__ |
       `GitHub <https://github.com/piwheels/piwheels/>`__

   poetry
       Command line tool that takes care of installing and isolating
       dependencies, as well as building and packaging Python packages. It uses
       :term:`pyproject.toml` and provides its own dependency resolver instead
       of :term:`pip`’s resolver functionality.

       `Docs <https://python-poetry.org/>`__ |
       `GitHub <https://github.com/python-poetry/poetry>`__ |
       `PyPI <https://pypi.org/project/poetry/>`__

   pypi.org
       `pypi.org  <https://pypi.org/>`_ is the domain name for the :term:`Python
       Package Index` (:term:`PyPI`). In 2017 it replaced the old index domain
       name *pypi.python.org*. He is supported by :term:`warehouse`.

   pyproject.toml
       Tool-independent file for the specification of projects defined in
       :pep:`518`.

       `Docs
       <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`__

       .. seealso::
          * :ref:`pyproject-toml`

   Python Package Index
   PyPI
       :term:`pypi.org` is the standard package index for the Python community.
       All Python developers can use and distribute their distributions.

   Python Packaging Authority
   PyPA
       The `Python Packaging Authority <https://www.pypa.io/en/latest/>`_ is a
       working group that manages several software projects for packaging,
       distributing and installing Python libraries. However, the goals stated
       in `PyPA Goals <https://www.pypa.io/en/latest/future/>`_ were created
       during discussions around :pep:`516`, :pep:`517` and :pep:`518`, which
       allowed competing workflows with the :term:`pyproject.toml`-based build
       system that do not need to be interoperable.

   readme_renderer
       ``readme_renderer`` is a library used to render documentation from markup
       languages like Markdown or reStructuredText into HTML. You can use it to
       check if your package descriptions are displayed correctly on
       :term:`PyPI`.

       `GitHub <https://github.com/pypa/readme_renderer/>`__ |
       `PyPI <https://pypi.org/project/readme-renderer/>`__

   release
       The snapshot of a project at a specific point in time, identified by a
       version identifier.

       One release can result in several :term:`Built Distributions
       <built distribution>`.

   setuptools
       setuptools (and ``easy_install``) is a collection of improvements to the
       Python Distutils that make it easier to create and distribute Python
       distributions, especially those that have dependencies on other packages.

       `Docs <https://setuptools.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/pypa/setuptools>`__ |
       `PyPI <https://pypi.org/project/setuptools>`__

       .. seealso::
          `Packaging and distributing projects
          <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_

   scikit-build
       Build system generator for ``C``-, ``C++``-, ``Fortran``- and ``Cython``
       extensions that integrates :term:`setuptools`, :term:`wheel` and
       :term:`pip`. It uses ``CMake`` internally to provide better support for
       additional compilers, build systems, cross-compilation and finding
       dependencies and their associated build requirements. To speed up and
       parallelise the creation of large parallelisation, Ninja can also be
       installed. can be installed.

       `Docs <https://scikit-build.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/scikit-build/scikit-build/>`__ |
       `PyPI <https://pypi.org/project/scikit-build>`__

   shiv
       Command line utility for building Python zip apps as described in
       :pep:`441`, but additionally with all dependencies.

       `Docs <https://shiv.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/linkedin/shiv>`__ |
       `PyPI <https://pypi.org/project/shiv/>`__

   source distribution
   sdist
        A distribution format (typically generated using) ``python setup.py
        sdist``.

        It provides metadata and the essential source files required for
        installation with a tool like :term:`Pip` or for generating :term:`built
        distributions <built distribution>`.

   Spack
       Flexible package manager that supports multiple versions, configurations,
       platforms and compilers. Any number of versions of packages can co-exist
       on the same system. Spack is designed for rapid creation of
       high-performance scientific applications on clusters and supercomputers.

       `Docs <https://spack.readthedocs.io/en/latest/index.html>`__ |
       `GitHub <https://github.com/spack/spack>`__

       .. seealso::
          * :doc:`Python4DataScience:productive/envs/spack/index`

   trove-classifiers
       trove-classifiers are classifiers used in the :term:`Python Package
       Index` to systematically describe projects and make them easier to find.
       On the other hand, they are a package that contains a list of valid and
       obsolete classifiers that can be used for verification.

       `Docs <https://pypi.org/classifiers/>`__ |
       `GitHub <https://github.com/pypa/trove-classifiers>`__ |
       `PyPI <https://pypi.org/project/trove-classifiers/>`__

   twine
       Command line programme that passes programme files and metadata to a web
       API. This allows Python packages to be uploaded to the :term:`Python
       Package Index`.

       `Docs <https://twine.readthedocs.io/en/latest/>`__ |
       `GitHub <https://github.com/pypa/twine>`__ |
       `PyPI <https://pypi.org/project/twine>`__

   venv
       Package that is in the Python standard library as of Python ≥ 3.3 and is
       intended for creating :term:`virtual environments <virtual environment>`.

       `Docs <https://docs.python.org/3/library/venv.html>`_ |
       `GitHub <https://github.com/python/cpython/tree/main/Lib/venv>`__

   virtualenv
       Tool that uses the ``path`` command line environment variable to create
       isolated Python :term:`virtual environments <virtual environment>`,
       similar to :term:`venv`, but provides additional functionality for
       configuration, maintenance, duplication and debugging.

       As of version 20.22.0, virtualenv no longer supports Python versions 2.7,
       3.5 and 3.6.

   Virtual environment
       An isolated Python environment that allows packages to be installed for a
       specific application rather than system-wide.

       .. seealso::
          * :ref:`virtual-environments`
          * `Creating Virtual Environments
            <https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments>`_

   Warehouse
       The current code base that powers the :term:`Python Package Index`
       (:term:`PyPI`). It is hosted on :term:`pypi.org`.

       `Docs <https://warehouse.pypa.io/>`__ |
       `GitHub <https://github.com/pypa/warehouse>`__

   wheel
       Distribution format introduced with :pep:`427`. It is intended to replace
       the :term:`Egg` format and is supported by current :term:`pip`
       installations.

       C extensions can be provided as platform-specific wheels for Windows,
       macOS and Linux on :term:`PyPI`. This has the advantage for the users of
       the package that they don’t have to compile during the installation.

       `Home <https://pythonwheels.com/>`_ |
       `Docs <https://wheel.readthedocs.io/>`__ |
       :pep:`427` |
       `GitHub <https://github.com/pypa/wheel>`__ |
       `PyPI <https://pypi.org/project/wheel/>`__ |

       .. seealso::
          * :ref:`wheels`
