# Copyright (C) 2021-2024 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

# Use a mock package to keep track of how many users are still trying to download NGSolve from the legacy URL
wget -O/dev/null -q https://github.com/fem-on-colab/fem-on-colab/releases/download/mock-20240112-172055-b78c48e/mock-install.tar.gz

cat << EOF




























################################################################################
#                                                                              #
#           The installation script for ngsolve has been moved from            #
#        https://fem-on-colab.github.io/releases/ngsolve-install.sh            #
#                                      to                                      #
#      https://fem-on-colab.github.io/releases/ngsolve-install-real.sh         #
#                   (note the additional "-real" in the URL).                  #
#                                                                              #
#   Please update your installation cell. Report issues at our issue tracker   #
#           https://github.com/fem-on-colab/fem-on-colab/issues                #
#                                                                              #
################################################################################




























EOF
sleep 2; kill -9 `ps --pid $$ -oppid=`; exit
