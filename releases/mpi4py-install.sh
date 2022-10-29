# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
SHARE_PREFIX="/usr/local/share/fem-on-colab"
MPI4PY_INSTALLED="$SHARE_PREFIX/mpi4py.installed"

if [[ ! -f $MPI4PY_INSTALLED ]]; then
    # Install gcc
    GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/f316960/releases/gcc-install.sh"}
    [[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && GCC_INSTALL_SCRIPT_DOWNLOAD=${GCC_INSTALL_SCRIPT_PATH} && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh && [[ ! -f ${GCC_INSTALL_SCRIPT_PATH} ]] && wget ${GCC_INSTALL_SCRIPT_DOWNLOAD} -O ${GCC_INSTALL_SCRIPT_PATH}
    source $GCC_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    MPI4PY_ARCHIVE_PATH=${MPI4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mpi4py-20221029-085103-cb94ed3/mpi4py-install.tar.gz"}
    [[ $MPI4PY_ARCHIVE_PATH == http* ]] && MPI4PY_ARCHIVE_DOWNLOAD=${MPI4PY_ARCHIVE_PATH} && MPI4PY_ARCHIVE_PATH=/tmp/mpi4py-install.tar.gz && wget ${MPI4PY_ARCHIVE_DOWNLOAD} -O ${MPI4PY_ARCHIVE_PATH}
    if [[ $MPI4PY_ARCHIVE_PATH != skip ]]; then
        tar -xzf $MPI4PY_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
    fi

    # Add symbolic links to the MPI libraries in /usr/lib, because Colab does not export /usr/local/lib to LD_LIBRARY_PATH
    if [[ $MPI4PY_ARCHIVE_PATH != skip ]]; then
        ln -fs /usr/local/lib/libmca*.so* /usr/lib
        ln -fs /usr/local/lib/libmpi*.so* /usr/lib
        ln -fs /usr/local/lib/libopen*.so* /usr/lib
        ln -fs /usr/local/lib/ompi*.so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $MPI4PY_INSTALLED
fi
