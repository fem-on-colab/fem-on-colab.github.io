.. _advanced:

Advanced usage
==============
.. meta::
    :description lang=en:
        Advanced usage of FEM on Colab packages and scripts.

Specific versions of end user packages
--------------------------------------

End user packages [#f1]_ are automatically built on a weekly basis, in order to follow upstream development.

Users that do not wish to be up to date with the upstream development cycle are invited to hardcode in their Google Colab notebooks a fixed release by replacing

.. raw:: html

    <div class="package-installation" style="margin-top: 0; margin-bottom: 0; margin-left: 1rem;">https://fem-on-colab.github.io/releases/{install-script}</div>

in the instructions reported in the :ref:`packages` page with

.. raw:: html

    <div class="package-installation" style="margin-top: 0; margin-bottom: 0; margin-left: 1rem;">https://github.com/fem-on-colab/fem-on-colab.github.io/raw/{commit}/releases/{install-script}</div>

where ``{install-script}`` is the installation script of the desired package, and ``{commit}`` is the SHA of a commit `in this list <https://github.com/fem-on-colab/fem-on-colab.github.io/commits/gh-pages>`__ at which the desired version was available.

.. rubric:: Notes

.. [#f1] The FEniCS package is not automatically built, due to the upstream development having moved to FEniCSx.

GitHub workflow to facilitate notebook preparation
---------------------------------------------------
The `Open in Colab workflow <https://github.com/fem-on-colab/fem-on-colab.github.io/commits/gh-pages>`__ facilitates automatic preparation of notebooks for deployment on Google Colab, by automatically adding installation cells, replacing local images contained in the local repository with their base64 representation, and scraping links to other notebooks in the same repository. Notebooks can be uploaded to Google Drive, to a GitHub repository or as artifact of a GitHub actions run. Sample usage is available `in this workflow file <https://github.com/fem-on-colab/open-in-colab-workflow/blob/main/.github/workflows/ci.yml>`__.
