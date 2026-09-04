# Copyright (C) 2021-2026 by the FEM on Colab authors
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
BOOST_INSTALLED="$SHARE_PREFIX/boost.installed"

if [[ ! -f $BOOST_INSTALLED ]]; then
    # Download and uncompress library archive
    BOOST_ARCHIVE_PATH=${BOOST_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/staging-boost-20260904-080755-0be0e98/boost-install.tar.gz"}
    [[ $BOOST_ARCHIVE_PATH == http* ]] && BOOST_ARCHIVE_DOWNLOAD=${BOOST_ARCHIVE_PATH} && BOOST_ARCHIVE_PATH=/tmp/boost-install.tar.gz && wget ${BOOST_ARCHIVE_DOWNLOAD} -O ${BOOST_ARCHIVE_PATH}
    if [[ $BOOST_ARCHIVE_PATH != skip ]]; then
        tar -xzf $BOOST_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Add symbolic links to the MPI libraries in /usr/lib, because INSTALL_PREFIX/lib may not be in LD_LIBRARY_PATH
    # on the actual cloud instance
    if [[ $BOOST_ARCHIVE_PATH != skip ]]; then
        ln -fs $INSTALL_PREFIX/lib/libboost*so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $BOOST_INSTALLED
fi
