# Copyright (C) 2021-2025 by the FEM on Colab authors
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
H5PY_INSTALLED="$SHARE_PREFIX/h5py.installed"

if [[ ! -f $H5PY_INSTALLED ]]; then
    # Install mpi4py
    MPI4PY_INSTALL_SCRIPT_PATH=${MPI4PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/bf409ff8/releases/mpi4py-install.sh"}
    [[ $MPI4PY_INSTALL_SCRIPT_PATH == http* ]] && MPI4PY_INSTALL_SCRIPT_DOWNLOAD=${MPI4PY_INSTALL_SCRIPT_PATH} && MPI4PY_INSTALL_SCRIPT_PATH=/tmp/mpi4py-install.sh && [[ ! -f ${MPI4PY_INSTALL_SCRIPT_PATH} ]] && wget ${MPI4PY_INSTALL_SCRIPT_DOWNLOAD} -O ${MPI4PY_INSTALL_SCRIPT_PATH}
    source $MPI4PY_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    H5PY_ARCHIVE_PATH=${H5PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/h5py-20250820-191509-d9fc5d1/h5py-install.tar.gz"}
    [[ $H5PY_ARCHIVE_PATH == http* ]] && H5PY_ARCHIVE_DOWNLOAD=${H5PY_ARCHIVE_PATH} && H5PY_ARCHIVE_PATH=/tmp/h5py-install.tar.gz && wget ${H5PY_ARCHIVE_DOWNLOAD} -O ${H5PY_ARCHIVE_PATH}
    if [[ $H5PY_ARCHIVE_PATH != skip ]]; then
        rm -rf /usr/lib/python*/*-packages/h5py*
        rm -rf $INSTALL_PREFIX/lib/python*/*-packages/h5py*
        tar -xzf $H5PY_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $H5PY_INSTALLED
fi
