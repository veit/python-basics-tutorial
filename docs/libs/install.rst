Adding more Python libraries
============================

Although Python’ :doc:`batteries` philosophy means that you can already do a lot
with the default installation of Python, there will inevitably come a situation
where you need functionality that is not included in Python.

If you need a third-party module that is not pre-built for your platform, you
must use its source distribution. However, this causes two problems:

* To install the source distribution, you need to find and download it.
* Certain Python paths and authorisations of your system are expected.

Python offers :ref:`pip` as a current solution for both problems. ``pip`` tries
to find the module in the :term:`Python Package Index` (:term:`PyPI`), downloads
it and all dependencies and takes care of the installation. You can also call
:term:`pypi.org` directly and search for packages or filter the packages by
category.

.. warning::
   Never install anything with ``pip`` into the global Python, not even with the
   ``--user`` flag. Always use :ref:`venv`. This way you avoid contaminating
   your Python installation with libraries that you install and then forget
   about. Every time you need to do something new, you should create a new
   virtual environment. This will also avoid library conflicts between different
   projects.

.. tip::
   We recommend that you configure ``pip`` so that it is not possible to install
   Python packages globally. To do this, you can enter the following in your
   :file:`~/.config/pip/pip.conf`:

   .. code-block:: ini

      [global]
      require-virtualenv = true

.. _venv:

``venv``
--------

A virtual environment (``virtualenv``) is a self-contained directory structure
that contains both an installation of Python and the additional packages. Since
the entire Python environment is contained in this directory, the libraries and
modules installed there cannot collide with those in the main system or in other
virtual environments, so that different applications can use different versions
of Python and its packages. Creating and using a virtual environment is a
two-step process:

#. First we create a project directory and then the virtual environment in it:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ mkdir myproj
         $ cd myproj
         $ python3 -m venv .venv

   .. tab:: Windows

      .. code-block:: ps1

         > mkdir myproj
         > cd myproj
         > py -m venv .venv

   This creates the environment with Python and :term:`pip` in a directory
   called :samp:`.venv`.

#. You can then activate this environment so that the next time you call
   ``python``, it will use the Python from your new environment:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ . .venv/bin/activate

   .. tab:: Windows

      .. code-block:: ps1

         > .venv\Scripts\activate

#. Install Python packages only for for this virtual environment, for example,
   the popular ``pandas`` library:

   .. tab:: Linux/macOS

      .. code-block:: console

         (.venv) $ python -m pip install pandas

   .. tab:: Windows

      .. code-block:: ps1

         (.venv) > python.exe -m pip install pandas

#. If you want to finish your work on this project, you can deactivate the
   virtual environment again with

   .. tab:: Linux/macOS

      .. code-block:: console

         (.venv) $ deactivate

   .. tab:: Windows

      .. code-block:: ps1

         (.venv) > deactivate

.. seealso::
   * :doc:`python3:tutorial/venv`

.. _pip:

``pip``
-------

The basic syntax of ``pip`` is quite simple:

.. code-block:: console

   (.venv) $ python -m pip install pandas

If you want to specify a particular version of a package, you can simply append
the version numbers:

.. code-block:: console

   (.venv) $ python -m pip install pandas==2.2.2

or

.. code-block:: console

   (.venv) $ python -m pip install "pandas>=2"

Proxy server
~~~~~~~~~~~~

To install Python packages via a proxy server, you can enter the following:

:samp:`python -m pip install --proxy
http://{USER_NAME}{:{PASSWORD}}@{PROXYSERVER_NAME}:{PORT} {PKG_NAME}`

You can also save the proxy server permanently as an environment variable:

.. tab:: Linux

   for example in the :file:`~/.bashrc` with:

   .. code-block:: bash

      $ export HTTP_PROXY=http://{USER_NAME}:{PASSWORD}@{PROXYSERVER_NAME}:{PORT}

.. tab:: Windows

   Add the following line to the environment variables:

   .. code-block:: ps1

      > set HTTP_PROXY={PROXYSERVER_NAME}:{PORT}

Pinning …
~~~~~~~~~

… of Python
:::::::::::

In contrast to applications, our packages usually support more than one Python
version. Nevertheless, we usually add the current standard version in
:file:`.python-version` to :doc:`packages <../packs/distribution>` as well:

.. literalinclude:: ../../.python-version
   :caption: .python-version

The nice thing about this is that we can use the same file in GitHub Actions as
input for `setup-python <https://github.com/actions/setup-python>`_:

.. literalinclude:: ../../.github/workflows/ci.yml
   :caption: .github/workflows/ci.yml
   :lines: 14, 29-35, 37-40
   :emphasize-lines: 12

In our :doc:`Python4DataScience:productive/git/advanced/gitlab/ci-cd/index`
pipelines, however, we use ``requires-python`` from the :ref:`pyproject-toml`
file to build :doc:`Docker containers with the appropriate Python version
<Python4DataScience:productive/git/advanced/gitlab/ci-cd/docker>`.

… of packages
:::::::::::::

To ensure a stable environment, it is advisable to specify the exact versions of
the dependencies.

.. tip::
   In none of our library projects does so much happen that the :doc:`Git
   history  <Python4DataScience:productive/git/review>` should mainly consist of
   updates. We only restrict the version numbers to be used in the event of
   problems. For apps, however, we specify the version numbers.

To pin versions for our applications and maintain cross-platform lock files, we
usually use :ref:`uv`. ``uv`` also helps us to ensure :ref:`reproducible Python
environments <reproduce-virtual-env>`.

However, packages can also be pinned using pip≥26.1:

.. code-block::

   $ python -m pip install --upgrade pip
   $ python -m pip --version

:pep:`751` defined the format for the :file:`pylock.toml` file, which can be
generated using the following command, for example:

.. code-block:: console

   $ python -m pip lock -e . -o pylock.prod.toml

Alternatively, :file:`a pylock.toml` file can be generated from a
:file:`requirements.txt` file:

.. code-block:: console

   $ python -m pip lock -r requirements.txt -o pylock.prod.toml

.. warning::
   In both cases, however, only the packages for the current platform and Python
   version are specified.

.. tip::
   If ``pip`` is not the only tool available, the cross-platform output of ``uv
   export`` is the smoother option.

The packages specified in :samp:`pylock{.NAME}.toml` can then be installed in a
different environment using:

.. code-block:: console

   $ python -m pip install -r pylock.prod.toml --no-deps

``--no-deps``
    ensures that transitive dependencies are not resolved in addition to the
    :samp:`pylock{.NAME}.toml`.

.. seealso::
   * `pip lock <https://pip.pypa.io/en/stable/cli/pip_lock/>`_
   * `pylock.toml Specification
     <https://packaging.python.org/en/latest/specifications/pylock-toml/>`_

.. _uv:

``uv``
------

:term:`uv` simplifies the creation of an initial project structure and the
management of your dependencies.

.. note::
   Many coding agents typically use ``pip`` when installing packages or running
   scripts. We therefore need to configure them first to use ``uv``:

   .. code-block:: md
      :caption: AGENTS.md

      - Use `uv` to manage Python environments and dependencies.
      - Use `uv run` to execute Python scripts and commands.
      - Don't edit `pyproject.toml` directly. Instead, use `uv add` and `uv add --dev` to manage dependencies.

   .. seealso::
      * :ref:`agentic-software-engineering:uv`

Installation
~~~~~~~~~~~~

``uv`` does not depend on Python. Pre-compiled, standalone binaries can be
installed on Linux, macOS and Windows:

.. tab:: Linux/macOS

   .. code-block:: console

      $ curl -LsSf https://astral.sh/uv/install.sh | sh

.. tab:: Windows

   .. code-block:: ps1

      > powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

``uv``  updates itself regularly with this installation.

Automatic shell completion
~~~~~~~~~~~~~~~~~~~~~~~~~~

To activate automatic shell completion for ``uv`` commands, carry out one of the
following steps:

.. tab:: Linux/macOS

   Specify your shell, for example with ``echo $SHELL``, then execute one of the
   following commands:

   .. code-block:: console

      $ echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
      $ echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
      $ echo 'uv generate-shell-completion fish | source' >> ~/.config/fish/config.fish
      $ echo 'eval (uv generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv

.. tab:: Windows

   .. code-block:: ps1

      Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
      Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'

Then restart the shell or call up ``source`` with your shell configuration file.

Update
~~~~~~

You can easily update uv with:

.. code:: console

   $ uv self update
   info: Checking for updates...
   success: Upgraded uv from v0.8.12 to v0.8.13! https://github.com/astral-sh/uv/releases/tag/0.8.13

Python installation
~~~~~~~~~~~~~~~~~~~

The current Python version can be installed with ``uv python install``.
Alternatively, a specific version can be installed with :samp:`uv python install
{3.14}`. However, you can install not only older CPython versions, but also
`PyPy <https://pypy.org>`_ with :samp:`uv python install pypy@{3.14}` or
Free-threaded Python with :samp:`uv python install --python-preferenc
only-managed {3.14t}`. You can see the Python versions that are already
installed with ``uv python list``. You can call up an installed Python version
with :samp:`uv run --python {3.14} python`.

Create project structure
~~~~~~~~~~~~~~~~~~~~~~~~

Depending on whether you want to create a :doc:`library <../packs/distribution>`
or an :doc:`application <../packs/apps>`, ``uv`` can create a suitable project
structure.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Using ``uv sync --frozen`` you can install your project’s dependencies in the
exact variants specified in the :file:`uv.lock` file.

.. seealso::
   * :ref:`uv_lock`
   * :ref:`reproduce-virtual-env`

Using :samp:`uv pip install --pylock pylock{.NAME}.toml`, you can also install
dependencies from an existing :samp:`pylock{.NAME}.toml` file.

Adding dependencies
~~~~~~~~~~~~~~~~~~~

Using :samp:`uv add {PACKAGE}`, you can add further dependencies to your
project. This adds the package to the ``dependencies`` section of the
:file:`pyproject.toml` file and writes the exact variant to the :file:`uv.lock`
file.

.. _uv-audit:

Vulnerability and malware checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``uv audit`` is a new command introduced in uv≥0.11.19 that checks the
dependencies in your project for known vulnerabilities in the `OSV
<https://osv.dev>`_ database and ‘undesirable’ project statuses, such as
*deprecated*:

.. code-block:: console

   $ uv audit
   warning: `uv audit` is experimental and may change without warning. Pass `--preview-features audit-command` to disable this warning.
   Resolved 115 packages in 16ms
   Found 12 known vulnerabilities and no adverse project statuses in 114 packages

   Vulnerabilities:

   idna 3.12 has 1 known vulnerability:
   - GHSA-65pc-fj4g-8rjx: Internationalized Domain Names in Applications (IDNA): Specially crafted inputs to idna.encode() can bypass CVE-2024-3651 fix
     Fixed in: 3.15
     Advisory information: https://github.com/kjd/idna/security/advisories/GHSA-65pc-fj4g-8rjx
   …

``uv add``, ``uv sync``, and so on can now be run during every synchronisation
process to check for previously identified malware. This feature is not enabled
by default, but it can be easily enabled by setting  ``UV_MALWARE_CHECK=1`` in
the shell.

.. seealso::
   * `uv audit <https://docs.astral.sh/uv/reference/cli/#uv-audit>`_
   * `uv audit settings <https://docs.astral.sh/uv/reference/settings/#audit>`_
