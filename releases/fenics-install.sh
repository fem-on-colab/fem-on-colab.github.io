# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
SHARE_PREFIX="/usr/local/share/fem-on-colab"
FENICS_INSTALLED="$SHARE_PREFIX/fenics.installed"

if [[ ! -f $FENICS_INSTALLED ]]; then
    # Install pybind11
    PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/8aad56e/releases/pybind11-install.sh"}
    [[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && PYBIND11_INSTALL_SCRIPT_DOWNLOAD=${PYBIND11_INSTALL_SCRIPT_PATH} && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh && [[ ! -f ${PYBIND11_INSTALL_SCRIPT_PATH} ]] && wget ${PYBIND11_INSTALL_SCRIPT_DOWNLOAD} -O ${PYBIND11_INSTALL_SCRIPT_PATH}
    source $PYBIND11_INSTALL_SCRIPT_PATH

    # Install boost (and its dependencies)
    BOOST_INSTALL_SCRIPT_PATH=${BOOST_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/d26da57/releases/boost-install.sh"}
    [[ $BOOST_INSTALL_SCRIPT_PATH == http* ]] && BOOST_INSTALL_SCRIPT_DOWNLOAD=${BOOST_INSTALL_SCRIPT_PATH} && BOOST_INSTALL_SCRIPT_PATH=/tmp/boost-install.sh && [[ ! -f ${BOOST_INSTALL_SCRIPT_PATH} ]] && wget ${BOOST_INSTALL_SCRIPT_DOWNLOAD} -O ${BOOST_INSTALL_SCRIPT_PATH}
    source $BOOST_INSTALL_SCRIPT_PATH

    # Install slepc4py (and its dependencies)
    SLEPC4PY_INSTALL_SCRIPT_PATH=${SLEPC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/6929e27/releases/slepc4py-install-real.sh"}
    [[ $SLEPC4PY_INSTALL_SCRIPT_PATH == http* ]] && SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD=${SLEPC4PY_INSTALL_SCRIPT_PATH} && SLEPC4PY_INSTALL_SCRIPT_PATH=/tmp/slepc4py-install.sh && [[ ! -f ${SLEPC4PY_INSTALL_SCRIPT_PATH} ]] && wget ${SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD} -O ${SLEPC4PY_INSTALL_SCRIPT_PATH}
    source $SLEPC4PY_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    FENICS_ARCHIVE_PATH=${FENICS_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/fenics-20221029-120150-3907b15/fenics-install.tar-aa3ba34bc5c96ef23306a37fdee3c751.gz"}
    [[ $FENICS_ARCHIVE_PATH == http* ]] && FENICS_ARCHIVE_DOWNLOAD=${FENICS_ARCHIVE_PATH} && FENICS_ARCHIVE_PATH=/tmp/fenics-install.tar.gz && wget ${FENICS_ARCHIVE_DOWNLOAD} -O ${FENICS_ARCHIVE_PATH}
    if [[ $FENICS_ARCHIVE_PATH != skip ]]; then
        tar -xzf $FENICS_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
    fi

    # Add symbolic links to FEniCS libraries in /usr/lib, because Colab does not export /usr/local/lib to LD_LIBRARY_PATH
    if [[ $FENICS_ARCHIVE_PATH != skip ]]; then
        ln -fs /usr/local/lib/libdolfin*.so* /usr/lib
        ln -fs /usr/local/lib/libmshr*.so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $FENICS_INSTALLED
fi
