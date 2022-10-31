# Copyright (C) 2021-2022 by the FEM on Colab authors
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
MPI4PY_INSTALLED="$SHARE_PREFIX/mpi4py.installed"

if [[ ! -f $MPI4PY_INSTALLED ]]; then
    # Install gcc
    GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/90b9c14/releases/gcc-install.sh"}
    [[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && GCC_INSTALL_SCRIPT_DOWNLOAD=${GCC_INSTALL_SCRIPT_PATH} && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh && [[ ! -f ${GCC_INSTALL_SCRIPT_PATH} ]] && wget ${GCC_INSTALL_SCRIPT_DOWNLOAD} -O ${GCC_INSTALL_SCRIPT_PATH}
    source $GCC_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    MPI4PY_ARCHIVE_PATH=${MPI4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mpi4py-20221031-112036-efa918f/mpi4py-install.tar.gz"}
    [[ $MPI4PY_ARCHIVE_PATH == http* ]] && MPI4PY_ARCHIVE_DOWNLOAD=${MPI4PY_ARCHIVE_PATH} && MPI4PY_ARCHIVE_PATH=/tmp/mpi4py-install.tar.gz && wget ${MPI4PY_ARCHIVE_DOWNLOAD} -O ${MPI4PY_ARCHIVE_PATH}
    if [[ $MPI4PY_ARCHIVE_PATH != skip ]]; then
        tar -xzf $MPI4PY_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Add symbolic links to the MPI libraries in /usr/lib, because INSTALL_PREFIX/lib may not be in LD_LIBRARY_PATH
    # on the actual cloud instance
    if [[ $MPI4PY_ARCHIVE_PATH != skip ]]; then
        ln -fs $INSTALL_PREFIX/lib/libmca*.so* /usr/lib
        ln -fs $INSTALL_PREFIX/lib/libmpi*.so* /usr/lib
        ln -fs $INSTALL_PREFIX/lib/libopen*.so* /usr/lib
        ln -fs $INSTALL_PREFIX/lib/ompi*.so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $MPI4PY_INSTALLED
fi
