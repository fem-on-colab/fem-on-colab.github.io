# Copyright (C) 2021-2025 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

# Use a mock package to keep track of how many users are still trying to download FEniCSx from the legacy URL
wget -O/dev/null -q https://github.com/fem-on-colab/fem-on-colab/releases/download/mock-20250301-014240-a52042e/mock-install.tar.gz

cat << EOF




























#################################################################################
#                                                                               #
#         The installation script for FEniCSx has been moved from               #
#        https://fem-on-colab.github.io/releases/fenicsx-install-real.sh        #
#                  to either of the following URLs                              #
#        1) if interested in the latest FEniCSx release, please use             #
# https://fem-on-colab.github.io/releases/fenicsx-install-release-real.sh       #
#                 (note the additional "-release-" in the URL).                 #
#        2) if interested in FEniCSx development version, please use            #
# https://fem-on-colab.github.io/releases/fenicsx-install-development-real.sh   #
#                 (note the additional "-development-" in the URL).             #
#                                                                               #
#   Please update your installation cell. Report issues at our issue tracker    #
#           https://github.com/fem-on-colab/fem-on-colab/issues                 #
#                                                                               #
#################################################################################




























EOF
sleep 2; kill -9 `ps --pid $$ -oppid=`; exit
