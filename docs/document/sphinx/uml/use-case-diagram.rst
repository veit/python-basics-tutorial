Use Case diagram
================

.. uml::

   :User: --> (Use)
   "Group of\nAdministrators " as Admin
   "Using the\napplication" as (Use)
   Admin --> (Administering\nthe Application)

.. code-block:: rest

   .. uml::

      :User: --> (Use)
      "Group of\nAdministrators " as Admin
      "Using the\napplication" as (Use)
      Admin --> (Administering\nthe Application)

Use cases are enclosed by round brackets ``()`` and resemble an oval.

Alternatively, the ``usecase`` keyword can be used to define a use case. In
addition, it is possible to define an alias using the ``as`` keyword. This alias
can then be used when defining relationships.

You can add line breaks to the name of the use cases with ``\n``.
