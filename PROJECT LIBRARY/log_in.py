# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is


from PyQt5 import QtCore, QtGui, QtWidgets

from welcome import welcome

class Ui_pass_window(object):
           
    def open_welcome(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.username=='ap_tharki' and self.password=='369':
                self.window = QtWidgets.QMainWindow()
                self.ui = welcome()
      
                self.ui.setupUi(self.window)
                self.window.show()
                pass_window.close() 

         
        
        

    def setupUi(self, pass_window):
        pass_window.setObjectName("pass_window")
        pass_window.resize(799, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/library-logo-design-template-45579f2f9eaf725821b915b523f191eb_screen.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pass_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(pass_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 811, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/library.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 491, 371))
        self.label_2.setStyleSheet("background-color:rgb(255, 97, 100);\n"
"color: rgb(255, 73, 76);\n"
"border-radius:20px;\n"
"opacity:0.6;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 491, 101))
        self.label_3.setStyleSheet("color:rgb(255, 0, 0);\n"
"font-size:19px;\n"
"background:rgb(240, 255, 74);\n"
"\n"
"font: 20pt \"MV Boli\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 290, 111, 31))
        self.label_4.setStyleSheet("font: 14px;\n"
"color:black;\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 390, 111, 31))
        self.label_5.setStyleSheet("font: 14px;\n"
"color:black;\n"
"font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 270, 291, 71))
        self.label_6.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"border-color:rgb(149, 0, 255);\n"
"border")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 370, 291, 71))
        self.label_7.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"border-color:rgb(149, 0, 255);\n"
"border")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 289, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 389, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 30, 91, 81))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/Logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 10, 151, 131))
        self.label_9.setStyleSheet("background-color:rgb(2, 255, 32);\n"
"border-radius:60px")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.open_welcome())
        self.pushButton.setGeometry(QtCore.QRect(380, 450, 75, 23))
        self.pushButton.setStyleSheet("color:red;\n"
"background-color:rgb(103, 255, 116);\n"
"font-weight:bold;\n"
"hover{\n"
"background-color:rgb(255, 112, 241);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
        pass_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(pass_window)
        QtCore.QMetaObject.connectSlotsByName(pass_window)

    def retranslateUi(self, pass_window):
        _translate = QtCore.QCoreApplication.translate
        pass_window.setWindowTitle(_translate("pass_window", "Login"))
        self.label_3.setText(_translate("pass_window", "          K.M.P.S LIBRARY "))
        self.label_4.setText(_translate("pass_window", "USERNAME    :"))
        self.label_5.setText(_translate("pass_window", "PASSWORD    :"))
        self.pushButton.setText(_translate("pass_window", "LOG IN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pass_window = QtWidgets.QMainWindow()
    ui = Ui_pass_window()
    ui.setupUi(pass_window)
    pass_window.show()
    sys.exit(app.exec_())
