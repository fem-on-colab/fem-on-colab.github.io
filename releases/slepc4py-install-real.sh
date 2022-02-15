# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
SHARE_PREFIX="/usr/local/share/fem-on-colab"
SLEPC4PY_INSTALLED="$SHARE_PREFIX/slepc4py.installed"

if [[ ! -f $SLEPC4PY_INSTALLED ]]; then
    # Install petsc4py (and its dependencies)
    PETSC4PY_INSTALL_SCRIPT_PATH=${PETSC4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/e35b204/releases/petsc4py-install-real.sh"}
    [[ $PETSC4PY_INSTALL_SCRIPT_PATH == http* ]] && wget -N ${PETSC4PY_INSTALL_SCRIPT_PATH} -O /tmp/petsc4py-install.sh && PETSC4PY_INSTALL_SCRIPT_PATH=/tmp/petsc4py-install.sh
    source $PETSC4PY_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    SLEPC4PY_ARCHIVE_PATH=${SLEPC4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/slepc4py-20220215-210251-f21c5aa-real/slepc4py-install.tar.gz"}
    [[ $SLEPC4PY_ARCHIVE_PATH == http* ]] && wget -N ${SLEPC4PY_ARCHIVE_PATH} -O /tmp/slepc4py-install.tar.gz && SLEPC4PY_ARCHIVE_PATH=/tmp/slepc4py-install.tar.gz
    if [[ $SLEPC4PY_ARCHIVE_PATH != skip ]]; then
        tar -xzf $SLEPC4PY_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $SLEPC4PY_INSTALLED
fi
