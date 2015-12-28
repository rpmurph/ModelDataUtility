# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_ModelDataUtility.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ModelDataUtility(object):
    def setupUi(self, ModelDataUtility):
        ModelDataUtility.setObjectName("ModelDataUtility")
        ModelDataUtility.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(ModelDataUtility)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(ModelDataUtility)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ModelDataUtility.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ModelDataUtility.reject)
        QtCore.QMetaObject.connectSlotsByName(ModelDataUtility)

    def retranslateUi(self, ModelDataUtility):
        ModelDataUtility.setWindowTitle(QtGui.QApplication.translate("ModelDataUtility", "ModelDataUtility", None, QtGui.QApplication.UnicodeUTF8))
