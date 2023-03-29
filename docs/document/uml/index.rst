Unified Modeling Language (UML)
===============================

Installation
------------

#. Install `plantuml <https://plantuml.com/starting>`_:

   * Install the Java and Graphviz dependencies:

     .. tab:: Linux

        .. code-block:: console

           $ sudo apt install openjdk-11-jdk graphviz

* Download the :download:`plantuml.jar
  <http://sourceforge.net/projects/plantuml/files/plantuml.jar/download>`.

#. Install `sphinxcontrib-plantuml
   <https://pypi.org/project/sphinxcontrib-plantuml/>`_:

   .. tab:: Linux/macOS

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
