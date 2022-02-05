# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Install OCC
OCC_INSTALL_SCRIPT_PATH=${OCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/fd62cb0/releases/occ-install.sh"}
[[ $OCC_INSTALL_SCRIPT_PATH == http* ]] && wget ${OCC_INSTALL_SCRIPT_PATH} -O /tmp/occ-install.sh && OCC_INSTALL_SCRIPT_PATH=/tmp/occ-install.sh
source $OCC_INSTALL_SCRIPT_PATH

# Install pybind11
PYBIND11_INSTALL_SCRIPT_PATH=${PYBIND11_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/e270331/releases/pybind11-install.sh"}
[[ $PYBIND11_INSTALL_SCRIPT_PATH == http* ]] && wget ${PYBIND11_INSTALL_SCRIPT_PATH} -O /tmp/pybind11-install.sh && PYBIND11_INSTALL_SCRIPT_PATH=/tmp/pybind11-install.sh
source $PYBIND11_INSTALL_SCRIPT_PATH

# Install petsc4py (and its dependencies)
PETSC4PY_INSTALL_SCRIPT_PATH=${PETSC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/3cd6a50/releases/petsc4py-install-real.sh"}
[[ $PETSC4PY_INSTALL_SCRIPT_PATH == http* ]] && wget ${PETSC4PY_INSTALL_SCRIPT_PATH} -O /tmp/petsc4py-install.sh && PETSC4PY_INSTALL_SCRIPT_PATH=/tmp/petsc4py-install.sh
source $PETSC4PY_INSTALL_SCRIPT_PATH

# Download and uncompress library archive
NGSOLVE_ARCHIVE_PATH=${NGSOLVE_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/ngsolve-20220205-001335-6710630/ngsolve-install.tar.gz"}
[[ $NGSOLVE_ARCHIVE_PATH == http* ]] && wget ${NGSOLVE_ARCHIVE_PATH} -O /tmp/ngsolve-install.tar.gz && NGSOLVE_ARCHIVE_PATH=/tmp/ngsolve-install.tar.gz
if [[ $NGSOLVE_ARCHIVE_PATH != skip ]]; then
    tar -xzf $NGSOLVE_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
fi

# Install X11 for ngsolve
apt install -y -qq libfontconfig1 libgl1
