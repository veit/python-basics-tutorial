Creating a distribution package
===============================

:term:`Distribution Packages <Distribution Package>` are archives that can be
uploaded to a package index such as :term:`pypi.org` and installed with
:term:`pip`.

.. tip::
   `cusy seminar: Advanced Python
   <https://cusy.io/en/our-training-courses/advanced-python.html>`_

Structure
---------

A minimal distribution package can look like this, for example:

.. code-block:: console

    dataprep
    ├── pyproject.toml
    └── src
        └── dataprep
            ├── __init__.py
            └── loaders.py

.. _pyproject-toml:

:file:`pyproject.toml`
----------------------

:pep:`517` and :pep:`518` brought extensible build backends, isolated builds and
`pyproject.toml
<https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_ in
:doc:`Python4DataScience:data-processing/serialisation-formats/toml/index`
format.

Among other things, :file:`pyproject.toml` tells :term:`pip` and :term:`build`
which backend tool to use to build distribution packages for your project. You
can choose from a number of backends, though this tutorial uses ``hatchling`` by
default.

A minimal yet functional :download:`dataprep/pyproject.toml` file will then look
like this, for example:

.. code-block:: toml
   :linenos:
   :lineno-start: 1

   [build-system]
   requires = ["hatchling>=1.27"]
   build-backend = "hatchling.build"

``build-system``
    defines a section describing the build system
``requires``
    defines a list of dependencies that must be installed for the build system
    to work, in our case ``hatchling>=1.27`` for :pep:`639` support.

    .. note::
       Dependency version numbers should usually be written in the
       `constraints.txt
       <https://pip.pypa.io/en/latest/user_guide/#constraints-files>`_ file, not
       here.

``build-backend``
    identifies the entry point for the build-backend object as a dotted path.
    The ``hatchling`` backend object is available under ``hatchling.build``.

    .. note::
       However, for Python packages that contain binary extensions with
       ``Cython``, ``C``, ``C++``, ``Fortran`` or ``Rust``, the
       :term:`hatchling` backend is not suitable. One of the following backends
       should be used here:

       * :term:`setuptools`
       * :term:`scikit-build`
       * :term:`maturin`

       But that’s not all – there are other backends:

       * :term:`Flit`
       * :term:`whey`
       * :term:`poetry`
       * :term:`pybind11`
       * :term:`meson-python`

    .. seealso::
       * `pypackaging-native <https://pypackaging-native.github.io>`_

.. note::
   With `check-toml
   <https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#check-toml>`_,
   `pyproject-fmt
   <https://pyproject-fmt.readthedocs.io/en/latest/>`_ and `validate-pyproject
   <https://validate-pyproject.readthedocs.io/en/latest/>`_ you can format and
   check your :file:`pyproject.toml` file.

.. seealso::
   If you want to look at alternatives to ``hatchling``:

   * :term:`setuptools`
   * :term:`Flit`
   * `poetry <https://github.com/python-poetry/poetry>`_
   * `pypackaging-native <https://pypackaging-native.github.io>`_

Metadata
~~~~~~~~

In :file:`pyproject.toml` you can also specify metadata for your package, such
as:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 5-21, 23-25, 42-
   :lineno-start: 5

``name``
    is the distribution name of your package. This can be any name as long as it
    contains only letters, numbers, ``.``, ``_`` and ``-``. It should also not
    already be assigned on the :term:`Python Package Index` (:term:`PyPI`).
``version``
    is the version of the package.

    In our example, the version number has been set statically. However, there
    is also the possibility to specify the version dynamically, for example by a
    file:

    .. code-block:: toml

       [project]
       ...
       dynamic = ["version"]
       [tool.hatch.version]
       path = "src/dataprep/__about__.py"

    The default pattern looks for a variable called :samp:`__version__` or
    :samp:`VERSION`, which contains the version, optionally preceded by the
    lower case letter :samp:`v`. The default pattern is based on :pep:`440`.

    If this is not the way you want to store versions, you can define a
    different regular expression with the :samp:`pattern` option.

    .. seealso::
       * `Calendar Versioning <https://calver.org>`_
       * `ZeroVer <https://0ver.org/>`_

    However, there are other version scheme plug-ins, such as `hatch-semver
    <https://github.com/fleetingbytes/hatch-semver>`_ for `semantic Versioning
    <https://semver.org>`_.

    With the version source plugin `hatch-vcs
    <https://github.com/ofek/hatch-vcs>`_ you can also use
    :doc:`Python4DataScience:productive/git/tag`:

    .. code-block:: toml

       [build-system]
       requires = ["hatchling>=1.27", "hatch-vcs"]
       ...
       [tool.hatch.version]
       source = "vcs"
       raw-options = { local_scheme = "no-local-version" }

    The setuptools backend also allows dynamic versioning:

    .. code-block:: toml

       [build-system]
       requires = ["setuptools>=77.0", "setuptools-scm"]
       build-backend = "setuptools.build_meta"
       [project]
       ...
       dynamic = ["version"]
       [tool.setuptools.dynamic]
       version = {attr = "dataprep.VERSION"}

    If you would like to make this version available in your package, you can
    use the following code:

    .. code-block:: python
       :caption: src/dataprep/__init__.py

       import importlib.metadata

       try:
           __version__ = importlib.metadata.version(__name__)
       except importlib.metadata.PackageNotFoundError:
           __version__ = "0.1.dev0"  # Fallback for development mode

    .. tip::
       If the version is in several text files, the use of `Bump My Version
       <https://github.com/callowayproject/bump-my-version>`_ may be
       recommended.

       The configuration file :file:`.bumpversion.toml` can look like this, for
       example:

       .. code-block:: toml

          [tool.bumpversion]
          current_version = "0.1.0"
          parse = "(?P<major>\\d+)\\.(?P<minor>\\d+)\\.(?P<patch>\\d+)"
          serialize = ["{major}.{minor}.{patch}"]
          search = "{current_version}"
          replace = "{new_version}"
          regex = false
          ignore_missing_version = false
          tag = false
          sign_tags = false
          tag_name = "v{new_version}"
          tag_message = "Bump version: {current_version} → {new_version}"
          allow_dirty = false
          commit = false
          message = "Bump version: {current_version} → {new_version}"
          commit_args = ""

          [[tool.bumpversion.files]]
          filename = "src/dataprep/__init__.py"

          [[tool.bumpversion.files]]
          filename = "docs/conf.py"

    .. seealso::
       * `Configuring setuptools using pyproject.toml files: Dynamic Metadata
         <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata>`_

``authors``
    is used to identify the authors of the package by name and email address.

    You can also list ``maintainers`` in the same format.

``description``
    is a short summary of the package, consisting of one sentence.
``readme``
    is a path to a file containing a detailed description of the package. This
    is displayed on the package details page on :term:`Python Package Index`
    (:term:`PyPI`). In this case, the description is loaded from ``README.rst``.

.. _license-expression:

``license-expression``
    contains valid `SPDX license expressions
    <https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/>`_.

    .. seealso::
       * `License-Expression
         <https://packaging.python.org/en/latest/specifications/core-metadata/#license-expression>`_
       * `Add License-Expression field
         <https://peps.python.org/pep-0639/#add-license-expression-field>`_

``license-files``
    specifies a list of files containing licence information.

    .. seealso::
       * `License-File (multiple use)
         <https://packaging.python.org/en/latest/specifications/core-metadata/#license-file-multiple-use>`_

``requires-python``
    specifies the versions of Python that are supported by your project. This
    will cause installers like :term:`pip` to search through older versions of
    packages until they find one that has a matching Python version.
``classifiers``
    gives the :term:`Python Package Index` (:term:`PyPI`) and :term:`pip` some
    additional metadata about your package. In this case, the package is only
    compatible with Python 3, is under the BSD licence and is OS independent.
    You should always at least specify the versions of Python your package runs
    under, under which licence your package is available and on which operating
    systems your package runs. You can find a complete list of classifiers at
    https://pypi.org/classifiers/.

    They also have a useful additional feature: to prevent a package from being
    uploaded to :term:`PyPI`, use the special classifier ``"Private :: Do Not
    Upload"``. :term:`PyPI` will always reject packages whose classifier starts
    with ``"Private ::"``.

``dependencies``
    specifies the dependencies for your package in an array.

    .. seealso::
       :pep:`631`

``urls``
    lets you list any number of additional links that are displayed on the
    :term:`Python Package Index` (:term:`PyPI`). In general, this could lead to
    source code, documentation, task managers, :abbr:`etc (et cetera)`.

.. error::
   If you receive the error in uv: :samp:`error: No \`project\` table found in:
   \`{/PATH/TO/}pyproject.toml\``, you probably haven’t defined a ``[project]``
   section. This can occur in repositories that only use the
   :file:`pyproject.toml` file to configure tools such as Black and Ruff, but
   do not define the project itself.

   To resolve the issue, you can insert a ``[project]`` section that must
   contain at least  ``name`` and ``version``. Alternatively, you can also use
   ``uv run`` with the ``--no-project`` option.

.. seealso::
   * `Declaring project metadata
     <https://packaging.python.org/en/latest/specifications/pyproject-toml/#declaring-project-metadata-the-project-table>`_
   * :pep:`345`

Dependency groups
~~~~~~~~~~~~~~~~~

``dependency-groups``
    allows you to specify dependency groups for your package. You can also
    distinguish between different sets:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 26-36
   :lineno-start: 26

Recursive dependency groups are also possible. For example, for ``dev`` you can
take over all dependencies from ``docs`` and ``test`` in addition to
``pre-commit``:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 37-41
   :lineno-start: 37

You can install these dependency groups, for example with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ cd /PATH/TO/YOUR/DISTRIBUTION_PACKAGE
      $ python3 -m venv .venv
      $ . .venv/bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install --group dev

.. tab:: Windows

   .. code-block:: ps1

      > cd C:\PATH\TO\YOUR\DISTRIBUTION_PACKAGE
      > python3 -m venv .venv
      > .venv\Scripts\activate.bat
      > python -m pip install --upgrade pip
      > python -m pip install --group dev

.. seealso::
   * :pep:`735`
   * `Dependency Groups
     <https://packaging.python.org/en/latest/specifications/dependency-groups/>`_

:file:`src` package
-------------------

When you create a new package, you shouldn’t use a flat layout but the
:file:`src` layout, which is also recommended in `Packaging Python Projects
<https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_ of the
:term:`PyPA`. A major advantage of this layout is that tests are run with the
installed version of your package and not with the files in your working
directory.

.. seealso::
   * Hynek Schlawack: `Testing & Packaging
     <https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html>`_

.. note::
   In Python ≥ 3.11 :envvar:`PYTHONSAFEPATH` can be used to ensure that the
   installed packages are used first.

:file:`dataprep`
    is the directory that contains the Python files. The name should match the
    project name to simplify configuration and be more recognisable to those
    installing the package.
:file:`__init__.py`
    is required to import the directory as a package. This allows you to import
    the following:

    .. code-block:: python

       import dataprep.loaders

    or

    .. code-block:: python

       from dataprep import loaders

    Although :file:`__init__.py` files are often empty, they can also contain
    code.

    .. seealso::
       * :ref:`python3:tut-packages`

:file:`loaders.py`
    is an example of a module within the package that could contain the logic
    (functions, classes, variables, :abbr:`etc. (et cetera)`) of your package.

Other files
-----------

:file:`CONTRIBUTORS.rst`
~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::
    * `All contributors <https://allcontributors.org/>`_

:file:`LICENSE`
~~~~~~~~~~~~~~~

You can find detailed information on this in the
:doc:`Python4DataScience:productive/licensing` section.

:file:`README.rst`
~~~~~~~~~~~~~~~~~~

This file briefly tells those who are interested in the package how to use it.

.. seealso::
    * `Make a README <https://www.makeareadme.com>`_
    * `readme.so <https://readme.so>`_

If you write the document in :doc:`/document/sphinx/rest`, you can also include
the contents as a detailed description in your package:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lineno-start: 5
   :lines: 5, 12

You can also include them in your :doc:`Sphinx documentation
</document/sphinx/start>` with ``.. include:: ../../README.rst``.

:file:`CHANGELOG.rst`
~~~~~~~~~~~~~~~~~~~~~

.. seealso::
    * `Keep a Changelog <https://keepachangelog.com/>`_
    * `Scriv <https://github.com/nedbat/scriv>`_
    * `changelog_manager <https://github.com/masukomi/changelog_manager>`_
    * `github-activity <https://github.com/executablebooks/github-activity>`_
    * `Dinghy <https://github.com/nedbat/dinghy>`_
    * `Python core-workflow blurb
      <https://github.com/python/core-workflow/tree/main/blurb>`_
    * `Release Drafter <https://github.com/release-drafter/release-drafter>`_
    * `towncrier <https://github.com/twisted/towncrier>`_

Historical files or files needed for binary extensions
------------------------------------------------------

Before the :file:`pyproject.toml` file introduced with :pep:`518` became the
standard, ``setuptools`` required :file:`setup.py`, :file:`setup.cfg` and
:file:`MANIFEST.in`. Today, however, these files are only needed for
:doc:`binary extensions <binary-extensions>` at best.

If you want to replace these files in your packages, you can do so with ``hatch
new --init`` or `ini2toml
<https://ini2toml.readthedocs.io/en/latest/setuptools_pep621.html>`_.

:file:`setup.py`
~~~~~~~~~~~~~~~~

A minimal and yet functional :download:`dataprep/setup.py` can look like this,
for example:

.. literalinclude:: dataprep/setup.py
   :language: python
   :linenos:

`package_dir
<https://docs.python.org/3.11/distutils/setupscript.html#listing-whole-packages>`_
points to the ``src`` directory, which can contain one or more packages. You can
then use setuptools’s `find_packages()
<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#finding-simple-packages>`_
to find all packages in this directory.

.. note::
    ``find_packages()`` without ``src/`` directory would package all directories
    with a ``__init__.py`` file, so also ``tests/`` directories.

:file:`setup.cfg`
~~~~~~~~~~~~~~~~~

This file is no longer needed, at least not for packaging. ``wheel`` nowadays
collects all required licence files automatically and ``setuptools`` can build
universal ``wheel`` packages with the ``options`` keyword argument, for example
:file:`dataprep-0.1.0-py3-none-any.whl`.

.. _manifest-in:

:file:`MANIFEST.in`
~~~~~~~~~~~~~~~~~~~

The file contains all files and directories that are not already covered by
``packages`` or ``py_module``. It can look like this:
:download:`dataprep/MANIFEST.in`:

.. literalinclude:: dataprep/MANIFEST.in
   :linenos:

For more instructions in :file:`Manifest.in`, see `MANIFEST.in commands
<https://packaging.python.org/en/latest/guides/using-manifest-in/>`__.

.. note::
   People often forget to update the :file:`Manifest.in` file. To avoid this,
   you can use `check-manifest <https://pypi.org/project/check-manifest/>`_ in a
   pre-commit hook.

.. note::
   If you want files and directories from :file:`MANIFEST.in` to be installed as
   well, for example if they are runtime-relevant data, you can specify this
   with ``include_package_data=True`` in your :func:`setup` call.

.. _uv-package-structure:

Create package structure
------------------------

With :samp:`uv init --package {MYPACK}` you can easily create an initial file
structure for packages.

.. code-block:: console

   $ uv init --package mypack
   $  tree mypack -a
   mypack
   ├── .git
   │   └── ...
   ├── .gitignore
   ├── .python-version
   ├── README.md
   ├── pyproject.toml
   └── src
       └── mypack
           └── __init__.py

:file:`.python-version`
   specifies which Python version should be used for developing the project.

   .. error::
      If you receive the following error message: error: :samp:`error: The
      Python request from \`.python-version\` resolved to Python {U.V.W}, which
      is incompatible with the project's Python requirement: \`>={X.Y}\`. Use
      \`uv python pin\` to update the \`.python-version\` file to a compatible
      version.`, this indicates a conflict between the version specified in the
      :file:`.python-version` file and the ``requires-python`` specification in
      the :file:`pyproject.toml` file. You now have three different options:

      * Update your :file:`.python-version` file with :samp:`uv python pin
        {X.Y.Z}`.
      * Override the Python version for a single command with  :samp:`uv run
        --python {X.Y} {COMMAND}`.
      * Update ``requires-python``.

:file:`mypack/pyproject.toml`
    The file :file:`pyproject.toml` contains a ``scripts`` entry point
    ``mypack:main``:

    .. literalinclude:: mypack/pyproject.toml
       :caption: mypack/pyproject.toml
       :emphasize-lines: 12-13

:file:`mypack/src/mypack/__init__.py`
    The module defines a CLI function :func:`main`:

    .. literalinclude:: mypack/src/mypack/__init__.py
       :caption: mypack/src/mypack/__init__.py

    It can be called with ``uv run``:

    .. code-block:: console

       $ uv run mypack
       Hello from mypack!

    .. note::
       If necessary, ``uv run`` creates a :ref:`virtual Python environment
       <venv>` in the :file:`.venv` folder before :func:`main` is executed.

.. _uv-build:

Build
-----

The next step is to create distribution packages for the package. These are
archives that can be uploaded to the :term:`Python Package Index` (:term:`PyPI`)
and installed by :term:`pip`. Now execute the command in the same directory
where :file:`pyproject.toml` is located:

.. tab:: Linux/macOS

   .. code-block:: console

      $ uv build
      Building source distribution...
      Building wheel from source distribution...
        Successfully built dist/mypack-0.1.0.tar.gz and dist/mypack-0.1.0-py3-none-any.whl

.. tab:: Windows

   .. code-block:: ps1

      > uv build
      Building source distribution...
      Building wheel from source distribution...
        Successfully built dist/mypack-0.1.0.tar.gz and dist/mypack-0.1.0-py3-none-any.whl

:file:`dist/mypack-0.1.0-py3-none-any.whl`
    is a build distribution. :term:`pip` prefers to install build distributions
    and only uses the source distributions if no suitable build distribution is
    available. You should always upload a source distribution and provide build
    distributions for the platforms with which your project is compatible. In
    this case, our example package is compatible with Python on every platform,
    so only one build distribution is required:

    ``mypack``
        is the normalised package name
    ``0.1.0``
        is the version of the distribution package
    ``py3``
        specifies the Python version and, if applicable, the C-`ABI
        <https://en.wikipedia.org/wiki/Application_binary_interface>`_
    ``none``
        specifies whether the :term:`Wheel` package is suitable for any OS or
        only specific ones
    ``any``
        ``any`` is suitable for any processor architecture, ``x86_64`` on the
        other hand only for chips with the x86 instruction set and a 64-bit
        architecture

    .. seealso::
       * :pep:`427`

:file:`mypack-0.1.0.tar.gz`
    is a :term:`source distribution`

.. seealso::
   * `Core metadata specifications
     <https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata>`_
   * `PyPA specifications
     <https://packaging.python.org/en/latest/specifications/>`_

Testing
-------

You can then check the :term:`Wheel` file with:

.. code-block:: console

   $ uv add --dev check-wheel-contents
   Resolved 17 packages in 8ms
      Built mypack @ file:///Users/veit/sandbox/mypack
   Prepared 1 package in 442ms
   Uninstalled 1 package in 0.89ms
   Installed 10 packages in 5ms
    + annotated-types==0.7.0
    + attrs==24.2.0
    + check-wheel-contents==0.6.0
    + click==8.1.7
    ~ mypack==0.1.0 (from file:///Users/veit/sandbox/mypack)
    + packaging==24.1
    + pydantic==2.9.2
    + pydantic-core==2.23.4
    + typing-extensions==4.12.2
    + wheel-filename==1.4.1
   $ uv run check-wheel-contents dist/*.whl
   dist/dataprep-0.1.0-py3-none-any.whl: OK

Alternatively, you can also install the package in a new project, for example in
:samp:`myapp`:

.. code-block:: console

   $ uv init --app myapp
   $ cd myapp
   $ uv add ../mypack/dist/mypack-0.1.0-py3-none-any.whl
   Resolved 8 packages in 130ms
   Installed 1 package in 3ms
    + mypack==0.1.0 (from file:///Users/veit/sandbox/mypack/dist/mypack-0.1.0-py3-none-any.whl)

You can then call ``mypack`` with ``uv run``:

.. code-block:: console

   $ uv run mypack
   Hello from mypack!

.. seealso::
   * `Troubleshooting build failures
   <https://docs.astral.sh/uv/reference/troubleshooting/build-failures/>`_

.. note::
   There are still many instructions that include a step to call
   :file:`setup.py`, for example :samp:`python setup.py sdist`. However, this is
   now considered `anti-pattern
   <https://x.com/pganssle/status/1152695229105000453>`_ by parts of the
   `Python Packaging Authority (PyPA) <https://github.com/pypa/>`_.

Checks
------

* If you want to create a task management package that writes the tasks to a
  database and provides them via a Python :abbr:`API (Application Programming
  Interface)` and a command line interface (:abbr:`CLI (Command-Line
  Interface)`), how would you structure the files?

* Think about how you want to fulfil the above tasks. Which libraries and
  modules can you think of that could fulfil this task? Sketch the code for the
  modules of the Python API, the command line interface and the database
  connection.
