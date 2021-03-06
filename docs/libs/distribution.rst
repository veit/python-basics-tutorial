Creating a distribution package
===============================

:term:`Distribution Packages <Distribution Package>` are archives that can be
uploaded to a package index and installed with :term:`Pip`.

Structure
---------

A minimal distribution package can look like this, for example:

.. code-block:: console

    dataprep
    ├── setup.py
    └── src
        └── dataprep
            ├── __init__.py
            └── loaders.py

``setup.py``
------------

A minimal and yet functional :download:`dataprep/setup.py` then looks like this,
for example:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 2,4-5,9-12,15-21,41-
   :lineno-start: 1

``src`` package
---------------

`package_dir
<https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages>`_
points to the ``src`` directory, which can contain one or more packages. You can
then use setuptools’s `find_packages()
<https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages>`_ to find all packages in this directory.

.. note::
    ``find_packages()`` without ``src/`` directory would package all directories
    with a ``__init__.py`` file, so also ``tests/`` directories.

``version``
-----------

There are various possibilities for ``version``, which are described in `PEP
0440 <https://www.python.org/dev/peps/pep-0440/>`_.

.. seealso::
    * `Semantic Versioning <https://semver.org>`_
    * `Calendar Versioning <https://calver.org>`_
    * `ZeroVer <https://0ver.org/>`_
    * `bump2version <https://pypi.org/project/bump2version/>`_
    * `Git Tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_

``classifiers``
---------------

With `classifiers <https://pypi.org/classifiers/>`_, suitable filters can be
created on the :term:`Python Package Index (PyPI)`:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 22-38
   :lineno-start: 16

Furthermore, PyPI has a useful additional function: it rejects unknown
classifiers, so that an accidental upload can be avoided.

.. seealso::
    `Add invalid classifier for non open source license to avoid upload to…
    <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

Dependencies
------------

Dependencies are specified with ``install_requires``:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 39
   :lineno-start: 32

.. note::
    Version numbers of dependencies should usually not be written in the
    ``setup.py`` file but in the `requirements.txt
    <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_ file.

.. seealso::
    `setup.py vs requirements.txt
    <https://caremad.io/posts/2013/07/setup-vs-requirement/>`_

Other files
-----------

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

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

`PEP 517 <https://peps.python.org/pep-0517/>`_ and `PEP 518
<https://peps.python.org/pep-0518/>`_ brought extensible build backends,
isolated builds and `pyproject.toml
<https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_. The
file uses the :doc:`jupyter-tutorial:data-processing/serialisation-formats/toml`
format and since we use ``setuptools``, the file should look like this or
something similar:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 1-4,6-
   :linenos:

``build-system``
    defines a section that describes the build system
``requires``
    defines a list of dependencies that must be installed for the build system
    to work. A setuptools build system requires ``setuptools`` and ``wheel``.
``build-backend``
    identifies the entry point for the build-backend object as a dotted path.
    The setuptools backend object is available at ``setuptools.build_meta``.

``LICENSE``
~~~~~~~~~~~

You can find detailed information on this in the
:doc:`jupyter-tutorial:productive/licensing` section.

``README.rst``
~~~~~~~~~~~~~~

This file briefly tells those who are interested in the package how to use it.
If you write the document in :doc:`/document/rest`, you can also include the
contents as a detailed description in your package:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 1,4-9,13-14,41

You can also include them in your :doc:`Sphinx documentation </document/start>`
with ``.. include:: ../../README.rst``.

``CHANGELOG.rst``
~~~~~~~~~~~~~~~~~

.. seealso::
   * `Keep a Changelog <https://keepachangelog.com>`_
   * `scriv <https://pypi.org/project/scriv/>`_

Build
-----

Changes to the directory in which the ``setup.py`` file is located.

.. code-block:: console

    $ pip install build
    $ cd /path/to/your/distribution_package
    $ rm -rf build dist
    $ python -m build .


The third line ensures that a clean build is created without artefacts from
previous builds. The second line builds an ``sdist`` archive on Linux/macOS as a
zipped tar file (``.tar.gz``) and on Windows a ZIP file and a ``bdist_wheel``
archive with ``.whl`` in the ``dist`` directory.

This command should create the following two files for our distribution package:

    dist/
      dataprep-0.1.0-py3-none-any.whl
      dataprep-0.1.0.tar.gz

``sdist``
    with ``dataprep-0.1.0.tar.gz`` the sources were made available in a
    distribution package.
``wheel``
    is a binary distribution format with the suffix ``..whl``., where the
    filename is composed as follows:

    ``dataprep``
        is the normalised package name
    ``0.1.0``
        is the version of the distribution package
    ``py3``
        specifies the Python version and, if applicable, the C-`ABI
        <https://en.wikipedia.org/wiki/Application_binary_interface>`_
    ``none``, ``macosx_10_9``
        specifies whether the wheel package is suitable for any OS or only
        specific ones
    ``any``,  ``x86_64``
        ``any`` is suitable for any processor architecture, ``x86_64`` on the
        other hand only for chips with the x86 instruction set and a 64-bit
        architecture

.. seealso::
    The reference for the file names can be found in `File name convention
    <https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

    For more information on ``sdist``, see `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`__
    and `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

Testing
-------

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

You can then call Python and import your loaders module:

.. code-block:: python

    from dataprep import loaders

.. note::
    There are still many instructions that include a step to call ``setup.py``,
    for example ``python setup.py sdist``. However, this is now considered
    `anti-pattern <https://twitter.com/pganssle/status/1152695229105000453>`_ by
    parts of the `Python Packaging Authority (PyPA)
    <https://github.com/pypa/>`_.

.. seealso::

    for packaging and distributing Python libraries with `setuptools
    <https://packaging.python.org/key_projects/#setuptools>`_: `Packaging and
    distributing projects
    <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_

    If you want to look at alternatives to ``setuptools``:

    * `flit <https://packaging.python.org/key_projects/#flit>`_
    * `hatch <https://github.com/ofek/hatch>`_
    * `poetry <https://github.com/python-poetry/poetry>`_
