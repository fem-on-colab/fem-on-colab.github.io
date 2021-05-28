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

# Patch MPI to load libstdc++ from the newest gcc
apt install -y -qq patchelf
patchelf --set-rpath "/usr/local/lib:/usr/lib/x86_64-linux-gnu/openmpi/lib:/usr/lib/gcc/x86_64-linux-gnu/11:/usr/lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu" /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so

# Download and uncompress library archive
MPI4PY_ARCHIVE_PATH=${MPI4PY_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mpi4py-20210528-175037-88a572b/mpi4py-install.tar.gz"}
[[ $MPI4PY_ARCHIVE_PATH == http* ]] && wget ${MPI4PY_ARCHIVE_PATH} -O /tmp/mpi4py-install.tar.gz && MPI4PY_ARCHIVE_PATH=/tmp/mpi4py-install.tar.gz
[[ $MPI4PY_ARCHIVE_PATH != skip ]] && tar -xzf $MPI4PY_ARCHIVE_PATH --strip-components=2 --directory=/usr/local || true
