Apps
====

App projects are suitable for web servers, scripts and :abbr:`CLI (command line
interfaces)`. We can also create them with ``uv init --package``:

.. code-block:: console

   $ uv init --package myapp
   tree mypack -a
   myapp
   $ uv init --app myapp
   $  tree myapp -a
   myapp
   ├── .git
   │   └── ...
   ├── .gitignore
   ├── .python-version
   ├── README.md
   ├── pyproject.toml
   └── src
       └── myapp
           └── __init__.py

:file:`myapp/pyproject.toml`
    The :file:`pyproject.toml` file contains a ``scripts`` entry point
    ``myapp:main``:

    .. literalinclude:: myapp/pyproject.toml
       :caption: myapp/pyproject.toml
       :lines: 12-13

:file:`myapp/src/myapp/__init__.py`
    The module defines a CLI function :func:`main`:

    .. literalinclude:: myapp/src/myapp/__init__.py
       :caption: myapp/src/myapp/__init__.py

    It can be called up with ``uv run``:

    .. code-block:: console

       $ uv run mypack
       Hello from myapp!

    Alternatively, you can also build a :ref:`virtual environment <venv>` and
    then call :func:`main` from Python:

    .. code-block:: console

       $  uv add --dev .
       Resolved 1 package in 1ms
       Audited in 0.01ms
       $ uv run python
       >>> import myapp
       >>> myapp.main()
       Hello from myapp!

.. note::
   I strongly believe that a Python application should be properly packaged to
   enjoy the many benefits, such as

   * source management with :doc:`importlib <python3:library/importlib>`
   * executable scripts with ``project.scripts`` instead of attached
     :file:`scripts` folders
   * the benefits of :file:`src` layout with a common, documented and well
     understood structure.

.. _uv_lock:

:file:`uv.lock` file
--------------------

With ``uv add --dev .`` the :file:`uv.lock` file was also created alongside the
:file:`pyproject.toml` file. :file:`uv.lock` is a cross-platform lock file that
records the packages that are to be installed across all possible Python
features such as operating system, architecture and Python version.

Unlike :file:`pyproject.toml`, which specifies the general requirements of your
project, :file:`uv.lock` contains the exact resolved versions that are installed
in the project environment. This file should be checked into the :doc:`Git
<Python4DataScience:productive/git/index>` version control system to enable
consistent and reproducible installations on different computers.

.. literalinclude:: myapp/uv.lock
   :caption: myapp/uv.lock

:file:`uv.lock` is a human-readable
:doc:`Python4DataScience:data-processing/serialisation-formats/toml/index` file,
but is managed by ``uv`` and should not be edited manually.

.. note::
   If ``uv`` is to be integrated into other tools or workflows, you can export
   the content to the `requirements file format
   <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_ using
   :samp:`uv export --format requirements-txt > {CONSTRAINTS.TXT}`. Conversely,
   the :samp:`{CONSTRAINTS.TXT}` file created can then be used with ``uv pip
   install`` or other tools.

.. _update-uv-lock:

Aktualisieren von :file:`uv.lock`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:file:`uv.lock` is updated regularly when ``uv sync`` and ``uv run`` are called.

``--frozen``
    leaves the :file:`uv.lock file` unchanged.
``--no-sync``
    avoids updating the environment during ``uv run`` calls.
``--locked``
    ensures that the lock file matches the project metadata. If the lockfile is
    not up-to-date, an error message is issued instead of updating the lockfile.

By default, ``uv`` favours the locked versions of the packages when executing
``uv sync`` and ``uv lock``. Package versions are only changed if the dependency
conditions of the project exclude the previous, locked version.

``uv lock --upgrade``
    updates all packages.
:samp:`uv lock --upgrade-package {PACKAGE}=={VERSION}`
    upgrades a single package to a specific version.

You can also use the
:doc:`Python4DataScience:productive/git/advanced/hooks/pre-commit` to regularly
update your uv.lock file:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   - repo: https://github.com/astral-sh/uv-pre-commit
     rev: 0.4.24
     hooks:
       - id: uv-lock

Restrict platform and Python versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your project only supports a limited number of platforms or Python versions,
you can do this in the :file:`pyprojects.toml` file in compliance with
:pep:`508`, for example to restrict the :file:`uv.lock` file to macOS and Linux
only:

.. code-block:: toml

   [tool.uv]
   environments = [
       "sys_platform == 'darwin'",
       "sys_platform == 'linux'",
   ]
