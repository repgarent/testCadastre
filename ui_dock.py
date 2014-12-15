# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dock.ui'
#
# Created: Mon Dec 15 12:06:04 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(593, 911)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.letRecherche = QtGui.QLineEdit(self.groupBox)
        self.letRecherche.setObjectName(_fromUtf8("letRecherche"))
        self.verticalLayout.addWidget(self.letRecherche)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lwgResult = QtGui.QListWidget(self.groupBox)
        self.lwgResult.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lwgResult.setMovement(QtGui.QListView.Static)
        self.lwgResult.setObjectName(_fromUtf8("lwgResult"))
        self.verticalLayout.addWidget(self.lwgResult)
        spacerItem = QtGui.QSpacerItem(20, 500, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Outil de recherche", None))
        self.groupBox_3.setTitle(_translate("DockWidget", "Recherche de propriétaire", None))
        self.groupBox.setTitle(_translate("DockWidget", "lineEdit+listWidget", None))
        self.label.setText(_translate("DockWidget", "Entrez votre recherche", None))
        self.label_2.setText(_translate("DockWidget", "Les résultat s\'afficheront ici", None))

