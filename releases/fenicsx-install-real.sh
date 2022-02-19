# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
SHARE_PREFIX="/usr/local/share/fem-on-colab"
FENICSX_INSTALLED="$SHARE_PREFIX/fenicsx.installed"

if [[ ! -f $FENICSX_INSTALLED ]]; then
    # Install pybind11
    PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/e9e1ba9/releases/pybind11-install.sh"}
    [[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && PYBIND11_INSTALL_SCRIPT_DOWNLOAD=${PYBIND11_INSTALL_SCRIPT_PATH} && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh && [[ ! -f ${PYBIND11_INSTALL_SCRIPT_PATH} ]] && wget ${PYBIND11_INSTALL_SCRIPT_DOWNLOAD} -O ${PYBIND11_INSTALL_SCRIPT_PATH}
    source $PYBIND11_INSTALL_SCRIPT_PATH

    # Install boost (and its dependencies)
    BOOST_INSTALL_SCRIPT_PATH=${BOOST_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/c88365b/releases/boost-install.sh"}
    [[ $BOOST_INSTALL_SCRIPT_PATH == http* ]] && BOOST_INSTALL_SCRIPT_DOWNLOAD=${BOOST_INSTALL_SCRIPT_PATH} && BOOST_INSTALL_SCRIPT_PATH=/tmp/boost-install.sh && [[ ! -f ${BOOST_INSTALL_SCRIPT_PATH} ]] && wget ${BOOST_INSTALL_SCRIPT_DOWNLOAD} -O ${BOOST_INSTALL_SCRIPT_PATH}
    source $BOOST_INSTALL_SCRIPT_PATH

    # Install slepc4py (and its dependencies)
    SLEPC4PY_INSTALL_SCRIPT_PATH=${SLEPC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/9ad8c8d/releases/slepc4py-install-real.sh"}
    [[ $SLEPC4PY_INSTALL_SCRIPT_PATH == http* ]] && SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD=${SLEPC4PY_INSTALL_SCRIPT_PATH} && SLEPC4PY_INSTALL_SCRIPT_PATH=/tmp/slepc4py-install.sh && [[ ! -f ${SLEPC4PY_INSTALL_SCRIPT_PATH} ]] && wget ${SLEPC4PY_INSTALL_SCRIPT_DOWNLOAD} -O ${SLEPC4PY_INSTALL_SCRIPT_PATH}
    source $SLEPC4PY_INSTALL_SCRIPT_PATH

    # Install itk (and its dependencies)
    ITK_INSTALL_SCRIPT_PATH=${ITK_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/567d867/releases/itk-install.sh"}
    [[ $ITK_INSTALL_SCRIPT_PATH == http* ]] && ITK_INSTALL_SCRIPT_DOWNLOAD=${ITK_INSTALL_SCRIPT_PATH} && ITK_INSTALL_SCRIPT_PATH=/tmp/itk-install.sh && [[ ! -f ${ITK_INSTALL_SCRIPT_PATH} ]] && wget ${ITK_INSTALL_SCRIPT_DOWNLOAD} -O ${ITK_INSTALL_SCRIPT_PATH}
    source $ITK_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    FENICSX_ARCHIVE_PATH=${FENICSX_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/fenicsx-20220219-011351-e8bfbb3-real/fenicsx-install.tar.gz"}
    [[ $FENICSX_ARCHIVE_PATH == http* ]] && FENICSX_ARCHIVE_DOWNLOAD=${FENICSX_ARCHIVE_PATH} && FENICSX_ARCHIVE_PATH=/tmp/fenicsx-install.tar.gz && wget ${FENICSX_ARCHIVE_DOWNLOAD} -O ${FENICSX_ARCHIVE_PATH}
    if [[ $FENICSX_ARCHIVE_PATH != skip ]]; then
        tar -xzf $FENICSX_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $FENICSX_INSTALLED
fi
