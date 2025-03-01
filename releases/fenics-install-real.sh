# Copyright (C) 2021-2025 by the FEM on Colab authors
#
# This file is part of FEM on Colab.
#
# SPDX-License-Identifier: MIT

# Use a mock package to keep track of how many users are still trying to download FEniCS from the legacy URL
wget -O/dev/null -q https://github.com/fem-on-colab/fem-on-colab/releases/download/mock-20250301-180649-d4ec134/mock-install.tar.gz

cat << EOF




























################################################################################
#                                                                              #
#         The installation script for legacy FEniCS has been moved from        #
#        https://fem-on-colab.github.io/releases/fenics-install-real.sh        #
#                                      to                                      #
#    https://fem-on-colab.github.io/releases/fenics-install-release-real.sh    #
#                 (note the additional "-release-" in the URL).                #
#                                                                              #
#   Please update your installation cell. Report issues at our issue tracker   #
#           https://github.com/fem-on-colab/fem-on-colab/issues                #
#                                                                              #
################################################################################




























EOF
sleep 2; kill -9 `ps --pid $$ -oppid=`; exit
