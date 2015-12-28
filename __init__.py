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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Model Data Utility" 
def description():
  return "Provides spatial context for downloading observed data for model input and calibration."
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "2.0"
def classFactory(iface): 
  # load ModelDataUtility class from file ModelDataUtility
  from ModelDataUtility import ModelDataUtility 
  return ModelDataUtility(iface)
