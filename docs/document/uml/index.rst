Unified Modeling Language (UML)
===============================

Installation
------------

#. Install `plantuml <https://plantuml.com/starting>`_:

   * Download the file `plantuml.jar
     <http://sourceforge.net/projects/plantuml/files/plantuml.jar/download>`_.

#. Install `sphinxcontrib-plantuml
   <https://pypi.org/project/sphinxcontrib-plantuml/>`_:

   .. tab:: Linux/MacOS

      .. code-block:: console

         $ bin/python -m pip install sphinxcontrib-plantuml

   .. tab:: Windows

      .. code-block:: ps1con

         C:> Scripts\python -m pip install sphinxcontrib-plantuml

#. We then configure the ``conf.py``:

   .. code-block:: python

    extensions = [
        ...,
        'sphinxcontrib.plantuml',
        ]

    plantuml = 'java -jar /PATH/TO/plantuml.jar'

   .. note::
            Also in Windows, the path is specified with ``/``.

.. toctree::
   :titlesonly:
   :hidden:

   sequence-diagram
   use-case-diagram
   activity-diagram
   class-diagram
