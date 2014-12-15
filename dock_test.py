# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testDock
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

from PyQt4 import QtCore, QtGui
from ui_dock import Ui_DockWidget
import os.path
import sqlite3

# create the dialog for zoom to point

class testDock(QtGui.QDockWidget, Ui_DockWidget):
    def __init__(self):
        QtGui.QDockWidget.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.lineEdit = LineEdit(parent=self.dockWidgetContents)
        self.verticalLayout_4.addWidget(self.lineEdit)

class LineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        # installe le QCompleter
        self.completer = QtGui.QCompleter(self)
        self.completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # installe le model à partir de la liste fournie datas
        model = QtGui.QStandardItemModel()
        #for i, word in enumerate(datas):
        for i, word in enumerate(self.getList()):
            item = QtGui.QStandardItem(word)
            model.setItem(i, 0, item)

        # installe le QSortFilterProxyModel qui s'insère entre le QCompleter et le model
        self.proxymodel = QtGui.QSortFilterProxyModel(self)
        self.proxymodel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxymodel.setSourceModel(model)
        self.completer.setModel(self.proxymodel)

        # chaque changement de texte déclenchera la filtration du model
        self.textChanged.connect(self.proxymodel.setFilterFixedString)

    def getList(self):
        print "fonction getList"
        try:
            # Creates or opens a file called mydb with a SQLite3 DB
            db = sqlite3.connect((os.path.join(os.path.dirname(__file__),'data.sqlite')))
            # Get a cursor object
            cursor = db.cursor()
            # Select
            cursor.execute('SELECT nom FROM proprietaire')
            # Fetch
            data = list()
            for row in cursor.fetchall():
                data.append(row[0])
            print "connexion réussie"
        # Catch the exception
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if db:
                db.close()

        return data