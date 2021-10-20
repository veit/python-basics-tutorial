Sequence diagram
================

.. uml::

    Browser -> Server: Authentication Request
    Server --> Browser: Authentication Response

    Browser -> Server: Another authentication Request
    Browser <-- Server: another authentication Response

.. code-block:: rest

   .. uml::

       Browser -> Server: Authentication Request
       Server --> Browser: Authentication Response

       Browser -> Server: Another authentication Request
       Browser <-- Server: another authentication Response

``->``
    is used to draw a message between two actors. The actors do not have to be
    declared explicitly.
``-->``
     is used to draw a dotted line.
``<- und <--``
    do not change the drawing, but may increase readability.
    
    .. note::
       This applies only to sequence diagrams. In other diagrams other rules may
       apply.
