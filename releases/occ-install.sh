# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Check for existing installation
SHARE_PREFIX="/usr/local/share/fem-on-colab"
OCC_INSTALLED="$SHARE_PREFIX/occ.installed"

if [[ ! -f $OCC_INSTALLED ]]; then
    # Install gcc
    GCC_INSTALL_SCRIPT_PATH=${GCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/fabd340/releases/gcc-install.sh"}
    [[ $GCC_INSTALL_SCRIPT_PATH == http* ]] && wget -N ${GCC_INSTALL_SCRIPT_PATH} -O /tmp/gcc-install.sh && GCC_INSTALL_SCRIPT_PATH=/tmp/gcc-install.sh
    source $GCC_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    OCC_ARCHIVE_PATH=${OCC_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/occ-20220215-201811-f21c5aa/occ-install.tar.gz"}
    [[ $OCC_ARCHIVE_PATH == http* ]] && wget -N ${OCC_ARCHIVE_PATH} -O /tmp/occ-install.tar.gz && OCC_ARCHIVE_PATH=/tmp/occ-install.tar.gz
    if [[ $OCC_ARCHIVE_PATH != skip ]]; then
        tar -xzf $OCC_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
    fi

    # Add symbolic links to TK libraries in /usr/lib, because Colab does not export /usr/local/lib to LD_LIBRARY_PATH
    if [[ $OCC_ARCHIVE_PATH != skip ]]; then
        ln -fs /usr/local/lib/libTK*.so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $OCC_INSTALLED
fi
