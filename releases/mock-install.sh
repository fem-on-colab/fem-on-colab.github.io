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
MOCK_INSTALLED="$SHARE_PREFIX/mock.installed"

if [[ ! -f $MOCK_INSTALLED ]]; then
    # Download and uncompress library archive
    MOCK_ARCHIVE_PATH=${MOCK_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mock-20221103-131037-d6a34cb/mock-install.tar.gz"}
    [[ $MOCK_ARCHIVE_PATH == http* ]] && MOCK_ARCHIVE_DOWNLOAD=${MOCK_ARCHIVE_PATH} && MOCK_ARCHIVE_PATH=/tmp/mock-install.tar.gz && wget ${MOCK_ARCHIVE_DOWNLOAD} -O ${MOCK_ARCHIVE_PATH}
    tar -xzf $MOCK_ARCHIVE_PATH --strip-components=$INSTALL_PREFIX_DEPTH --directory=$INSTALL_PREFIX

    # Mark package as installed
    mkdir -p $SHARE_PREFIX
    touch $MOCK_INSTALLED
fi
set +x
cat << EOF
################################################################################
#     This installation is offered by FEM on Colab, an open-source project     #
#       developed and maintained at Università Cattolica del Sacro Cuore       #
#    by Dr. Francesco Ballarin. Please see https://fem-on-colab.github.io/     #
#       for more details, including a list of further available packages       #
#                    and how to contribute to the project.                     #
#                                                                              #
#   We are conducting an informal survey on FEM on Colab usage by our users.   #
#   The survey is anonymous, and its compilation will typically only require   #
#   a couple of minutes of your time. If you wish, give us your feedback at    #
#                     https://forms.gle/36sZZWNvPpUv8XWr7                      #
################################################################################
EOF
set -x
