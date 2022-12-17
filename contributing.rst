How to contribute
=================
.. meta::
    :description lang=en:
        FEM on Colab developement takes place on GitHub. We are still at an early developement stage.
        Feel free to contact us by email for further information.

.. image:: _static/images/github-logo.png
    :target: https://github.com/fem-on-colab/fem-on-colab
    :height: 80px
    :width: 80px
    :alt: Go to repository on GitHub
.. image:: _static/images/email.png
    :target: mailto:francesco.ballarin@unicatt.it
    :height: 80px
    :width: 80px
    :alt: Contact us via email

History and the underlying motivation
-------------------------------------

The project started in 2021 with two main technical motivations:

* the Google Colab team realesed in February 2021 an upgrade to their system to use python 3.7. This effectively detaches their python version from Ubuntu upstream packages, bacause python 3.7 is not supported by upstream Ubuntu 18.04 LTS (the newest supported version is 3.6). This means that a custom packaging pipeline needs to be implemented to support Colab.
* the gcc suite available on Colab (although slightly newer than the one in Ubuntu 18.04 LTS), is still part of the 7.x series. This is too old for some of the target libraries in this project.

Contributing: small donations through GitHub Sponsors
-----------------------------------------------------

Small donations can be sent through the `GitHub Sponsors <https://github.com/sponsors/francesco-ballarin>`__ program.

Contributing: reporting broken packages
---------------------------------------

Please report broken packages by `opening a new GitHub issue <https://github.com/fem-on-colab/fem-on-colab/issues>`__.

Contributing: maintaining a package
-----------------------------------

Packages are released automatically following a weekly schedule for end user packages, and a monthly schedule for the rest of the supported packages. To manually release an updated version of an existing package without waiting for the schedule, proceed as follows:

1. If an issue has been opened on `our GitHub tracker <https://github.com/fem-on-colab/fem-on-colab/issues>`__ reporting a broken package, please assign the issue to yourself to let users/maintainers know that you are working on it.
2. Go to the `scheduled release workflow on our GitHub Actions <https://github.com/fem-on-colab/fem-on-colab/actions/workflows/schedule_all.yml>`__ and manually trigger a new build from the `Run workflow` dropdown. Make sure to insert the name of the library to build.
3. [Optional, but suggested if the reported issue was not detected by CI] After a successful workflow, please double check existing tests on an actual Colab runtime, by clicking on the `Open in Colab` badges in the README file in the package subfolder.
4. [Optional, but suggested if the reported issue was not detected by CI] Similarly, double check existing tests of any downstream dependency of the updated package. See our `dependency graph <https://github.com/fem-on-colab/fem-on-colab/raw/main/scripts/graph.png>`__ to determine downstream packages that need checking.

Please get in touch with us by `email <mailto:francesco.ballarin@unicatt.it>`__ if you are interested in helping maintaining a package.
