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
ITK_INSTALLED="$SHARE_PREFIX/itk.installed"

if [[ ! -f $ITK_INSTALLED ]]; then
    # Install vtk
    VTK_INSTALL_SCRIPT_PATH=${VTK_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/f62d03d/releases/vtk-install.sh"}
    [[ $VTK_INSTALL_SCRIPT_PATH == http* ]] && VTK_INSTALL_SCRIPT_DOWNLOAD=${VTK_INSTALL_SCRIPT_PATH} && VTK_INSTALL_SCRIPT_PATH=/tmp/vtk-install.sh && [[ ! -f ${VTK_INSTALL_SCRIPT_PATH} ]] && wget ${VTK_INSTALL_SCRIPT_DOWNLOAD} -O ${VTK_INSTALL_SCRIPT_PATH}
    source $VTK_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    ITK_ARCHIVE_PATH=${ITK_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/itk-20221202-195804-1f8b405/itk-install.tar.gz"}
    [[ $ITK_ARCHIVE_PATH == http* ]] && ITK_ARCHIVE_DOWNLOAD=${ITK_ARCHIVE_PATH} && ITK_ARCHIVE_PATH=/tmp/itk-install.tar.gz && wget ${ITK_ARCHIVE_DOWNLOAD} -O ${ITK_ARCHIVE_PATH}
    if [[ $ITK_ARCHIVE_PATH != skip ]]; then
        tar -xzf $ITK_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $ITK_INSTALLED
fi
