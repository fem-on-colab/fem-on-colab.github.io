# Copyright (C) 2021-2022 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

set -e
set -x

# Download and uncompress library archive
MOCK_ARCHIVE_PATH=${MOCK_ARCHIVE_PATH:-"https://github.com/fem-on-colab/fem-on-colab/releases/download/mock-20220115-001631-4a192c2/mock-install.tar.gz"}
[[ $MOCK_ARCHIVE_PATH == http* ]] && wget ${MOCK_ARCHIVE_PATH} -O /tmp/mock-install.tar.gz && MOCK_ARCHIVE_PATH=/tmp/mock-install.tar.gz
tar -xzf $MOCK_ARCHIVE_PATH --strip-components=2 --directory=/usr/local
