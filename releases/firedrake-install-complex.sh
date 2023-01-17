# Copyright (C) 2021-2023 by the FEM on Colab authors
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
FIREDRAKE_INSTALLED="$SHARE_PREFIX/firedrake.installed"

if [[ ! -f $FIREDRAKE_INSTALLED ]]; then
    # Install pybind11
    PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/bd824e7/releases/pybind11-install.sh"}
    [[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && PYBIND11_INSTALL_SCRIPT_DOWNLOAD=${PYBIND11_INSTALL_SCRIPT_PATH} && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh && [[ ! -f ${PYBIND11_INSTALL_SCRIPT_PATH} ]] && wget ${PYBIND11_INSTALL_SCRIPT_DOWNLOAD} -O ${PYBIND11_INSTALL_SCRIPT_PATH}
    source $PYBIND11_INSTALL_SCRIPT_PATH

    # Install boost (and its dependencies)
    BOOST_INSTALL_SCRIPT_PATH=${BOOST_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/62dc5c3/releases/boost-install.sh"}
    [[ $BOOST_INSTALL_SCRIPT_PATH == http* ]] && BOOST_INSTALL_SCRIPT_DOWNLOAD=${BOOST_INSTALL_SCRIPT_PATH} && BOOST_INSTALL_SCRIPT_PATH=/tmp/boost-install.sh && [[ ! -f ${BOOST_INSTALL_SCRIPT_PATH} ]] && wget ${BOOST_INSTALL_SCRIPT_DOWNLOAD} -O ${BOOST_INSTALL_SCRIPT_PATH}
    source $BOOST_INSTALL_SCRIPT_PATH

    # Install slepc4py (and its dependencies)
    SLEPC4PY_INSTALL_SCRIPT_PATH=${SLEPC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/1f587b4/releases/slepc4py-install-complex.sh"}
    [[ $SLEPC4PY_INSTALL_SCRIPT_PATH == http* ]] && SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD=${SLEPC4PY_INSTALL_SCRIPT_PATH} && SLEPC4PY_INSTALL_SCRIPT_PATH=/tmp/slepc4py-install.sh && [[ ! -f ${SLEPC4PY_INSTALL_SCRIPT_PATH} ]] && wget ${SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD} -O ${SLEPC4PY_INSTALL_SCRIPT_PATH}
    source $SLEPC4PY_INSTALL_SCRIPT_PATH

    # Install vtk
    VTK_INSTALL_SCRIPT_PATH=${VTK_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/fb87dcb/releases/vtk-install.sh"}
    [[ $VTK_INSTALL_SCRIPT_PATH == http* ]] && VTK_INSTALL_SCRIPT_DOWNLOAD=${VTK_INSTALL_SCRIPT_PATH} && VTK_INSTALL_SCRIPT_PATH=/tmp/vtk-install.sh && [[ ! -f ${VTK_INSTALL_SCRIPT_PATH} ]] && wget ${VTK_INSTALL_SCRIPT_DOWNLOAD} -O ${VTK_INSTALL_SCRIPT_PATH}
    source $VTK_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    FIREDRAKE_ARCHIVE_PATH=${FIREDRAKE_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/firedrake-20230117-202051-7f7ca17-complex/firedrake-install.tar.gz"}
    [[ $FIREDRAKE_ARCHIVE_PATH == http* ]] && FIREDRAKE_ARCHIVE_DOWNLOAD=${FIREDRAKE_ARCHIVE_PATH} && FIREDRAKE_ARCHIVE_PATH=/tmp/firedrake-install.tar.gz && wget ${FIREDRAKE_ARCHIVE_DOWNLOAD} -O ${FIREDRAKE_ARCHIVE_PATH}
    if [[ $FIREDRAKE_ARCHIVE_PATH != skip ]]; then
        rm -rf /usr/lib/python*/*-packages/netCDF4*
        rm -rf $INSTALL_PREFIX/lib/python*/*-packages/netCDF4*
        tar -xzf $FIREDRAKE_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $FIREDRAKE_INSTALLED
fi
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
