# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Install pybind11
PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/e270331/releases/pybind11-install.sh"}
[[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && wget ${PYBIND11_INSTALL_SCRIPT_PATH} -O /tmp/pybind11-install.sh && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh
source $PYBIND11_INSTALL_SCRIPT_PATH

# Install boost (and its dependencies)
BOOST_INSTALL_SCRIPT_PATH=${BOOST_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/5edcc61/releases/boost-install.sh"}
[[ $BOOST_INSTALL_SCRIPT_PATH == http* ]] && wget ${BOOST_INSTALL_SCRIPT_PATH} -O /tmp/boost-install.sh && BOOST_INSTALL_SCRIPT_PATH=/tmp/boost-install.sh
source $BOOST_INSTALL_SCRIPT_PATH

# Install slepc4py (and its dependencies)
SLEPC4PY_INSTALL_SCRIPT_PATH=${SLEPC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/cd7971e/releases/slepc4py-install-real.sh"}
[[ $SLEPC4PY_INSTALL_SCRIPT_PATH == http* ]] && wget ${SLEPC4PY_INSTALL_SCRIPT_PATH} -O /tmp/slepc4py-install.sh && SLEPC4PY_INSTALL_SCRIPT_PATH=/tmp/slepc4py-install.sh
source $SLEPC4PY_INSTALL_SCRIPT_PATH

# Download and uncompress library archive
FIREDRAKE_ARCHIVE_PATH=${FIREDRAKE_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/firedrake-20220110-092734-2602f12/firedrake-install.tar.gz"}
[[ $FIREDRAKE_ARCHIVE_PATH == http* ]] && wget ${FIREDRAKE_ARCHIVE_PATH} -O /tmp/firedrake-install.tar.gz && FIREDRAKE_ARCHIVE_PATH=/tmp/firedrake-install.tar.gz
if [[ $FIREDRAKE_ARCHIVE_PATH != skip ]]; then
    rm -rf /usr/local/lib/python3.7/dist-packages/cftime*
    rm -rf /usr/local/lib/python3.7/dist-packages/networkx*
    rm -rf /usr/local/lib/python3.7/dist-packages/netCDF4*
    tar -xzf $FIREDRAKE_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
fi
