Plugins
=======

So far, we have focused on using :doc:`mock <python3:library/unittest.mock>`
directly. However, there are many plugins that can help with mocking, such as
`pytest-mock <https://pypi.org/project/pytest-mock/>`_, which, amongst other
things, provides a ``mocker`` fixture. One advantage is that the fixture cleans
up after itself, so you don’t need to use a ``with`` block, as we did in our
examples. `mocker.spy
<https://pytest-mock.readthedocs.io/en/latest/usage.html#spy>`_ is also a handy
simplification based on ``wraps`` and ``autospec``.

There are also some specialised mocking libraries:

- For mocking database access, the following are suitable:

  - `pytest-postgresql <https://pypi.org/project/pytest-postgresql/>`_
  - `pytest-mongo <https://pypi.org/project/pytest-mongo/>`_
  - `pytest-mysql <https://pypi.org/project/pytest-mysql/>`_
  - `pytest-dynamodb <https://pypi.org/project/pytest-dynamodb/>`_.

- To test HTTP servers, you can use `pytest-httpserver
  <https://pypi.org/project/pytest_httpserver/>`_.
- To mock `requests <https://pypi.org/project/requests/>`_, you can use
  `responses <https://pypi.org/project/responses/>`_ or `betamax
  <https://pypi.org/project/betamax/>`_.
- Other tools for various requirements are

  - `pytest-rabbitmq <https://pypi.org/project/pytest-rabbitmq/>`_
  - `pytest-solr <https://pypi.org/project/pytest-solr/>`_
  - `pytest-elasticsearch <https://pypi.org/project/pytest-elasticsearch/>`_ and
    `pytest-redis <https://pypi.org/project/pytest-redis/>`_.
