# Copyright (C) 2021 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Install gcc
GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://fem-on-colab.github.io/releases/gcc-install.sh"}
[[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && wget ${GCC_INSTALL_SCRIPT_PATH} -O /tmp/gcc-install.sh && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh
source $GCC_INSTALL_SCRIPT_PATH

# Install MPI
add-apt-repository -y ppa:marmistrz/openmpi
apt update
apt install -y -qq libopenmpi-dev

# Download and uncompress library archive
MPI4PY_ARCHIVE_PATH=${MPI4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mpi4py-20210527-123923-a1f30c0/mpi4py-install.tar.gz"}
[[ $MPI4PY_ARCHIVE_PATH == http* ]] && wget ${MPI4PY_ARCHIVE_PATH} -O /tmp/mpi4py-install.tar.gz && MPI4PY_ARCHIVE_PATH=/tmp/mpi4py-install.tar.gz
[[ $MPI4PY_ARCHIVE_PATH != skip ]] && tar -xzf $MPI4PY_ARCHIVE_PATH --strip-components=2 --directory=/usr/local || true
