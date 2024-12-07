# Copyright (C) 2021-2024 by the FEM on Colab authors
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
GMSH_INSTALLED="$SHARE_PREFIX/gmsh.installed"

if [[ ! -f $GMSH_INSTALLED ]]; then
    # Install h5py (and its dependencies, most notably gcc and mpi4py)
    H5PY_INSTALL_SCRIPT_PATH=${H5PY_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/bc474259/releases/h5py-install.sh"}
    [[ $H5PY_INSTALL_SCRIPT_PATH == http* ]] && H5PY_INSTALL_SCRIPT_DOWNLOAD=${H5PY_INSTALL_SCRIPT_PATH} && H5PY_INSTALL_SCRIPT_PATH=/tmp/h5py-install.sh && [[ ! -f ${H5PY_INSTALL_SCRIPT_PATH} ]] && wget ${H5PY_INSTALL_SCRIPT_DOWNLOAD} -O ${H5PY_INSTALL_SCRIPT_PATH}
    source $H5PY_INSTALL_SCRIPT_PATH

    # Install OCC (and its dependencies, most notably gcc)
    OCC_INSTALL_SCRIPT_PATH=${OCC_INSTALL_SCRIPT_PATH:-"https://github.com/fem-on-colab/fem-on-colab.github.io/raw/a10a5545/releases/occ-install.sh"}
    [[ $OCC_INSTALL_SCRIPT_PATH == http* ]] && OCC_INSTALL_SCRIPT_DOWNLOAD=${OCC_INSTALL_SCRIPT_PATH} && OCC_INSTALL_SCRIPT_PATH=/tmp/occ-install.sh && [[ ! -f ${OCC_INSTALL_SCRIPT_PATH} ]] && wget ${OCC_INSTALL_SCRIPT_DOWNLOAD} -O ${OCC_INSTALL_SCRIPT_PATH}
    source $OCC_INSTALL_SCRIPT_PATH

    # Download and uncompress library archive
    GMSH_ARCHIVE_PATH=${GMSH_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/gmsh-20241207-014119-e11a96a/gmsh-install.tar.gz"}
    [[ $GMSH_ARCHIVE_PATH == http* ]] && GMSH_ARCHIVE_DOWNLOAD=${GMSH_ARCHIVE_PATH} && GMSH_ARCHIVE_PATH=/tmp/gmsh-install.tar.gz && wget ${GMSH_ARCHIVE_DOWNLOAD} -O ${GMSH_ARCHIVE_PATH}
    if [[ $GMSH_ARCHIVE_PATH != skip ]]; then
        tar -xzf $GMSH_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX
    fi

    # Add symbolic links to gmsh libraries in /usr/lib, because INSTALL_PREFIX/lib may not be in LD_LIBRARY_PATH
    # on the actual cloud instance
    if [[ $GMSH_ARCHIVE_PATH != skip ]]; then
        ln -fs $INSTALL_PREFIX/lib/libgmsh*.so* /usr/lib
    fi

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $GMSH_INSTALLED
fi

# Display end user packages announcement
set +x
cat << EOF
























################################################################################
#     This installation is offered by FEM on Colab, an open-source project     #
#       developed and maintained at Università Cattolica del Sacro Cuore       #
#   by Prof. Francesco Ballarin. Please see https://fem-on-colab.github.io/    #
#       for more details, including a list of further available packages       #
#       and how to sponsor the development or contribute to the project.       #
#                                                                              #
#   We are conducting an informal survey on FEM on Colab usage by our users.   #
#   The survey is anonymous, and its compilation will typically only require   #
#   a couple of minutes of your time. If you wish, give us your feedback at    #
#                     https://forms.gle/36sZZWNvPpUv8XWr7                      #
################################################################################
























EOF
set -x
