# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cae_cip.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cae(object):
    def setupUi(self, cae):
        cae.setObjectName("cae")
        cae.resize(462, 180)
        cae.setSizeGripEnabled(False)
        cae.setModal(False)
        self.formLayout = QtWidgets.QFormLayout(cae)
        self.formLayout.setObjectName("formLayout")
        self.text_enc = QtWidgets.QLabel(cae)
        self.text_enc.setObjectName("text_enc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.text_enc)
        self.textBox_enc = QtWidgets.QLineEdit(cae)
        self.textBox_enc.setObjectName("textBox_enc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textBox_enc)
        self.label_2 = QtWidgets.QLabel(cae)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.offset = QtWidgets.QLineEdit(cae)
        self.offset.setObjectName("offset")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.offset)
        self.encrypt = QtWidgets.QPushButton(cae)
        self.encrypt.setObjectName("encrypt")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.encrypt)
        self.decrypt = QtWidgets.QPushButton(cae)
        self.decrypt.setObjectName("decrypt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.decrypt)
        self.label = QtWidgets.QLabel(cae)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textBox_enc_2 = QtWidgets.QLineEdit(cae)
        self.textBox_enc_2.setObjectName("textBox_enc_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textBox_enc_2)

        self.retranslateUi(cae)
        QtCore.QMetaObject.connectSlotsByName(cae)

    def retranslateUi(self, cae):
        _translate = QtCore.QCoreApplication.translate
        cae.setWindowTitle(_translate("cae", "Caesar\'s Cipher"))
        self.text_enc.setText(_translate("cae", "Text:"))
        self.textBox_enc.setPlaceholderText(_translate("cae", "Enter text to be modified"))
        self.label_2.setText(_translate("cae", "Offset:"))
        self.offset.setText(_translate("cae", "0"))
        self.offset.setPlaceholderText(_translate("cae", "Enter Offset"))
        self.encrypt.setText(_translate("cae", "Encrypt"))
        self.decrypt.setText(_translate("cae", "Decrypt"))
        self.label.setText(_translate("cae", "Output:"))
        self.textBox_enc_2.setPlaceholderText(_translate("cae", "Your modified text"))

