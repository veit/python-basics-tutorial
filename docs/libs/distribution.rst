Creating a distribution package
===============================

:term:`Distribution Packages <Distribution Package>` are archives that can be
uploaded to a package index such as :term:`pypi.org` and installed with
:term:`pip`.

Some of the following commands require a new version of pip, so you should make
sure you have the latest version installed:


.. tab:: Linux/macOS

   .. code-block:: console

      $ python3 -m pip install --upgrade pip

.. tab:: Windows

   .. code-block:: ps1

      > python  -m pip install --upgrade pip

.. seealso::
   Packaging and distributing Python libraries with `setuptools
   <https://packaging.python.org/key_projects/#setuptools>`_:

   * `Packaging and distributing projects
     <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_

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

``pyproject.toml``
------------------

`PEP 517 <https://peps.python.org/pep-0517/>`_ and `PEP 518
<https://peps.python.org/pep-0518/>`_ brought extensible build backends,
isolated builds and `pyproject.toml
<https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_ in :doc:`jupyter-tutorial:data-processing/serialisation-formats/toml/index` format.

Among other things, ``pyproject.toml`` tells :term:`pip` and ``build`` which
backend tool to use to build distribution packages for your project. You can
choose from a number of backends, though this tutorial uses ``hatchling`` by
default.

A minimal yet functional :download:`dataprep/pyproject.toml` file will then look
like this, for example:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 1-3
   :lineno-start: 1

``build-system``
    defines a section describing the build system
``requires``
    defines a list of dependencies that must be installed for the build system
    to work, in our case ``hatchling``.

    .. note::
       Dependency version numbers should usually be written in the
       `requirements.txt
       <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_ file,
       not here.

``build-backend``
    identifies the entry point for the build-backend object as a dotted path.
    The ``hatchling`` backend object is available under ``hatchling.build``.

.. seealso::
   If you want to look at alternatives to ``setuptools``:

   * `setuptools <https://packaging.python.org/key_projects/#setuptools>`_
   * `flit <https://packaging.python.org/key_projects/#flit>`_
   * `poetry <https://github.com/python-poetry/poetry>`_
   * `pypackaging-native <https://pypackaging-native.github.io>`_

Metadata
~~~~~~~~

In ``pyproject.toml`` you can also specify metadata for your package, such as:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 5-
   :lineno-start: 5

``name``
    is the distribution name of your package. This can be any name as long as it
    contains only letters, numbers, ``.``, ``_`` and ``-``. It should also not
    already be assigned on the :term:`Python Package Index (PyPI)`.
``version``
    is the version of the package.

    .. seealso::
       * `PEP 440 – Version Identification and Dependency Specification
         <https://peps.python.org/pep-0440/>`_
       * `Semantic Versioning <https://semver.org>`_
       * `Calendar Versioning <https://calver.org>`_
       * `ZeroVer <https://0ver.org/>`_
       * `bump2version <https://pypi.org/project/bump2version/>`_

    Some build backends allow you to specify the version in other ways, such as
    by file or :doc:`jupyter-tutorial:productive/git/tag`.

``authors``
    is used to identify the authors of the package by name and email address.

    You can also list ``maintainers`` in the same format.

``description``
    is a short summary of the package, consisting of one sentence.
``readme``
    is a path to a file containing a detailed description of the package. This
    is displayed on the package details page on :term:`Python Package Index
    (PyPI)`. In this case, the description is loaded from ``README.rst``.
``requires-python``
    specifies the versions of Python that are supported by your project. This
    will cause installers like :term:`pip` to search through older versions of
    packages until they find one that has a matching Python version.
``classifiers``
    gives the :term:`Python Package Index (PyPI)` and :term:`pip` some
    additional metadata about your package. In this case, the package is only
    compatible with Python 3, is under the BSD licence and is OS independent.
    You should always at least specify the versions of Python your package runs
    under, under which licence your package is available and on which operating
    systems your package runs. You can find a complete list of classifiers at
    https://pypi.org/classifiers/.

    They also have a useful additional function: the :term:`Python Package
    Index (PyPI)` rejects packages with unknown classifiers, so that an
    accidental upload can be avoided.

    .. seealso::
       `Add invalid classifier for non open source license to avoid upload to…
       <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

``urls``
    lets you list any number of additional links that are displayed on the
    :term:`Python Package Index (PyPI)`. In general, this could lead to source
    code, documentation, task managers, :abbr:`etc (et cetera)`.

.. seealso::
   * `Declaring project metadata
     <https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata>`_
   * `PEP 345 – Metadata for Python Software Packages 1.2
     <https://peps.python.org/pep-0345/>`_

``src`` package
---------------

``dataprep``
    is the directory that contains the Python files. The name should match the
    project name to simplify configuration and be more recognisable to those
    installing the package.
``__init__.py``
    is required to import the directory as a package. The file should be empty.
``loaders.py``
    is an example of a module within the package that could contain the logic
    (functions, classes, constants, :abbr:`etc. (et cetera)`) of your package.

Other files
-----------

``setup.py``
~~~~~~~~~~~~

A minimal and yet functional :download:`dataprep/setup.py` looks like this, for
example:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 4-5, 9-12, 15-21,41
   :lineno-start: 1

`package_dir
<https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages>`_
points to the ``src`` directory, which can contain one or more packages. You can
then use setuptools’s `find_packages()
<https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages>`_ to find all packages in this directory.

.. note::
    ``find_packages()`` without ``src/`` directory would package all directories
    with a ``__init__.py`` file, so also ``tests/`` directories.

``MANIFEST.in``
~~~~~~~~~~~~~~~

The file contains all files and directories that are not already covered by
``packages`` or ``py_module``. It can look like this:
:download:`dataprep/MANIFEST.in`:

.. literalinclude:: dataprep/MANIFEST.in
   :linenos:

For more instructions in ``Manifest.in``, see `Creating a source distribution
<https://docs.python.org/3/distutils/commandref.html?highlight=manifest#creating-a-source-distribution-the-sdist-command>`__.

.. note::
    People often forget to update the ``Manifest.in`` file. To avoid this, you
    can use `check-manifest <https://pypi.org/project/check-manifest/>`_ in a
    pre-commit hook.

.. note::
    If you want files and directories from ``MANIFEST.in`` to be installed as
    well, for example if they are runtime-relevant data, you can specify this
    with ``include_package_data=True`` in your ``setup()`` call.

``setup.cfg``
~~~~~~~~~~~~~

This file is no longer needed, at least not for packaging. ``wheel`` nowadays
collects all required licence files automatically and ``setuptools`` can build
universal ``wheel`` packages with the ``options`` keyword argument, for example
``dataprep-0.1.0-py3-none-any.whl``.

``LICENSE``
~~~~~~~~~~~

You can find detailed information on this in the
:doc:`jupyter-tutorial:productive/licensing` section.

 ``CONTRIBUTORS.rst``
 ~~~~~~~~~~~~~~~~~~~~

.. seealso::
    * `All contributors <https://allcontributors.org/>`_

``README.rst``
~~~~~~~~~~~~~~

This file briefly tells those who are interested in the package how to use it.

.. seealso::
    * `Make a README <https://www.makeareadme.com>`_
    * `readme.so <https://readme.so>`_

If you write the document in :doc:`/document/rest`, you can also include the
contents as a detailed description in your package:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 4-5, 9-21,41

You can also include them in your :doc:`Sphinx documentation </document/start>`
with ``.. include:: ../../README.rst``.

``CHANGELOG.rst``
~~~~~~~~~~~~~~~~~

.. seealso::
    * `Keep a Changelog <https://keepachangelog.com/>`_
    * `Scriv <https://github.com/nedbat/scriv>`_
    * `changelog_manager <https://github.com/masukomi/changelog_manager>`_
    * `github-activity <https://github.com/executablebooks/github-activity>`_
    * `Dinghy <https://github.com/nedbat/dinghy>`_
    * `Python core-workflow blurb
      <https://github.com/python/core-workflow/tree/master/blurb>`_
    * `Release Drafter <https://github.com/release-drafter/release-drafter>`_
    * `towncrier <https://github.com/twisted/towncrier>`_

Build
-----

The next step is to create distribution packages for the package. These are
archives that can be uploaded to the :term:`Python Package Index (PyPI)` and
installed by :term:`pip`.

Make sure you have the latest version of ``build`` installed:

Now run the command in the same directory where ``pyproject.toml`` is located:

.. tab:: Linux/macOS

   .. code-block:: console

      $ cd /PATH/TO/YOUR/DISTRIBUTION_PACKAGE
      $ rm -rf build dist
      $ python3 -m build

.. tab:: Windows

   .. code-block:: ps1

      > cd /PATH/TO/YOUR/DISTRIBUTION_PACKAGE
      > rm -rf build dist
      > python -m build

The second line ensures that a clean build is created without artefacts from
previous builds. The third line should output a lot of text and create two files
in the ``dist`` directory when finished:

.. code-block:: console

   dist
   ├── dataprep-0.1.0-py3-none-any.whl
   └── dataprep-0.1.0.tar.gz

``dataprep-0.1.0-py3-none-any.whl``
    is a binary distribution format with the suffix ``..whl``., where the
    filename is composed as follows:

    ``dataprep``
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

``dataprep-0.1.0.tar.gz``
    is a source distribution.

.. seealso::
    The reference for the file names can be found in `File name convention
    <https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

    For more information on ``sdist``, see `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`__
    and `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

Testing
-------

.. tab:: Linux/macOS

   .. code-block:: console

      $ mkdir test_env
      $ cd test_env
      $ python3 -m venv .
      $ source bin/activate
      $ python -m pip install dist/dataprep-0.1.0-py3-none-any.whl
      Processing ./dist/dataprep-0.1.0-py3-none-any.whl
      Collecting pandas
        Using cached pandas-1.3.4-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
      …
      Successfully installed dataprep-0.1.0 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

.. tab:: Windows

   .. code-block:: console

      > mkdir test_env
      > cd test_env
      > python -m venv .
      > source bin/activate
      > python -m pip install dist/dataprep-0.1.0-py3-none-any.whl
      Processing ./dist/dataprep-0.1.0-py3-none-any.whl
      Collecting pandas
        Using cached pandas-1.3.4-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
      …
      Successfully installed dataprep-0.1.0 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

Anschließend könnt ihr die :term:`Wheel`-Datei überprüfen mit:

.. code-block:: console

    $ mkdir test_env
    $ cd !$
    cd test_env
    $ python3 -m venv .
    $ source bin/activate
    $ python -m pip install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1.0-py3-none-any.whl
    Collecting pandas
      Using cached pandas-1.3.4-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
    …
    Successfully installed dataprep-0.1.0 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

Then you can check the wheel with:

.. code-block:: console

    $ python -m pip install check-wheel-contents
    $ python check-wheel-contents dist/*.whl
    dist/dataprep-0.1.0-py3-none-any.whl: OK

Alternatively, you can also install the package:

.. code-block:: console

    $ python -m pip install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1-py3-none-any.whl
    Collecting pandas
    …
    Installing collected packages: numpy, pytz, six, python-dateutil, pandas, dataprep
    Successfully installed dataprep-0.1 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

You can then call Python and import your ``loaders`` module:

.. code-block:: python

    from dataprep import loaders

.. note::
    There are still many instructions that include a step to call ``setup.py``,
    for example ``python setup.py sdist``. However, this is now considered
    `anti-pattern <https://twitter.com/pganssle/status/1152695229105000453>`_ by
    parts of the `Python Packaging Authority (PyPA)
    <https://github.com/pypa/>`_.
