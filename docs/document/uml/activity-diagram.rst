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

``=== code ===``
    Synchronisation bar

    Example:

    .. code-block:: rest

        . uml::
        
           (*) --> ===B1===
           --> "First parallel activity"
           --> ===B2===
           ===B1=== --> "Parallel activity 2"
           --> ===B2===
           --> (*)

   .. image:: sync-bar.svg
