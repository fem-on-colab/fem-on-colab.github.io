.. _packages:

Packages
============
.. meta::
    :description lang=en:
        You can install one of the packages provided by FEM on Colab by adding the following cell at the top of your notebook.
.. packages::

Automated weekly build of end user packages
-------------------------------------------

Since January 2022 end user packages [#f1]_ are automatically built on a weekly basis, in order to follow upstream development.

Users that do not wish to be up to date with the upstream development cycle are invited to hardcode in their Google Colab notebooks a fixed release by replacing

.. raw:: html

    <div class="package-installation" style="margin-top: 0; margin-bottom: 0; margin-left: 1rem;">https://fem-on-colab.github.io/releases/{install-script}</div>

in the instructions above with

.. raw:: html

    <div class="package-installation" style="margin-top: 0; margin-bottom: 0; margin-left: 1rem;">https://github.com/fem-on-colab/fem-on-colab.github.io/raw/{commit}/releases/{install-script}</div>

where ``{install-script}`` is the installation script of the desired package, and ``{commit}`` is the SHA of a commit `in this list  <https://github.com/fem-on-colab/fem-on-colab.github.io/commits/gh-pages>`__ at which the desired version was available.

.. rubric:: Notes

.. [#f1] The FEniCS package is not automatically built, due to the upstream development having moved to FEniCSx.

Weekly release downloads stats
------------------------------
.. stats::
