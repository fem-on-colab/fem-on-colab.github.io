# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Install gcc
GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/84e52a2/releases/gcc-install.sh"}
[[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && wget ${GCC_INSTALL_SCRIPT_PATH} -O /tmp/gcc-install.sh && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh
source $GCC_INSTALL_SCRIPT_PATH

# Download and uncompress library archive
OCC_ARCHIVE_PATH=${OCC_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/occ-20220110-153551-8a6ff99/occ-install.tar.gz"}
[[ $OCC_ARCHIVE_PATH == http* ]] && wget ${OCC_ARCHIVE_PATH} -O /tmp/occ-install.tar.gz && OCC_ARCHIVE_PATH=/tmp/occ-install.tar.gz
if [[ $OCC_ARCHIVE_PATH != skip ]]; then
    tar -xzf $OCC_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
fi

# Add symbolic links to TK libraries in /usr/lib, because Colab does not export /usr/local/lib to LD_LIBRARY_PATH
if [[ $OCC_ARCHIVE_PATH != skip ]]; then
    ln -fs /usr/local/lib/libTK*.so* /usr/lib
fi
