# Copyright (C) 2021-2024 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
INSTALL_PREFIX=${INSTALL_PREFIX:-"/usr/local"}
INSTALL_PREFIX_DEPTH=$(echo $INSTALL_PREFIX | awk -F"/" '{print NF-1}')
PROJECT_NAME=${PROJECT_NAME:-"fem-on-colab"}
SHARE_PREFIX="$INSTALL_PREFIX/share/$PROJECT_NAME"
NGSOLVE_INSTALLED="$SHARE_PREFIX/ngsolve.installed"

if [[ ! -f $NGSOLVE_INSTALLED ]]; then
    # Install OCC
    OCC_INSTALL_SCRIPT_PATH=${OCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/b132c1b/releases/occ-install.sh"}
    [[ $OCC_INSTALL_SCRIPT_PATH == http* ]] && OCC_INSTALL_SCRIPT_DOWNLOAD=${OCC_INSTALL_SCRIPT_PATH} && OCC_INSTALL_SCRIPT_PATH=/tmp/occ-install.sh && [[ ! -f ${OCC_INSTALL_SCRIPT_PATH} ]] && wget ${OCC_INSTALL_SCRIPT_DOWNLOAD} -O ${OCC_INSTALL_SCRIPT_PATH}
    source $OCC_INSTALL_SCRIPT_PATH

    # Install pybind11
    PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/76536e9/releases/pybind11-install.sh"}
    [[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && PYBIND11_INSTALL_SCRIPT_DOWNLOAD=${PYBIND11_INSTALL_SCRIPT_PATH} && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh && [[ ! -f ${PYBIND11_INSTALL_SCRIPT_PATH} ]] && wget ${PYBIND11_INSTALL_SCRIPT_DOWNLOAD} -O ${PYBIND11_INSTALL_SCRIPT_PATH}
    source $PYBIND11_INSTALL_SCRIPT_PATH

    # Install slepc4py (and its dependencies)
    SLEPC4PY_INSTALL_SCRIPT_PATH=${SLEPC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/dd3167b/releases/slepc4py-install-complex.sh"}
    [[ $SLEPC4PY_INSTALL_SCRIPT_PATH == http* ]] && SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD=${SLEPC4PY_INSTALL_SCRIPT_PATH} && SLEPC4PY_INSTALL_SCRIPT_PATH=/tmp/slepc4py-install.sh && [[ ! -f ${SLEPC4PY_INSTALL_SCRIPT_PATH} ]] && wget ${SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD} -O ${SLEPC4PY_INSTALL_SCRIPT_PATH}
    source $SLEPC4PY_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    NGSOLVE_ARCHIVE_PATH=${NGSOLVE_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/ngsolve-20240224-010320-02da547-complex/ngsolve-install.tar.gz"}
    [[ $NGSOLVE_ARCHIVE_PATH == http* ]] && NGSOLVE_ARCHIVE_DOWNLOAD=${NGSOLVE_ARCHIVE_PATH} && NGSOLVE_ARCHIVE_PATH=/tmp/ngsolve-install.tar.gz && wget ${NGSOLVE_ARCHIVE_DOWNLOAD} -O ${NGSOLVE_ARCHIVE_PATH}
    if [[ $NGSOLVE_ARCHIVE_PATH != skip ]]; then
        tar -xzf $NGSOLVE_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Add symbolic links to python libraries in /usr/lib, because PYTHONHOME/lib may not be in LD_LIBRARY_PATH
    # on the actual cloud instance
    if [[ $NGSOLVE_ARCHIVE_PATH != skip ]]; then
        PYTHONHOME=$(python3 -c "import sys; print(sys.exec_prefix)")
        if [[ $PYTHONHOME != "/usr" ]]; then
            ln -fs $PYTHONHOME/lib/libpython*.so* /usr/lib
        fi
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $NGSOLVE_INSTALLED
fi

# Display end user packages announcement
set +x
cat << EOF
























################################################################################
#     This installation is offered by FEM on Colab, an open-source project     #
#       developed and maintained at Università Cattolica del Sacro Cuore       #
#    by Dr. Francesco Ballarin. Please see https://fem-on-colab.github.io/     #
#       for more details, including a list of further available packages       #
#       and how to sponsor the development or contribute to the project.       #
#                                                                              #
#   We are conducting an informal survey on FEM on Colab usage by our users.   #
#   The survey is anonymous, and its compilation will typically only require   #
#   a couple of minutes of your time. If you wish, give us your feedback at    #
#                     https://forms.gle/36sZZWNvPpUv8XWr7                      #
################################################################################
























EOF
set -x
