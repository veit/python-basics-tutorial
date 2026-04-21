Hypothesis
==========

`Property testing
<https://en.wikipedia.org/wiki/Software_testing#Property_testing>`_ is a testing
method that does not check whether specific inputs lead to specific outputs, but
instead generates random inputs, runs the programme with all of these inputs,
and then verifies the validity of this property.

In Python, you can use `Hypothesis <https://hypothesis.readthedocs.io/>`_ to
generate such inputs :term:`parametrically <Parameter>`, enabling you to quickly
find errors in your tests.

.. seealso::
   The :doc:`Jupyter Tutorial <jupyter-tutorial:notebook/testing/hypothesis>`
   describes how Hypothesis can also be used in Jupyter Notebooks.

Installation
------------

.. tab:: Linux/macOS

   .. code-block:: console

      $ uv add --group tests hypothesis

.. tab:: Windows

   .. code-block:: ps1con

      C:> uv add --group tests hypothesis

Alternatively, Hypothesis can also be installed using extensions, for example:

.. tab:: Linux/macOS

   .. code-block:: console

      $ uv add --group tests "hypothesis[numpy, pandas]"

.. tab:: Windows

   .. code-block:: ps1con

          C:> uv add --group tests "hypothesis[numpy, pandas]"

.. seealso:
   * `First-party extensions
     <https://hypothesis.readthedocs.io/en/latest/extras.html>`_

Example using ``strategies`` and ``given``
------------------------------------------

#. First, we import sample data for `floats
   <https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.floats>`_
   and `lists
   <https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.lists>`_
   from `hypothesis.strategies
   <https://hypothesis.readthedocs.io/en/latest/reference/strategies.html>`_. To
   be able to apply this sample data to our test function, we also import
   `hypothesis.given
   <https://hypothesis.readthedocs.io/en/latest/reference/api.html#hypothesis.given>`_:

   .. literalinclude:: test_hypothesis.py
      :language: python
      :lines: 1-3
      :lineno-start: 1

#. For our test, we will now use ``hypothesis.given`` as a :doc:`dekorator
   <../functions/decorators>` to convert the test function into a parameterised
   one, which is then executed with a wide range of suitable data:

   .. literalinclude:: test_hypothesis.py
      :language: python
      :lines: 6-
      :lineno-start: 6

#. Finally, we run the test:

   .. tab:: Linux/macOS

      .. code-block:: pytest

         $ uv run pytest docs/test/test_hypothesis.py
         ============================= test session starts ==============================
         platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
         rootdir: /Users/veit/cusy/trn/python-basics-tutorial-de
         plugins: hypothesis-6.152.1
         collected 1 item

         test_hypothesis.py F                                                     [100%]

         =================================== FAILURES ===================================
         __________________________________ test_mean ___________________________________

             @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
         >   def test_mean(ls):

         test_hypothesis.py:6:
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

         ls = [9.9792015476736e+291, 1.7976931348623157e+308]

             @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
             def test_mean(ls):
                 mean = sum(ls) / len(ls)
         >       assert min(ls) <= mean <= max(ls)
         E       assert inf <= 1.7976931348623157e+308
         E         +  where 1.7976931348623157e+308 = max([9.9792015476736e+291, 1.7976931348623157e+308])

         test_hypothesis.py:8: AssertionError
         ---------------------------------- Hypothesis ----------------------------------
         Falsifying example: test_mean(
             ls=[9.9792015476736e+291, 1.7976931348623157e+308],
         )
         =========================== short test summary info ============================
         FAILED test_hypothesis.py::test_mean - assert inf <= 1.7976931348623157e+308
         ============================== 1 failed in 0.44s ===============================

   .. tab:: Windows

      .. code-block:: pytest

         C:> uv run pytest docs/test/test_hypothesis.py
         ============================= test session starts ==============================
         platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
         rootdir: C:\Users\veit\python-basics-tutorial-de
         plugins: hypothesis-6.152.1
         collected 1 item

         test_hypothesis.py F                                                     [100%]

         =================================== FAILURES ===================================
         __________________________________ test_mean ___________________________________

             @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
         >   def test_mean(ls):

         test_hypothesis.py:6:
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

         ls = [9.9792015476736e+291, 1.7976931348623157e+308]

             @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
             def test_mean(ls):
                 mean = sum(ls) / len(ls)
         >       assert min(ls) <= mean <= max(ls)
         E       assert inf <= 1.7976931348623157e+308
         E        +  where 1.7976931348623157e+308 = max([9.9792015476736e+291, 1.7976931348623157e+308])

         test_hypothesis.py:8: AssertionError
         ---------------------------------- Hypothesis ----------------------------------
         Falsifying example: test_mean(
             ls=[9.9792015476736e+291, 1.7976931348623157e+308],
         )
         =========================== short test summary info ============================
         FAILED test_hypothesis.py::test_mean - assert inf <= 1.7976931348623157e+308
         ============================== 1 failed in 0.44s ===============================

   In the list ``[9.9792015476736e+291, 1.7976931348623157e+308]``, the
   calculation of the mean gives ``inf``, and ``inf`` is not less than the
   larger of the two numbers.

Example with regular expressions
--------------------------------

#. In the following example, we attempt to extract the ``username`` and
   ``domain`` with a :doc:`regular expression
   <../types/strings/built-in-modules/regex>` from an email address using:

   .. literalinclude:: test_emails.py
      :lines: 1, 5-9

#. Now let’s write a test called :func:`test_parse_email` to check our function.
   We’ll use the `emails
   <https://hypothesis.readthedocs.io/en/latest/reference/strategies.html#hypothesis.strategies.emails>`_
   strategy from Hypothesis as our input values. As a result, we expect, for
   example, that for :samp:`veit@cusy.io`, the ``username`` is veit and the
   ``domain`` is cusy.io.

#. In our test, we assume, on the one hand, that two entries are always returned
   and that the second entry contains a full stop (``.``):

   .. literalinclude:: test_emails.py
      :lines: 3-4, 10-

#. Now let’s run the test:

   .. code-block:: pytest
      :emphasize-lines: 26

      $ uv run pytest docs/test/test_emails.py
      ============================= test session starts ==============================
      platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
      rootdir: /Users/veit/cusy/trn/python-basics-tutorial-de
      configfile: pyproject.toml
      plugins: hypothesis-6.152.1
      collected 1 item

      docs/test/test_emails.py F                                               [100%]

      =================================== FAILURES ===================================
      _______________________________ test_parse_email _______________________________
        + Exception Group Traceback (most recent call last):
        |   File "/Users/veit/cusy/trn/python-basics-tutorial-de/docs/test/test_emails.py", line 12, in test_parse_email
        |     def test_parse_email(email):
        |                    ^^^
        |   File "/Users/veit/cusy/trn/python-basics-tutorial-de/.venv/lib/python3.13/site-packages/hypothesis/core.py", line 2264, in wrapped_test
        |     raise the_error_hypothesis_found
        | ExceptionGroup: Hypothesis found 2 distinct failures. (2 sub-exceptions)
        +-+---------------- 1 ----------------
          | Traceback (most recent call last):
          |   File "/Users/veit/cusy/trn/python-basics-tutorial-de/docs/test/test_emails.py", line 16, in test_parse_email
          |     assert '.' in result[1]
          | AssertionError: assert '.' in '0'
          | Falsifying example: test_parse_email(
          |     email='0/0@A.AC',
          | )
          +---------------- 2 ----------------
          | Traceback (most recent call last):
          |   File "/Users/veit/cusy/trn/python-basics-tutorial-de/docs/test/test_emails.py", line 13, in test_parse_email
          |     result = parse_email(email)
          |   File "/Users/veit/cusy/trn/python-basics-tutorial-de/docs/test/test_emails.py", line 8, in parse_email
          |     result = re.match(r"(?P<username>\w+).(?P<domain>[\w\.]+)", email).groups()
          |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          | AttributeError: 'NoneType' object has no attribute 'groups'
          | Falsifying example: test_parse_email(
          |     email='/@A.AC',
          | )
          +------------------------------------
      =========================== short test summary info ============================
      FAILED docs/test/test_emails.py::test_parse_email - ExceptionGroup: Hypothesis found 2 distinct failures. (2 sub-exceptions)
      ============================== 1 failed in 0.14s ===============================

   The email address provided by Hypothesis, ``0/0@A.ac``, shows that our
   regular expression in the :func:`parse_email` method is not yet sufficient.
   We will therefore adjust our regular expression and then run the test again:

   .. literalinclude:: test_emails_2.py
      :diff: test_emails.py

   .. code-block:: pytest

        $ uv run pytest docs/test/test_emails_2.py
        ============================= test session starts ==============================
        platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
        rootdir: /Users/veit/cusy/trn/python-basics-tutorial-de
        configfile: pyproject.toml
        plugins: hypothesis-6.152.1
        collected 1 item

        docs/test/test_emails_2.py .                                             [100%]

        ============================== 1 passed in 0.29s ===============================

Third-party extensions
----------------------

There are a number of open-source libraries that extend :doc:`index`
capabilities. Some of these are listed on `Third-party extensions
<https://hypothesis.readthedocs.io/en/latest/extensions.html>`_; you can find
more on :term:`PyPI` by searching for `keywords
<https://pypi.org/search/?q=hypothesis>`_ or using the `framework classifier
<https://pypi.org/search/?c=Framework+%3A%3A+Hypothesis>`_.
