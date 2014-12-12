# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test.ui'
#
# Created: Fri Dec 12 10:52:54 2014
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

class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName(_fromUtf8("test"))
        test.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(test)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.cbxProprio = QtGui.QComboBox(test)
        self.cbxProprio.setGeometry(QtCore.QRect(10, 20, 381, 27))
        self.cbxProprio.setEditable(True)
        self.cbxProprio.setObjectName(_fromUtf8("cbxProprio"))
        self.btnTest = QtGui.QPushButton(test)
        self.btnTest.setGeometry(QtCore.QRect(30, 240, 87, 27))
        self.btnTest.setCheckable(False)
        self.btnTest.setObjectName(_fromUtf8("btnTest"))
        self.lwgResult = QtGui.QListWidget(test)
        self.lwgResult.setGeometry(QtCore.QRect(10, 50, 381, 141))
        self.lwgResult.setObjectName(_fromUtf8("lwgResult"))

        self.retranslateUi(test)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), test.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), test.reject)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        test.setWindowTitle(_translate("test", "test", None))
        self.btnTest.setText(_translate("test", "test", None))

