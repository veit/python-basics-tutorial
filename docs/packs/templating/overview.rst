Overview
========

A minimal CookieCutter template looks like this:

.. code-block:: console

    cookiecutter-namespace-template/
    ├── {{ cookiecutter.project_name }}/  <--- Project template
    │   └── …
    └── cookiecutter.json                 <--- Prompts & default values

For jsonexample, the file ``cookiecutter.json`` can look like this:

.. code-block:: json

    {
      "full_name": "Veit Schiele",
      "email": "veit@example.org",
      "github_username": "veit",
      "project_name": "vsc.example",
      "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
      "namespace": "{{ cookiecutter.project_slug.split('.')[0] }}",
      "package_name": "{{ cookiecutter.project_slug.split('.')[1] }}",
      "project_short_description": "Python Namespace Package contains all you need to create a Python namespace package.",
      "pypi_username": "veit",
      "use_pytest": "y",
      "command_line_interface": ["Click", "No command-line interface"],
      "version": "0.1.0",
      "create_author_file": "y",
      "license": ["MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3", "Not open source"]
    }

In addition, any number of directories and files can be created.

As a result you will get the following file structure:

.. code-block:: console

    my.package/                            <--- Value corresponding to what you enter
    │                                          at the project_name prompt
    │
    └── …                                 <--- Files corresponding to those in your
                                               cookiecutter’s
                                               {{ cookiecutter.project_name }}/ directory
