from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setFixedSize(728, 199)
        Window.setWindowIcon(QtGui.QIcon("sleepytime/sleepytime.ico"))

        def shutdowncmd():
            os.system("shutdown -h now")

        def rebootcmd():
            os.system("reboot")

        def logoutcmd():
            os.system("kill -9 -1")

        def Suspendcmd():
            os.system("systemctl suspend")

        def hibernatecmd():
            os.system("systemctl hibernate")

        self.Shutdownbtn = QtWidgets.QPushButton(Window)
        self.Shutdownbtn.setGeometry(QtCore.QRect(10, 20, 161, 91))
        self.Shutdownbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Shutdownbtn.setObjectName("Shutdownbtn")
        self.Shutdownbtn.clicked.connect(shutdowncmd)

        

        

        self.Logoutbtn = QtWidgets.QPushButton(Window)
        self.Logoutbtn.setGeometry(QtCore.QRect(10, 140, 701, 41))
        self.Logoutbtn.setObjectName("Logoutbtn")
        self.Logoutbtn.clicked.connect(logoutcmd)
        
       
        self.Rebootbn = QtWidgets.QPushButton(Window)
        self.Rebootbn.setGeometry(QtCore.QRect(190, 20, 161, 91))
        self.Rebootbn.setObjectName("Rebootbn")
        self.Rebootbn.clicked.connect(rebootcmd)
       
        self.Hibernatebtn = QtWidgets.QPushButton(Window)
        self.Hibernatebtn.setGeometry(QtCore.QRect(550, 20, 161, 91))
        self.Hibernatebtn.setObjectName("Hibernatebtn")
        self.Hibernatebtn.clicked.connect(hibernatecmd)

       
        self.Suspendbtn = QtWidgets.QPushButton(Window)
        self.Suspendbtn.setGeometry(QtCore.QRect(370, 20, 161, 91))
        self.Suspendbtn.setObjectName("Suspendbtn")
        self.Suspendbtn.clicked.connect(Suspendcmd)
        

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Sleepytime"))
        self.Shutdownbtn.setText(_translate("Window", "Shut down"))
        self.Logoutbtn.setText(_translate("Window", "Log Out"))
        self.Rebootbn.setText(_translate("Window", "Reboot"))
        self.Hibernatebtn.setText(_translate("Window", "Hibernate"))
        self.Suspendbtn.setText(_translate("Window", "Suspend"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

