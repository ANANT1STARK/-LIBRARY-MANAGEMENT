# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_submit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


import mysql.connector as a

con = a.connect(host="localhost",user="root",passwd="",database="library1")
class book_submit(object):
    def bookup(self,book_code,no_of_books):
        command = 'select total_book from books where BCODE=%s'
        data = (book_code,)
        c = con.cursor()
        c.execute(command,data)
        myresult = c.fetchone()
        t = myresult[0] + no_of_books
        sql = 'update books set total_book = %s where BCODE = %s'
        data =(t,book_code)
        c.execute(sql,data)
        con.commit()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.submit.hide()
        self.label_2.setText('SUCCESS !!')
    def submit_book(self):
        name_of_student = self.lineEdit.text()
        book_name = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        d = self.lineEdit_4.text()
        command = "insert into submit values(%s,%s,%s,%s)"
        data = (name_of_student,book_name,book_code,d)
        c = con.cursor()
        c.execute(command,data)
        con.commit()
    
        self.bookup(book_code,1)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/library-logo-design-template-45579f2f9eaf725821b915b523f191eb_screen.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 821, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/library2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 231, 51))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-weight:bold;\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 100, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 231, 51))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-weight:bold;\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 170, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 240, 231, 51))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-weight:bold;\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 250, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 310, 231, 51))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-weight:bold;\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 320, 121, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 30, 461, 51))
        self.label_6.setStyleSheet("color: rgb(91, 255, 62);\n"
"font-weight:bold;\n"
"font: 87 22pt \"Segoe UI Black\";\n"
"border-style:solid;\n"
"border-width:5px;\n"
"border-color:rgb(197, 49, 255);\n"
"background-color: rgb(255, 35, 39);")
        self.label_6.setObjectName("label_6")
        self.submit = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.submit_book())
        self.submit.setGeometry(QtCore.QRect(340, 420, 91, 51))
        self.submit.setStyleSheet("background-color: rgb(212, 255, 0);\n"
"color:rgb(0, 0, 0);\n"
"font-weight:bold;\n"
"font-size:15px;")
        self.submit.setObjectName("submit")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LIBREARY MANAGEMENT"))
        self.label_2.setText(_translate("MainWindow", "STUDENT NAME    :"))
        self.label_3.setText(_translate("MainWindow", "BOOK NAME          :"))
        self.label_4.setText(_translate("MainWindow", "BOOK CODE          :"))   
        self.label_5.setText(_translate("MainWindow", "DATE(year/month/day)      :"))
        self.label_6.setText(_translate("MainWindow", "                BOOK SUBMIT"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = book_submit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
