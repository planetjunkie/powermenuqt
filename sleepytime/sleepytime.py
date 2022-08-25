from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os

os.system("clear && exit")

class Ui_MainWindow(object):
    def ui(self, QMainWindow):
        QMainWindow.resize(800, 200)
        QMainWindow.setMinimumSize(QtCore.QSize(300, 200))
        QMainWindow.setWindowOpacity(1.0)
        QMainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

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

        def do_action(act):
            if act == 0:
                cw = confirm_win(shutdowncmd, "power off")
                cw.exec()
            elif act == 1:
                cw = confirm_win(rebootcmd, "reboot")
                cw.exec()
            elif act == 2:
                cw = confirm_win(logoutcmd, "logout")
                cw.exec()
            elif act == 3:
                cw = confirm_win(suspendcmd, "suspend the computer")
                cw.exec()
            elif act == 4:
                cw = confirm_win(hibernatecmd, "hibernate the computer")
                cw.exec()


        menubar = QMainWindow.menuBar()

        sleepymenu = menubar.addMenu("&Sleepytime")
        sleepymenu.addAction("&Exit", quit)

        aboutmenu = menubar.addMenu('&About')
        aboutmenu.addAction('&About Sleepytime', abtwin.aboutwindow)
        
       
        

        self.centeral = QtWidgets.QWidget(QMainWindow)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centeral)
        self.layoutwin = QtWidgets.QVBoxLayout()
        self.tabs = QtWidgets.QTabWidget(self.centeral)
        self.os = QtWidgets.QWidget()    
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.os)
        self.osbtnlayout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(self.os)
        self.label.setText("Leaving? Goodbye & Stay Safe <3")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.suspendbtn = QtWidgets.QPushButton(self.os)
        self.suspendbtn.setMinimumSize(QtCore.QSize(50, 90))
        self.suspendbtn.clicked.connect(lambda: do_action(3))
        self.osbtnlayout.addWidget(self.suspendbtn)

        self.hibernatebtn = QtWidgets.QPushButton(self.os)
        self.hibernatebtn.setMinimumSize(QtCore.QSize(50, 90))
        self.hibernatebtn.clicked.connect(lambda: do_action(4))
        self.osbtnlayout.addWidget(self.hibernatebtn)

        self.logoutbtn = QtWidgets.QPushButton(self.os)
        self.logoutbtn.setMinimumSize(QtCore.QSize(50, 90))
        self.logoutbtn.clicked.connect(lambda: do_action(2))
        self.osbtnlayout.addWidget(self.logoutbtn)
        
        self.horizontalLayout_2.addLayout(self.osbtnlayout)
        self.tabs.addTab(self.os, "")
        self.device = QtWidgets.QWidget()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.device)
        self.devicebtnlayout = QtWidgets.QHBoxLayout()

        self.shutdownbtn = QtWidgets.QPushButton(self.device)
        self.shutdownbtn.setMinimumSize(QtCore.QSize(0, 90))
        self.shutdownbtn.clicked.connect(lambda: do_action(0))
        self.devicebtnlayout.addWidget(self.shutdownbtn)

        self.rebootbtn = QtWidgets.QPushButton(self.device)
        self.rebootbtn.setMinimumSize(QtCore.QSize(0, 90))
        self.rebootbtn.clicked.connect(lambda: do_action(1))
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

class abtwin(QDialog):
    def aboutwindow():
        msg = QMessageBox()
        msg.setWindowTitle("About sleepytime")
        msg.setText("Sleepytime is an open source powermenu, This Application was developed with love by Ali Alshamsi (@planetjunkie) --- (Current Version: v2.2 (Release Candidate))")
        msg.exec_()

class confirm_win(QDialog):
    def __init__(self, function, action):
        super().__init__()

        self.function = function
        self.action = action

        self.setWindowTitle("Confirm")

        button = QDialogButtonBox.Yes | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(button)
        self.button_box.accepted.connect(self.run_func)
        self.button_box.rejected.connect(self.nothing)

        self.boxlay = QVBoxLayout()
        lbl_message = QLabel(f"Are you sure you would like to {self.action}?")
        self.boxlay.addWidget(lbl_message)
        self.boxlay.addWidget(self.button_box)
        self.setLayout(self.boxlay)

    def nothing(self):
        self.close()

    def run_func(self):
        self.close()
        self.function()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
