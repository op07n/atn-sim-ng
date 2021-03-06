#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------
atn-sim-gui

GUI do simulador ATN

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

revision 0.1  2017/March  matias
initial release (Linux/Python)
---------------------------------------------------------------------------------------------------
"""
__version__ = "$revision: 0.1$"
__author__ = "Ivan Matias"
__date__ = "2017/03"

# < imports >--------------------------------------------------------------------------------------

# python library
import logging
import sys

# PyQt library
from PyQt4 import QtGui

# atn_sim_mngr
import atn_sim_mngr as atn

# < module data >----------------------------------------------------------------------------------

# logger
M_LOG_FILE = "atn-sim-gui.log"
M_LOG_LEVEL = logging.DEBUG

# -------------------------------------------------------------------------------------------------
def main():
    """
    initalize and kick off the main loop
    """
    logger = logging.getLogger('main_app')

    # create application
    l_app = QtGui.QApplication(sys.argv)
    assert l_app

    # create ATN manager
    logger.info("Creating the ATN simulator manager")
    l_atn_mngr = atn.CATNSimMngr()
    assert l_atn_mngr

    # show interface
    logger.info("Show the ATN simulator GUI")
    l_atn_mngr.show_gui()

    # run interface
    sys.exit(l_app.exec_())
    logger.info("Exit app")

# -------------------------------------------------------------------------------------------------
# this is the bootstrap process

if "__main__" == __name__:

    # logger
    logging.basicConfig(filename=M_LOG_FILE, level=M_LOG_LEVEL,filemode='w',
                        format='%(asctime)s %(levelname)s: %(message)s')

    # run application
    main()

# < the end >--------------------------------------------------------------------------------------