from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


import cae_ui



class Cipher(QDialog, cae_ui.Ui_cae):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFocus()

        self.encrypt.clicked.connect(lambda: self.encrypt_text(1))
        self.decrypt.clicked.connect(lambda: self.encrypt_text(-1))


    cip_dic = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n",
               14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}


    def encrypt_text(self, flag):
        temp = 0
        enc_out = ""
        enc_text = self.textBox_enc.text()
        off = int(self.offset.text())*flag
        for i in range(len(enc_text)):
            if enc_text[i]!=" ":
                for key, value in self.cip_dic.items():
                    if value==enc_text[i]:
                        temp = key
                        break
                temp = (temp+off)%26
                enc_out+=self.cip_dic[temp]
            else:
                enc_out+=" "
        self.textBox_enc_2.setText(enc_out)



app = QApplication(sys.argv)
cipher = Cipher()
cipher.show()
app.exec_()




