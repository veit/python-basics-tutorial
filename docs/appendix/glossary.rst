Glossary
========

.. glossary::
   :sorted:

   Argument
       A value that is passed to a function. There are two types of arguments:

       Keyword argument
           an argument that is preceded by an identifier (for example ``name=``)
           in a function call or that is passed as a value in a dictionary
           preceded by ``**``.
       Position argument
           an argument that is not a keyword argument. Position arguments can be
           at the beginning of an argument list and/or passed as elements of an
           iteration preceded by ``*``.


   Constant
       Python has :term:`immutable` objects, but no constant variables.
       Variables refer to objects, but there is no way to prevent a new
       assignment from being made.

   Control flow
       Time sequence of the individual commands of a computer program.

       .. seealso::
          * :doc:`/control-flow/index`

   Decorator
       A function that returns another function, usually applied as a function
       transformation using ``@wrapper`` syntax. Common examples of decorators
       are :ref:`classmethod` and :ref:`staticmethod`.

       .. seealso::
          * :doc:`/functions/decorators`

   Docstring
       A :doc:`/types/strings/built-in-modules/string` literal that appears as
       the first expression in a class, function or module. It is recognised by
       the Python compiler and included in the ``__doc__`` attribute of the
       enclosing class, function or module.

       .. seealso::
          * :doc:`/document/sphinx/docstrings`

   Duck typing
       Programming style in which the type of an object is not examined to
       determine whether it has the correct interface, but instead the method or
       attribute is simply called.

           ‘If it looks like a duck, swims like a duck, and quacks like a duck,
           then it probably is a duck.’

       By emphasising interfaces rather than specific types, well-designed code
       improves its flexibility by allowing polymorphic substitution. Duck
       typing avoids tests with :class:`type` or :func:`isinstance` and
       typically uses :func:`hasattr` tests or :term:`EAFP` programming instead.

       .. seealso::
          * :ref:`duck-typing`

   EAFP
       Easier to ask for forgiveness than permission. This common Python style
       assumes the existence of valid keys or attributes and catches exceptions
       if this assumption proves false. It is characterised by many :term:`try`
       and :term:`except` statements. This technique is in contrast to the
       :term:`LBYL` style, which is common in many other languages such as C.

   Exception
   Exception handling
       An exception passes on certain programme states – usually error states –
       to other programme levels. It is a customisable form of :term:`assert`.

       .. seealso::
          * :doc:`/control-flow/exceptions`
          * `Logging exceptions
            <https://python-basics-tutorial.readthedocs.io/en/latest/logging/examples.html#Logging-exceptions>`_
          * :ref:`pytest_fail`
          * :class:`python3:Exception`

   F-string
       :doc:`String </types/strings/built-in-modules/string>` literal preceded
       by an ``f`` or ``F``.

       .. seealso::
          * :ref:`f-strings`
          * :pep:`498`

   Function
       A series of instructions that returns a value. It can also be passed
       zero or more arguments that can be used when executing the main part.

       .. seealso::
          * :doc:`/functions/index`

   Garbage collection
       Process of releasing memory when it is no longer in use.

       .. seealso::
          * :py:mod:`gc`

   Immutable
       An object that cannot be mutated. The value of an immutable object cannot
       change. :doc:`Tuples <../types/sequences-sets/tuples>` are examples of
       immutable objects.

   LBYL
       Look before you leap. With this style, the preconditions are explicitly
       checked before the call. This style is in contrast to the :term:`EAFP`
       approach and is characterised by the presence of many ``if`` statements.

   Method
       A :term:`function` that is defined within a class. If it is called as an
       attribute of an instance of this class, the method receives the instance
       object as its first :term:`argument` (which is normally called ``self``).

   Parameter
       :term:`Argument` of a :term:`function` (or :term:`method`) definition.

       .. seealso::
          * :doc:`/functions/params`

   Singleton object
       A singleton class can only create one instance of itself.
       :doc:`../types/none` is an example of a singleton class in Python.

   Zen of Python
       Listing of Python design principles and philosophies that are helpful for
       understanding and using the language. The list can be output by entering
       ``import this``.

   .. _start-packaging:

   build
       ``build`` is a :pep:`517`-compatible Python package builder. It offers a
       :abbr:`CLI (Command Line Interface)` for creating packages and a Python
       :abbr:`API (Application Programming Interface)`.

       .. seealso::
          * `Docs <https://build.pypa.io/en/stable/index.html>`__
          * `GitHub <https://github.com/pypa/build>`__
          * `PyPI <https://pypi.org/project/build>`__

   Built distribution
   bdist
       A structure of files and metadata that only need to be moved to the
       correct location on the target system during installation. :term:`wheel`
       is such a format, but not *distutil’s* :term:`source distribution`, which
       requires a build step.

   cibuildwheel
       :doc:`/packs/cibuildwheel` is a Python package that builds :term:`wheels
       <wheel>` for all common platforms and Python versions on most :term:`CI`
       systems.

       .. seealso::
          * :term:`multibuild`
          * `Docs <https://cibuildwheel.pypa.io/>`__
          * `GitHub <https://github.com/pypa/cibuildwheel>`__
          * `PyPI <https://pypi.org/project/cibuildwheel>`__

   conda
       Package management tool for the `Anaconda distribution
       <https://docs.anaconda.com/anaconda/index.html>`_. It is specifically
       aimed at the scientific community, especially Windows, where the
       installation of binary extensions is often difficult.

       Conda does not install packages from :term:`PyPI` and can only install
       from the official Continuum repositories or from `anaconda.org
       <https://anaconda.org/>`_ or local (for example intranet) package
       servers.

       .. note::
          :term:`pip` can be installed in conda and work side-by-side to manage
          distributions of :term:`PyPI`.

       .. seealso::
          * `Conda: Myths and Misconceptions
            <https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>`_
          * `Conda build variants
            <https://docs.conda.io/projects/conda-build/en/latest/resources/variants.html>`_
          * `Docs <https://docs.conda.io/en/latest/>`__
          * `GitHub <https://github.com/conda/conda>`__

   devpi
       `devpi <https://www.devpi.net/>`_ is a powerful :term:`PyPI`-compatible
       server and PyPI proxy cache with a command line tool to enable packaging,
       testing and publishing activities.

       .. seealso::
          * `Docs <https://devpi.net/docs/>`__
          * `GitHub <https://github.com/devpi/devpi>`__
          * `PyPI <https://pypi.org/project/devpi>`__

   Distribution package
       A versioned archive file containing Python :term:`packages <Import
       package>`, :term:`modules <Module>` and other resource files used to
       distribute a release.

   distutils
       Python standard library package that provides support for bootstrapping
       :term:`pip` into an existing Python installation or :term:`virtual
       environment`.

       .. seealso::
          * :doc:`Docs <python3:library/ensurepip>`
          * `GitHub <https://github.com/pypa/distutils>`__

   Egg
       A :term:`built distribution` format introduced by :term:`setuptools` and
       now replaced by :term:`wheel`. For more information, see `The Internal
       Structure of Python Eggs
       <https://setuptools.pypa.io/en/latest/deprecated/python_eggs.html>`_ and
       `Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_.

   enscons
       enscons is a Python packaging tool based on `SCons
       <https://scons.org/>`_. It builds :term:`pip`-compatible :term:`source
       distributions <Source distribution>` and :term:`wheels <wheel>` without
       using :term:`distutils` or :term:`setuptools`, including distributions
       with C extensions. enscons has a different architecture and philosophy
       than :term:`distutils`, as it adds Python packaging to a general build
       system. enscons can help you build :term:`sdists <sdist>` and
       :term:`wheels <wheel>`.

       .. seealso::
          * `GitHub <https://github.com/dholth/enscons>`__
          * `PyPI <https://pypi.org/project/enscons>`__

   Flit
       Flit provides an easy way to create pure Python packages and modules and
       upload them to the :term:`Python Package Index`. Flit can generate a
       configuration file to quickly set up a project, create a :term:`source
       distribution` and :term:`wheel`, and upload them to PyPI.

       Flit uses :term:`pyproject.toml` to configure a project. Flit does not
       rely on tools like :term:`setuptools` to create distributions or
       :term:`twine` to upload them to :term:`PyPI`.

       .. seealso::
          * `Docs <https://flit.pypa.io>`__
          * `GitHub <https://github.com/pypa/flit>`__
          * `PyPI <https://pypi.org/project/flit>`__

   Hatch
       Hatch is a command line tool that can be used to configure and version
       packages and to specify dependencies. The plugin system allows you to
       easily extend the functionalities.

       .. seealso::
          * `Docs <https://hatch.pypa.io/latest/>`__
          * `GitHub <https://github.com/pypa/hatch>`__
          * `PyPI <https://pypi.org/project/hatch>`__

   hatchling
       Build backend of :term:`Hatch`, which can also be used for publishing on
       the :term:`Python Package Index`.

   Import Package
       A Python module that can contain other modules or recursively other
       packages.

   maturin
       Formerly pyo3-pack, is a :pep:`621`-compatible build tool for
       :doc:`binary extensions <../packs/binary-extensions>` in Rust.

   meson-python
       Build backend that uses the `Meson <https://mesonbuild.com>`_ build
       system. It supports a variety of languages, including C, and is able to
       fulfil the requirements of most complex build configurations.

       .. seealso::
          * `Docs <https://mesonbuild.com/meson-python/>`__
          * `GitHub <https://github.com/mesonbuild/meson-python>`__
          * `PyPI <https://pypi.org/project/meson-python/>`__

   Module
       An object that serves as an organisational unit of Python code. Modules
       have a :doc:`namespace </oop/namespaces>` that contains any Python
       objects. They are loaded by importing them into Python.

       Python modules can exist in two different variants:

       Pure Module
           A module written in Python and contained in a single ``.py`` file
           (and possibly associated ``.pyc`` and/or ``.pyo`` files).

       Extension Module
           Usually included in a single dynamically loadable precompiled file,
           for example a common object file (``.so``).

       .. seealso::
          * :doc:`/libs/batteries`

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

       .. seealso::
          * `Docs <https://pdm.fming.dev/>`__
          * `GitHub <https://github.com/pdm-project/pdm/>`__
          * `PyPI <https://pypi.org/project/pdm>`__

   pex
       Library and tool for creating Python executable (:file:`.pex`) files,
       which are independent Python environments. :file:`.pex` files are zip files with #!/usr/bin/env python and a special __main__.py file, which can greatly simplify the deployment of Python applications.

       Bibliothek und Werkzeug zur Erzeugung von Python Executable
       (:file:`.pex`)-Dateien, die eigenständige Python-Umgebungen sind.
       .pex-Dateien sind Zip-Dateien mit ``#!/usr/bin/env python`` und einer
       speziellen :file:`__main__.py`-Datei, die das Deployment von
       Python-Applikationen stark vereinfachen können.

       .. seealso::
          * `Docs <https://docs.pex-tool.org/>`__
          * `GitHub <https://github.com/pex-tool/pex>`__
          * `PyPI <https://pypi.org/project/pex>`__

   pip
       Popular tool for installing Python packages that is included in new
       versions of Python.

       It provides the essential core functions for searching, downloading and
       installing packages from the :term:`Python Package Index` and other
       Python package directories and can be integrated into a variety of
       development workflows via a :abbr:`CLI (command line interface)`.

       .. seealso::
          * `Docs <https://pip.pypa.io/>`__
          * `GitHub <https://github.com/pypa/pip>`__
          * `PyPI <https://pypi.org/project/pip/>`__

   pip-tools
       Set of tools that can keep your builds deterministic and still keep up to
       date with new versions of your dependencies.

       .. seealso::
          * `Docs <https://pip-tools.readthedocs.io/en/latest/>`__
          * `GitHub <https://github.com/jazzband/pip-tools/>`__
          * `PyPI <https://pypi.org/project/pip-tools/>`__

   Pipenv
       Pipenv bundles :term:`Pipfile`, :term:`pip` and :term:`virtualenv` in a
       single toolchain. It can automatically import the
       :file:`requirements.txt` and also check the environment for CVEs using
       `safety <https://safetycli.com>`_. Finally, it also facilitates the
       uninstallation of packages and their dependencies.

       .. seealso::
          * `Docs <https://pipenv.pypa.io/en/latest/>`__
          * `GitHub <https://github.com/pypa/pipenv>`__
          * `PyPI <https://pypi.org/project/pipenv>`__

   Pipfile
   Pipfile.lock
       :file:`Pipfile` and :file:`Pipfile.lock` are a higher-level,
       application-orientated alternative to :term:`pip`’s
       :file:`requirements.txt` file. The :pep:`PEP 508 Environment Markers
       <508#environment-markers>` are also supported.

       .. seealso::
          * `Docs <https://pipenv.pypa.io/en/latest/pipfile.html>`__
          * `GitHub <https://github.com/pypa/pipfile>`__

   pipx
       pipx helps you to avoid dependency conflicts with other packages
       installed on the system.

       .. seealso::
          * `Docs <https://pipx.pypa.io/stable/>`__
          * `GitHub <https://github.com/pypa/pipx>`__
          * `PyPI <https://pypi.org/project/pipx/>`__

   piwheels
       Website and underlying software that fetches :term:`source distribution`
       packages from :term:`PyPI` and compiles them into binary :term:`wheels
       <wheel>` optimised for installation on Raspberry Pis.

       .. seealso::
          * `Home <https://www.piwheels.org/>`__
          * `Docs <https://piwheels.readthedocs.io/en/latest/index.html>`__
          * `GitHub <https://github.com/piwheels/piwheels/>`__

   poetry
       An all-in-one solution for pure Python projects. It replaces
       :term:`setuptools`, :term:`venv`/:term:`pipenv`, :term:`pip`,
       :term:`wheel` and :term:`twine`. However, it makes some poor default
       assumptions for libraries and the :term:`pyproject.toml` configuration is
       non-standard.

       .. seealso::
          * `Docs <https://python-poetry.org/>`__
          * `GitHub <https://github.com/python-poetry/poetry>`__
          * `PyPI <https://pypi.org/project/poetry/>`__

   pybind11
       This is :term:`setuptools`, but with a C++ extension and :term:`wheels
       <wheel>` generated by :term:`cibuildwheel`.

       .. seealso::
          * `Docs <https://pybind11.readthedocs.io/en/stable/>`__
          * `GitHub <https://github.com/pybind/pybind11>`__
          * `PyPI <https://pypi.org/project/pybind11/>`__

   pypi.org
       `pypi.org  <https://pypi.org/>`_ is the domain name for the :term:`Python
       Package Index` (:term:`PyPI`). It replaced the old index domain name
       ``pypi.python.org`` in 2017. It is supported by :term:`warehouse`.

   pyproject.toml
       Tool-independent file for specifying projects, which is defined in
       :pep:`518`.

       .. seealso::
          * :ref:`pyproject-toml`
          * `Docs
            <https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`__

   Python Package Index
   PyPI
       :term:`pypi.org` is the standard package index for the Python community.
       All Python developers can use and share their distributions.

   Python Packaging Authority
   PyPA
       The `Python Packaging Authority <https://www.pypa.io/en/latest/>`_ is a
       working group that manages several software projects for the packaging,
       distribution and installation of Python libraries. However, the goals
       stated in `PyPA Goals <https://www.pypa.io/en/latest/future/>`_ were
       created during the discussions around :pep:`516`, :pep:`517` and
       :pep:`518`, which allowed competing workflows with the
       :term:`pyproject.toml`-based build system that do not need to be
       interoperable.

   readme_renderer
       ``readme_renderer`` is a library that is used to render documentation
       from markup languages like Markdown or reStructuredText to HTML. You can
       use it to check whether your package descriptions are displayed correctly
       on :term:`PyPI`.

       .. seealso::
          * `GitHub <https://github.com/pypa/readme_renderer/>`__
          * `PyPI <https://pypi.org/project/readme-renderer/>`__

   Release
       The snapshot of a project at a specific point in time, characterised by a
       version identifier.

       A release can result in several :term:`built distributions <Built
       distribution>`.

   scikit-build
       Build system generator for ``C``, ``C++``, ``Fortran`` and ``Cython``
       extensions that integrates :term:`setuptools`, :term:`wheel` and
       :term:`pip`. It uses ``CMake`` internally to provide better support for
       additional compilers, build systems, cross-compilation and finding
       dependencies and their associated build requirements. To speed up and
       parallelise the creation of large projects, `Ninja
       <https://ninja-build.org>`_ can also be installed.

       .. seealso::
          * `Docs <https://scikit-build.readthedocs.io/en/latest/>`__
          * `GitHub <https://github.com/scikit-build/scikit-build>`__
          * `PyPI <https://pypi.org/project/scikit-build>`__

   setuptools
       setuptools are the classic build system, which is very powerful, but with
       a steep learning curve and high configuration effort. From version
       61.0.0, the setuptools also support :term:`pyproject.toml` files.

       .. seealso::
          * `Docs <https://setuptools.readthedocs.io/>`__
          * `GitHub <https://github.com/pypa/setuptools>`__
          * `PyPI <https://pypi.org/project/setuptools>`__
          * `Packaging and distributing projects
            <https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/>`_

   shiv
       Command line programme for creating Python zip apps as described in
       :pep:`441`, but with all additional dependencies.

       .. seealso::
          * `Docs <https://shiv.readthedocs.io/en/latest/>`__
          * `GitHub <https://github.com/linkedin/shiv>`__
          * `PyPI <https://pypi.org/project/shiv/>`__

   Source distribution
   sdist
       A distribution format (usually generated using ``python setup.py
       sdist``).

       It provides metadata and the essential source files required for
       installation with a tool such as :term:`Pip` or for generating
       :term:`built distributions <Built distribution>`.

   Spack
       Flexible package manager that supports multiple versions, configurations,
       platforms and compilers. Any number of versions of packages can coexist
       on the same system. Spack was developed for the rapid creation of
       high-performance scientific applications on clusters and supercomputers.

       .. seealso::
          * :doc:`Python4DataScience:productive/envs/spack/index`
          * `Docs <https://spack.readthedocs.io/en/latest/index.html>`__
          * `GitHub <https://github.com/spack/spack>`__

   trove-classifiers
       trove classifiers are classifiers that are used in the :term:`Python
       Package Index` to systematically describe projects and make them easier
       to find. On the other hand, they are a package that contains a list of
       valid and outdated classifiers that can be used for checking.

       .. seealso::
          * `Docs <https://pypi.org/classifiers/>`__
          * `GitHub <https://github.com/pypa/trove-classifiers>`__
          * `PyPI <https://pypi.org/project/trove-classifiers/>`__

   twine
       Command line programme that transfers programme files and metadata to a
       web :abbr:`API (Application Programming Interface)`. This allows Python
       packages to be uploaded to the :term:`Python Package Index`.

       .. seealso::
          * `Docs <https://twine.readthedocs.io/en/latest/>`__
          * `GitHub <https://github.com/pypa/twine>`__
          * `PyPI <https://pypi.org/project/twine>`__

   uv
       An extremely fast Python package and project manager written in `Rust
       <https://www.rust-lang.org>`_.

       uv greatly simplifies the development and deployment of Python projects:

       * :ref:`Installation <uv>`
       * :ref:`Create packages <uv-package-structure>` and publish them on
         :doc:`PyPI <../packs/publish>` or :doc:`GitLab <../packs/gitlab>`
       * :doc:`Developing applications <../packs/apps>`
       * Testing libraries with different :ref:`Python versions
         <various-python-versions>` and :ref:`tox_uv`
       * :ref:`Reproducing <reproduce-virtual-env>` and :ref:`updating
         <update-uv-lock>` the Python environment, if necessary also with a
         :doc:`Python4DataScience:productive/envs/uv/dependency-bot`
       * :doc:`Python4DataScience:productive/envs/uv/cicd`
       * :doc:`Python4DataScience:productive/envs/uv/docker`
       * Check vulnerabilities with :ref:`uv-secure <check-vulnerabilities>`

       .. seealso::
          * `Docs <https://docs.astral.sh/uv/>`__
          * `GitHub <https://github.com/astral-sh/uv>`__
          * `PyPI <https://pypi.org/project/uv/>`__

   venv
       Package that is part of the Python standard library from Python ≥ 3.3 and
       is intended for creating :term:`virtual environments <Virtual
       environment>`.

       .. seealso::
          * :doc:`Docs <python3:library/venv>`
          * `GitHub <https://github.com/python/cpython/tree/main/Lib/venv>`__

   virtualenv
       Tool that uses the ``path`` command line environment variable to create
       isolated Python :term:`virtual environments <Virtual environment>`,
       similar to :term:`venv`, but provides additional functionality for
       configuration, maintenance, duplication and troubleshooting.

       As of version 20.22.0, virtualenv no longer supports Python versions 2.7,
       3.5 and 3.6.

   Virtual environment
       An isolated Python environment that allows the installation of packages
       for a specific application instead of installing them system-wide.

       .. seealso::
          * :ref:`venv`
          * `Creating Virtual Environments
            <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments>`_

   Warehouse
       The current code base that drives the :term:`Python Package Index`
       (:term:`PyPI`). It is hosted on :term:`pypi.org`.

       .. seealso::
          * `Docs <https://warehouse.pypa.io/>`__
          * `GitHub <https://github.com/pypi/warehouse>`__

   wheel
       Distribution format that was introduced with :pep:`427`. It is intended
       to replace the :term:`Egg` format and is supported by current :term:`pip`
       installations.

       C extensions can be provided as platform-specific wheels for Windows,
       macOS and Linux on the :term:`PyPI`. This has the advantage for you that
       you do not have to compile the package when installing it.

       .. seealso::
          * `Home <https://pythonwheels.com/>`__
          * `Docs <https://wheel.readthedocs.io/>`__
          * :pep:`427`
          * `GitHub <https://github.com/pypa/wheel>`__
          * `PyPI <https://pypi.org/project/wheel/>`__

       .. seealso::
          * :ref:`wheels`

   whey
       Simple Python :term:`wheel` builder with automation options for
       :term:`trove-classifiers`.

   .. _end-packaging:

   .. _start-test-procedures:

   Static test procedures
       are used to check the source code, although this is not executed. They
       are divided into

       * :ref:`reviews <code_reviews>` and
       * `static program analysis
         <https://en.wikipedia.org/wiki/Static_program_analysis>`_

         There are various Python packages that can help you with static code
         analysis, including :doc:`Python4DataScience:productive/qa/flake8`,
         :doc:`Python4DataScience:productive/qa/pysa` and
         :doc:`Python4DataScience:productive/qa/wily`.

   Dynamic test procedures
       are used to find errors when executing the source code. A distinction is
       made between :term:`whitebox <Whitebox test>` and :term:`blackbox
       <Blackbox test>` tests.

   .. _end-test-procedures:

   .. _start-test:

   Whitebox test
       is developed with knowledge of the source code and the software
       structure.

       Various modules are available in Python:

       :doc:`/test/unittest`
           supports you in the automation of tests.
       :doc:`/test/mock`
           allows you to create and use mock objects.
       :doc:`../document/doctest`
           allows you to test tests written in Python :term:`docstrings
           <Docstring>`.
       :doc:`/test/tox`
           allows you to test in different environments.

   Blackbox test
       is developed without knowledge of the source code. In addition to
       :doc:`/test/unittest`, :doc:`/test/hypothesis` can also be used for such
       tests in Python.

   ``assert``
       A keyword that stops code execution if its argument is false.

   Continuous Integration
   CI
       Automatic checking of the creation and testing process on different
       platforms.

   Dummy
       Object that is passed around but never actually used. Normally dummies
       are only used to fill :term:`parameter` lists.

   ``except``
       Keyword used to intercept an :term:`exception` and handle it carefully.

   Fake
       Object that has an implementation that actually works, but usually takes
       a shortcut that makes it unsuitable for production.

   Integration test
       Tests that check whether the different parts of the software work
       together as expected.

   Mock
       Objects programmed with :term:`exceptions <exception>` that form a
       specification of the calls you are likely to receive.

       .. seealso::
          * `Mock object <https://en.wikipedia.org/wiki/Mock_object>`_

   pytest
       A Python package with test utilities.

       .. seealso::
          * :doc:`/test/pytest/index`

   Regression test
       Tests to protect against new errors or regressions that may occur as a
       result of new software and updates.

   Stubs
       provide ready-made responses to calls made during the test and usually
       do not react at all to anything that has not been programmed for the
       test.

   Test-driven development
   TDD
       A software development strategy in which the tests are written before the
       code.

   ``try``
       A keyword that protects a part of the code that can throw an
       :term:`exception`.

   .. _end-test:
