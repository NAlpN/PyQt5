# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Web_Sayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Web_Sayfasi(object):
    def setupUi(self, Web_Sayfasi):
        Web_Sayfasi.setObjectName("Web_Sayfasi")
        Web_Sayfasi.resize(400, 302)
        self.label = QtWidgets.QLabel(Web_Sayfasi)
        self.label.setGeometry(QtCore.QRect(130, 120, 81, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Web_Sayfasi)
        QtCore.QMetaObject.connectSlotsByName(Web_Sayfasi)

    def retranslateUi(self, Web_Sayfasi):
        _translate = QtCore.QCoreApplication.translate
        Web_Sayfasi.setWindowTitle(_translate("Web_Sayfasi", "Form"))
        self.label.setText(_translate("Web_Sayfasi", "Web Sayfası"))
