Debugging test failures
=======================

When tests fail, we need to find out why. Maybe it’s the test, or maybe it’s the
application. The process of finding out where the problem is and what to do
about it is similar.

pytest offers many tools that can help us solve a problem faster without having
to run a debugger. Python includes a built-in source code debugger called
``pdb``, as well as several options that make debugging with ``pdb`` quick and
easy.

Below we will debug some broken code using pytest options and ``pdb``, looking
at the debugging options and integration of pytest and ``pdb``.

Debugging with pytest options
-----------------------------

pytest contains a whole range of command line options that are useful for
debugging. We will use some of them to fix our test errors. Options for
selecting which tests to run, in what order, and when to stop them.

In all of these descriptions, the term *error* refers to a failed ``assertion``
or other uncaught ``exception`` found in our source or test code, including
fixtures.

#. Re-execution of failed tests

   Let’s start debugging by making sure that the tests fail when we re-execute
   them. To do this, we use ``--lf`` to re-execute only the failed tests and
   ``--tb=no`` to hide the traceback. This way we know that we can reproduce the
   error.

   #. Now we can start debugging the first error by running the first failed
      test, stopping after the error and looking at the traceback: ``pytest --lf
      -x``.

   #.  To make sure we understand the problem, we can run the same test again
       with ``-l``/``--showlocals``. We don’t need the full traceback again, so
       we can shorten it with ``--tb=short``: ``pytest --lf -x -l --tb=short``.

       ``-l``/``--showlocals`` are often very helpful and sometimes good enough
       to recognise a test error completely.

#. Debugging with pdb

   :abbr:`pdb (Python Debugger)` is part of the Python standard library, so we
   don’t need to install anything to use it. You can start pdb from pytest in
   several ways:

   - add a ``breakpoint()`` call to either the test or application code. When a
     pytest run encounters a ``breakpoint()`` function call, it will stop there
     and start pdb.
   - use the ``--pdb`` option. With ``--pdb``, pytest will stop at the point of
     failure.
   - uses the combination of the ``--lf`` and ``--trace`` options. With
     ``--trace`` pytest stops at the beginning of each test.

     The common commands recognised by pdb are listed below:

     +-------------------------------+-----------------------------------------------+
     | Options                       | Description                                   |
     +===============================+===============================================+
     | Meta commands                                                                 |
     +-------------------------------+-----------------------------------------------+
     | :samp:`h(elp)`                | outputs a list of commands.                   |
     +-------------------------------+-----------------------------------------------+
     | :samp:`h(elp) {COMMAND}`      | outputs the help for a command.               |
     +-------------------------------+-----------------------------------------------+
     | :samp:`q(uit)`                | terminates pdb.                               |
     +-------------------------------+-----------------------------------------------+
     | See where you are                                                             |
     +-------------------------------+-----------------------------------------------+
     | :samp:`l(ist)`                | lists eleven lines around the current line;   |
     |                               | when called again, the next eleven lines are  |
     |                               | listed.                                       |
     +-------------------------------+-----------------------------------------------+
     | :samp:`l(ist) .`              | The same as above, but with a dot. Lists      |
     |                               | eleven lines around the current line. Useful  |
     |                               | if you have used l(list) a few times and have |
     |                               | lost your current position.                   |
     +-------------------------------+-----------------------------------------------+
     | :samp:`l(ist) first|last`     | lists a specific group of lines.              |
     +-------------------------------+-----------------------------------------------+
     | :samp:`ll`                    | lists the entire source code for the current  |
     |                               | function.                                     |
     +-------------------------------+-----------------------------------------------+
     | :samp:`w(here)`               | outputs the stack trace.                      |
     +-------------------------------+-----------------------------------------------+
     | View values                                                                   |
     +-------------------------------+-----------------------------------------------+
     | :samp:`p(rint) {EXPR}`        | evaluates :samp:`{EXPR}` and outputs the      |
     |                               | value.                                        |
     +-------------------------------+-----------------------------------------------+
     | :samp:`pp {EXPR}`             | corresponds to :samp:`p(rint) {EXPR}`, but    |
     |                               | uses ``pretty-print`` from the :doc:`pprint   |
     |                               | <python3:library/pprint>` module.             |
     +-------------------------------+-----------------------------------------------+
     | :samp:`a(rgs)`                | outputs the argument list of the current      |
     |                               | function.                                     |
     +-------------------------------+-----------------------------------------------+
     | Execution commands                                                            |
     +-------------------------------+-----------------------------------------------+
     | :samp:`s(tep)`                | executes the current line and jumps to the    |
     |                               | next line in your source code, even if it is  |
     |                               | inside a function.                            |
     +-------------------------------+-----------------------------------------------+
     | :samp:`n(ext)`                | executes the current line and jumps to the    |
     |                               | next line in the current function.            |
     +-------------------------------+-----------------------------------------------+
     | :samp:`c(ontinue)`            | continues to the next breakpoint.  When used  |
     |                               | with ``--trace`` , continues to the start of  |
     |                               | the next test.                                |
     +-------------------------------+-----------------------------------------------+
     | :samp:`unt(il) {LINENO}`      | continues to the specified line number.       |
     +-------------------------------+-----------------------------------------------+

     .. seealso::
        The complete list can be found in `Debugger Commands
        <https://docs.python.org/3/library/pdb.html#debugger-commands>`_ of the
        pdb documentation.

Combining pdb and tox
---------------------

In order to combine pdb with tox, we need to make sure that we can pass
arguments through tox to pytest. This is done with the ``{posargs}`` function of
tox, which was described in :ref:`posargs`. We have already set up this function
in our :file:`tox.ini` for Items:

.. code-block:: ini
   :emphasize-lines: 11

   [tox]
   envlist = py38, py39, py310, py311
   isolated_build = True
   skip_missing_interpreters = True

   [testenv]
   deps =
     pytest
     faker
     pytest-cov
   commands = pytest --cov=items --cov-fail-under=99  {posargs}

   [gh-actions]
   python =
     3.8: py38
     3.9: py39
     3.10: py310
     3.11: py311

We want to run the Python 3.11 environment and start the debugger on a failed
test with ``tox -e py311 -- --pdb --no-cov``. This will take us to the pdb,
right at the assertion that failed.

Once we have found and fixed the error, we can run the tox environment again
with this one test error: ``tox -e py311 -- --lf --tb=no --no-cov``.

Overview of the most common pytest debugger options
---------------------------------------------------

+-------------------------------+-----------------------------------------------+
| Options                       | Description                                   |
+===============================+===============================================+
| Options for selecting which tests are to be executed in which order and when  |
| they are to be stopped:                                                       |
+-------------------------------+-----------------------------------------------+
| :samp:`--lf`,                 | executes the test that failed first           |
| :samp:`--last-failedlf`       |                                               |
+-------------------------------+-----------------------------------------------+
| :samp:`--ff`,                 | starts with the test that failed first and    |
| :samp:`--failed-first`        | then executes all of them.                    |
+-------------------------------+-----------------------------------------------+
| :samp:`-x`,                   | stops at the first error and then executes    |
| :samp:`--exitfirst`           | all.                                          |
+-------------------------------+-----------------------------------------------+
| :samp:`-maxfail={NUM}`        | stops the tests after :samp:`{NUM}` errors.   |
+-------------------------------+-----------------------------------------------+
| :samp:`--nf`,                 | executes new test files first, then the rest  |
| :samp:`--new-first`           | sorted by modification date.                  |
+-------------------------------+-----------------------------------------------+
| :samp:`--sw`,                 | executes the last failed test, then stops at  |
| :samp:`--stepwise`            | the next error and starts again at the last   |
|                               | failed test the next time. Similar to the     |
|                               | combination of :samp:`--lf -x`, but more      |
|                               | efficient.                                    |
+-------------------------------+-----------------------------------------------+
| :samp:`--sw-skip`,            | as above, but a failed test is skipped.       |
| :samp:`--stepwise-skip`       |                                               |
+-------------------------------+-----------------------------------------------+
| Options to control pytest output:                                             |
+-------------------------------+-----------------------------------------------+
| :samp:`-v`,                   | verbos, :samp:`-vv`  even more detailed       |
| :samp:`--verbose:`            |                                               |
+-------------------------------+-----------------------------------------------+
| :samp:`--tb`                  | Traceback style:                              |
|                               | :samp:`[auto|long|short|line|native|no]`      |
|                               |                                               |
|                               | I usually use :samp:`--tb=short` as the       |
|                               | default setting in the configuration file and |
|                               | the others for debugging.                     |
+-------------------------------+-----------------------------------------------+
| :samp:`-l`,                   | shows local variables next to the stacktrace. |
| :samp:`--showlocals`          |                                               |
+-------------------------------+-----------------------------------------------+
| Options to start a command line debugger:                                     |
+-------------------------------+-----------------------------------------------+
| :samp:`--pdb`                 | starts the Python debugger in the event of an |
|                               | error. Very useful for debugging with         |
|                               | :doc:`../tox`.                                |
+-------------------------------+-----------------------------------------------+
| :samp:`--trace`               | starts the pdb source code debugger           |
|                               | immediately when each test is executed.       |
+-------------------------------+-----------------------------------------------+
| :samp:`--pdbcls`              | uses alternatives to pdb, for example the     |
|                               | IPython debugger with ``--pdb-cls =           |
|                               | IPython.terminal.debugger:TerminalPdb``       |
+-------------------------------+-----------------------------------------------+
