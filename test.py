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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from testdialog import testDialog
from dock_test import *
import os.path
import sqlite3
import unicodedata


class test(object):

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'test_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
 
        #Create the Dockwiget (after translation) and keep reference
        self.dwg = testDock()
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dwg)


    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/test/icon.png"),
            u"Test", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Test", self.action)

        #remplissage de la letRecherche
        self.dwg.letRecherche.textChanged.connect(self.letRechercheChange)
        
    def letRechercheChange(self, text):
        #on vide la liste d'affichage  
        self.dwg.lwgResult.clear()
        if not text:
            pass
        else:
            text2=self.suppression_diacritics(text)
            #connexion a la DB
            db = sqlite3.connect(os.path.join(os.path.dirname(__file__),'data.sqlite'))
            cursor = db.cursor()
            #on recherche les correspondances dans la colonne nom
            cursor.execute("SELECT nom FROM proprietaire where nom like ?", ('%' + text + '%', ))
            #on remplit la liste d'affichage
            for row in cursor.fetchall():
                self.dwg.lwgResult.addItem(row[0])
            cursor.execute("SELECT nom FROM proprietaire where nom like ?", ('%' + text2 + '%', ))
            for row in cursor.fetchall():
                self.dwg.lwgResult.addItem(row[0])

    def suppression_diacritics(self, s):
        def remove(char):
            deco = unicodedata.decomposition(char)
            if deco:
                return unichr(int(deco.split()[0],16))
            return char
        return ''.join([remove(a) for a in s])

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Test", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        # self.dlg.show()
        # Run the dialog event loop
        result = 1
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dwg)
