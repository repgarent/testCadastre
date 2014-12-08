# -*- coding: utf-8 -*-
"""
/***************************************************************************
 test
                                 A QGIS plugin
 plugin de test
                             -------------------
        begin                : 2014-11-03
        copyright            : (C) 2014 by alexis
        email                : repgarent@gmail.com
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

def classFactory(iface):
    # load test class from file test
    from test import test
    return test(iface)
