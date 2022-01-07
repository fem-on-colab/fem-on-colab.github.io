# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Install gcc
GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/7a3dea8/releases/gcc-install.sh"}
[[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && wget ${GCC_INSTALL_SCRIPT_PATH} -O /tmp/gcc-install.sh && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh
source $GCC_INSTALL_SCRIPT_PATH

# Download and uncompress library archive
MPI4PY_ARCHIVE_PATH=${MPI4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mpi4py-20220107-165441-ef21dd8/mpi4py-install.tar.gz"}
[[ $MPI4PY_ARCHIVE_PATH == http* ]] && wget ${MPI4PY_ARCHIVE_PATH} -O /tmp/mpi4py-install.tar.gz && MPI4PY_ARCHIVE_PATH=/tmp/mpi4py-install.tar.gz
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
