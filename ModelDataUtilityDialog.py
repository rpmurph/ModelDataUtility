"""
/***************************************************************************
Name			 	 : Model Data Utility
Description          : Provides spatial context for downloading observed data for model input and calibration.
Date                 : 28/Dec/15 
copyright            : (C) 2015 by Paradigm Environmental
email                : ryan.murphy@paradigmh2o.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_ModelDataUtility import Ui_ModelDataUtility
# create the dialog for ModelDataUtility
class ModelDataUtilityDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ModelDataUtility ()
    self.ui.setupUi(self)