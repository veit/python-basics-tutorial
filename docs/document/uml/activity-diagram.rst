Activity diagram
================

``(*)``
    Start and end nodes of the activity diagram.

    ``(*top)``
        In some cases, this can be used to move the start point to the beginning
        of the diagram.

``-->``
    defines an activity

    ``-down->``
        Down arrow (default value)
    ``-right-> or ->``
        Right arrow
    ``-left->``
        Arrow to the left
    ``-up->``
        Arrow up

``if``, ``then``, ``else``
    Keywords for the definition of branches.

    Example:

    .. code-block:: rest

       .. uml::

           (*) --> "Initialisation"
           if "a test" then
           -->[true] "An activity"
           --> "Another activity"
           -right-> (*)
           else
           ->[false] "Something else"
           -->[end the processes] (*)
           endif

   .. image:: activity-diagram.svg

``fork``, ``fork again`` and ``end fork`` or ``end merge``
    Keywords for parallel processing.

    Example:

    .. code-block:: rest

       .. uml::

          start
          fork
            :action 1;
          fork again
            :action 2;
          end fork
          stop

    .. image:: parallel.svg
