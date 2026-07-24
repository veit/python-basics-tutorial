shot-scraper
============

`shot-scraper <https://shot-scraper.datasette.io/en/stable/>`_ is a tool to
automate the process of updating screenshots.

Installation
------------

.. code-block:: console

   $ uv add --group docs shot-scraper
   $ uv run shot-scraper install

.. note::
   The second line installs the required browser.

.. seealso::
   `shot-scraper Installation
   <https://shot-scraper.datasette.io/en/stable/installation.html>`_

Use
---

shot-scraper can be used in several ways

#. …for single screenshots on the command line:

   .. code-block:: console

      $ uv run shot-scraper https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html -o ~/Downloads/clean-prep.png

   …or with additional options, for example for JavaScript and CSS selectors:

   .. code-block:: console

      $ uv run shot-scraper https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html -s '#overview' -o ~/Downloads/clean-prep.png

#. …for a set of screenshots configured in a YAML file:

   .. code-block:: yaml

      - url: https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html
        output: ~/Downloads/clean-prep.png
      - url: https://www.example.org/
        width: 736
        quality: 40
        output: example.jpg

   Afterwards ``shot-scraper multi`` can be used, for example:

   .. code-block:: console

      $ shot-scraper multi shots.yaml
      Screenshot of 'https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html' written to '~(Downloads/clean-prep.png'
      Screenshot of 'https://www.example.org/' written to 'example.jpg'

   .. seealso::
      * `Taking multiple screenshots
        <https://shot-scraper.datasette.io/en/stable/multi.html>`_

#. …for videos:

   The ``shot-scraper video`` command captures a WebM video based on a
   :doc:`Python4DataScience:data-processing/serialisation-formats/yaml/index`
   storyboard. Storyboards describe the video as a sequence of scenes. Each
   scene can open a page, wait for content, perform actions and pause between
   steps, for example:

   .. literalinclude:: storyboard.yml
      :caption: storyboard.yml
      :language: yaml

   Then run the following command:

   .. code-block:: console

      $ uv run shot-scraper video storyboard.yml

   This opens ``url``, records the scenes and saves the video as
   :file:`demo.webm`.

   As long as `FFmpeg <https://www.ffmpeg.org/>`_ is installed, you can use the
   ``--mp4`` option to convert the recorded WebM video to MP4 as well.

   .. seealso::
      * `Recording videos
        <https://shot-scraper.datasette.io/en/stable/video.html>`_

GitHub Actions
--------------

shot-scraper can be easily integrated into GitHub Actions. The shot-scraper-demo
repository also contains an exemplary `shots.yml
<https://github.com/simonw/shot-scraper-demo/blob/main/.github/workflows/shots.yml>`_. Once a day, two screenshots are created and transferred back to the
repository. Note, however, that saving image files that change frequently can
make the revision history very unreadable. Therefore, you should use
shot-scraper with caution together with GitHub Actions.
