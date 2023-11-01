Plugins
=======

As powerful as pytest is, it can do even more when we add plugins. The pytest
codebase is designed to allow customisation and extensions, and there are hooks
that allow changes and improvements through plugins.

You may be surprised to find that you have already written some plugins if you
have worked through the previous sections. Every time you add fixtures or hook
functions to a project’s :file:`conftest.py` file, you are creating a local
plugin. It’s just a little extra work to turn these :file:`conftest.py` files
into installable plugins that you can share between projects, with other people,
or with the world.

But first, let’s start with where you can find third-party plugins. There are
quite a few plugins out there, so there’s a good chance that any changes you
want to make to pytest have already been written.

Finding plugins
---------------

You can find third-party pytest plugins in various places, for example the
:doc:`pytest documentation <pytest:reference/plugin_list>` contains an
alphabetical list of plugins from :term:`pypi.org`. You can also search pypi.org
itself, for `pytest <https://pypi.org/search/?q=pytest>`_ or for the `pytest
framework <https://pypi.org/search/?q=&c=Framework+%3A%3A+Pytest>`_. Finally,
many popular pytest plugins can also be found in `pytest-dev
<https://github.com/pytest-dev>`_ on GitHub.

Installing plugins
------------------

Like other Python packages, pytest plugins can be easily installed with
:term:`pip`: :samp:`python -m pip install {pytest-cov}`.

Plugins for …
-------------

… modified test sequences
~~~~~~~~~~~~~~~~~~~~~~~~~

pytest usually executes our tests in a predictable order. For a directory of
test files, pytest executes each file in alphabetical order. Within each file,
each test is executed in the order in which it appears in the file. However, it
can sometimes be useful to change this order. The following plugins change the
usual sequence of a test:

`pytest-xdist <https://pypi.org/project/pytest-xdist/>`_
    executes tests in parallel, either with several CPUs on one machine or
    several remote machines.
`pytest-rerunfailures <https://pypi.org/project/pytest-rerunfailures/>`_
    re-executes failed tests and is particularly helpful in the case of faulty
    tests.
`pytest-repeat <https://pypi.org/project/pytest-repeat/>`_
    makes it easy to repeat one or more tests.
`pytest-order <https://pypi.org/project/pytest-order/>`_
    enables the order to be defined using :doc:`markers`.
`pytest-randomly <https://pypi.org/project/pytest-randomly/>`_
    runs the tests in random order, first by file, then by class, then by test
    file.

… modified output
~~~~~~~~~~~~~~~~~

The normal pytest output mainly shows dots for passed tests and characters for
other output. If you pass ``-v``, you will see a list of test names with the
result. However, there are plugins that change the output even further:

`pytest-instafail <https://pypi.org/project/pytest-instafail/>`_
    adds a ``--instafail`` option that reports tracebacks and output from failed
    tests immediately after the failure. Normally, pytest reports tracebacks and
    output from failed tests only after all tests have completed.
`pytest-sugar <https://pypi.org/project/pytest-sugar/>`_
    shows green checkmarks instead of dots for passed tests and has a nice
    progress bar. Like pytest-instafail, it also shows failures immediately.
`pytest-html <https://pypi.org/project/pytest-html/>`_
    enables the creation of HTML reports. Reports can be extended with
    additional data and images, such as screenshots of error cases.
`pytest-icdiff <https://pypi.org/project/pytest-icdiff/>`_
    improves diffs in the error messages of the pytest assertion with `ICDiff
    <https://www.jefftk.com/icdiff>`_.

… web development
~~~~~~~~~~~~~~~~~

pytest is used extensively for testing web projects and there is a long list of
plugins that further simplify testing:

`pytest-selenium <https://pypi.org/project/pytest-selenium/>`_
    provides fixtures that enable simple configuration of browser-based tests
    with `Selenium <https://www.selenium.dev>`_.
`pytest-splinter <https://pypi.org/project/pytest-splinter/>`_
    provide the high-level API of the Selenium-based `Splinter
    <https://pypi.org/project/splinter/>`_ to be used more easily from pytest.
`pytest-httpx <https://pypi.org/project/pytest-httpx/>`_
    facilitates the testing of `HTTPX <https://www.python-httpx.org>`_ and
    `FastAPI <https://fastapi.tiangolo.com>`_ applications.

.. _fake_plugins:

… fake data
~~~~~~~~~~~

We have already used `Faker <https://pypi.org/project/Faker/>`_ in
:ref:`marker_fixtures_combined` to create multiple item instances. There are
many cases in different areas where it is helpful to generate fake data. It is
therefore not surprising that there are several plugins that fulfil this need:

`Faker <https://pypi.org/project/Faker/>`_
    generates fake data for you and offers a faker fixture for use with pytest.
`pytest-factoryboy <https://pypi.org/project/pytest-factoryboy/>`_
    contains fixtures for `factory-boy
    <https://pypi.org/project/factory-boy/>`_, a database model data generator.
`pytest-mimesis <https://pypi.org/project/pytest-mimesis/>`_
    generates fake data similar to Faker, but `Mimesis
    <https://pypi.org/project/mimesis/>`_ is a lot faster.

… various things
~~~~~~~~~~~~~~~~

`pytest-cov <https://pypi.org/project/pytest-cov/>`_
    executes the  :doc:`../coverage` during testing.
`pytest-benchmark <https://pypi.org/project/pytest-benchmark/>`_
    performs benchmark timing for code within tests.
`pytest-timeout <https://pypi.org/project/pytest-timeout/>`_
    prevents tests from running too long.
`pytest-asyncio <https://pypi.org/project/pytest-asyncio/>`_
    tests asynchronous functions.
`pytest-mock <https://pypi.org/project/pytest-mock/>`_
    is a thin wrapper around the  :doc:`unittest.mock <../mock>` patching API.
`pytest-freezegun <https://pypi.org/project/pytest-freezegun/>`_
    freezes the time so that any code that reads the time, date or clock time
    will get the same value during a test. set a specific time.
:doc:`pytest-grpc <Python4DataScience:data-processing/apis/grpc/test>`
    is a Pytest plugin for
    :doc:`Python4DataScience:data-processing/apis/grpc/index`.
`pytest-bdd <https://pypi.org/project/pytest-bdd/>`_
    writes :abbr:`BDD (Behavior Driven Development)` tests with pytest.

Own plugins
-----------

.. seealso::
   * `Writing plugins
     <https://docs.pytest.org/en/latest/how-to/writing_plugins.html>`_
