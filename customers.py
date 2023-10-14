"""
Main widnow of Customers app
Made by K>K> 
2022    
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QPixmap, QScreen
import os
from db_con import dbConnection
import hashlib


class Ui_Login(object):
    def __init__(self, Login, parent=None):
        super(Ui_Login, self).__init__(parent)
        Login.setObjectName("Login")
        Login.resize(500, 200)
        Login.setMinimumSize(QtCore.QSize(500, 200))
        Login.setBaseSize(QtCore.QSize(500, 200))
        self.imagelabel = QtWidgets.QLabel(Login)
        self.imagelabel.setGeometry(QtCore.QRect(50, 30, 161, 121))
        self.imagelabel.setObjectName("imagelabel")
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(250, 20, 241, 158))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        # my 
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.imagelabel.setText(_translate("Login", ""))
        pixmap = QPixmap('ui/login_graphic.png')    
        self.imagelabel.setPixmap(pixmap)                   # loading image as pixmap to label
        self.label.setText(_translate("Login", "Username / E-mail"))
        self.label_2.setText(_translate("Login", "Password"))
        self.label_3.setText(_translate("Login", "Forgot Password?"))
        self.pushButton.setText(_translate("Login", "Login"))

#my funcs
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def warningbox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def login(self):
        email = self.lineEdit.text()    
        password = hashlib.md5(self.lineEdit_2.text().encode('utf-8')).hexdigest()
        db = dbConnection()
        db.connect()
        query = f"SELECT count(*) FROM users WHERE email=\'{email}\' AND pass = \'{password}\'"
        row = db.fetchone(query)
        db.close()
        if row[0] == 1:
            self.loggedas = f"You are logged as: {email}"

            self.warningbox("Login problem", "Your email or password is not correct. Enter correct details. ")
        

class Ui_Customers(object):
    def __init__(self, Customers, parent = None):
        super(Ui_Customers, self).__init__(parent)
        self.loggedas = ''
        Customers.setObjectName("Customers")
        Customers.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Customers)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 230, 191, 51))
        self.label.setObjectName("label")
       
        Customers.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Customers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Customers.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Customers)
        self.statusbar.setObjectName("statusbar")
        Customers.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Customers)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Customers)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
            
        self.retranslateUi(Customers)
        QtCore.QMetaObject.connectSlotsByName(Customers)

    def retranslateUi(self, Customers):
        _translate = QtCore.QCoreApplication.translate
        Customers.setWindowTitle(_translate("Customers", "Customers"))
        self.menuFile.setTitle(_translate("Customers", "App"))
        self.actionOpen.setText(_translate("Customers", "Login"))
        self.actionClose.setText(_translate("Customers", "Close"))
        self.label.setText(_translate("Login", ""))
        
        #my actions
        self.actionOpen.triggered.connect(self.actionOpenLogin)

#my functions
    def actionOpenLogin(self):
        self.window_login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window_login)
        self.window_login.show()  
        
    def openLogin(self):
        self.sub = Ui_Login()
        self.sub.show()
        
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customers = Ui_Customers("")
    Customers.show()
    sys.exit(app.exec_())
