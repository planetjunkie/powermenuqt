from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 200)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWindowIcon(QtGui.QIcon('sleepytime/sleepytime.png'))

        def shutdowncmd():
            os.system("shutdown -h now")

        def rebootcmd():
            os.system("reboot")

        def logoutcmd():
            os.system("kill -9 -1")

        def suspendcmd():
            os.system("systemctl suspend")

        def hibernatecmd():
            os.system("systemctl hibernate")


        self.centeral = QtWidgets.QWidget(MainWindow)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centeral)
        self.layoutwin = QtWidgets.QVBoxLayout()
        self.tabs = QtWidgets.QTabWidget(self.centeral)
        self.os = QtWidgets.QWidget()    
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.os)
        self.osbtnlayout = QtWidgets.QHBoxLayout()


        self.suspendbtn = QtWidgets.QPushButton(self.os)
        self.suspendbtn.setMinimumSize(QtCore.QSize(50, 90))
        self.suspendbtn.clicked.connect(suspendcmd)
        self.osbtnlayout.addWidget(self.suspendbtn)

        self.hibernatebtn = QtWidgets.QPushButton(self.os)
        self.hibernatebtn.setMinimumSize(QtCore.QSize(50, 90))
        self.hibernatebtn.clicked.connect(hibernatecmd)
        self.osbtnlayout.addWidget(self.hibernatebtn)

        self.logoutbtn = QtWidgets.QPushButton(self.os)
        self.logoutbtn.setMinimumSize(QtCore.QSize(50, 90))
        self.logoutbtn.clicked.connect(logoutcmd)
        self.osbtnlayout.addWidget(self.logoutbtn)
        
        self.horizontalLayout_2.addLayout(self.osbtnlayout)
        self.tabs.addTab(self.os, "")
        self.device = QtWidgets.QWidget()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.device)
        self.devicebtnlayout = QtWidgets.QHBoxLayout()

        self.shutdownbtn = QtWidgets.QPushButton(self.device)
        self.shutdownbtn.setMinimumSize(QtCore.QSize(0, 90))
        self.shutdownbtn.clicked.connect(shutdowncmd)
        self.devicebtnlayout.addWidget(self.shutdownbtn)

        self.rebootbtn = QtWidgets.QPushButton(self.device)
        self.rebootbtn.setMinimumSize(QtCore.QSize(0, 90))
        self.rebootbtn.clicked.connect(rebootcmd)
        self.devicebtnlayout.addWidget(self.rebootbtn)
        self.horizontalLayout_3.addLayout(self.devicebtnlayout)
        
        self.tabs.addTab(self.device, "")
        self.layoutwin.addWidget(self.tabs)
        self.verticalLayout_2.addLayout(self.layoutwin)
        MainWindow.setCentralWidget(self.centeral)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sleepytime"))
        self.suspendbtn.setText(_translate("MainWindow", "Suspend"))
        self.hibernatebtn.setText(_translate("MainWindow", "Hibernate"))
        self.logoutbtn.setText(_translate("MainWindow", "Log Out"))
        self.tabs.setTabText(self.tabs.indexOf(self.os), _translate("MainWindow", "OS"))
        self.shutdownbtn.setText(_translate("MainWindow", "Shutdown"))
        self.rebootbtn.setText(_translate("MainWindow", "Reboot"))
        self.tabs.setTabText(self.tabs.indexOf(self.device), _translate("MainWindow", "Device"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
