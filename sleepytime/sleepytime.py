from PyQt5.QtWidgets import *
from PyQt5.QtCore import  QSize
import os
wintitle = "Sleepytime"


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


buttonwidth = 150
buttonheight = 100

def main():
  application = QApplication([])
  window = QWidget()
  window.setWindowTitle(wintitle)
  window.setFixedSize(QSize(800, 200))
  window.show()

  shutdownbtn = QPushButton("Shutdown")
  rebootbtn = QPushButton("Reboot")
  logoutbtn = QPushButton("Logout")
  Suspendbtn = QPushButton("Suspend (systemctl)")
  hibernatebtn = QPushButton("Hibernate (systemctl)")

  shutdownbtn.setFixedSize(buttonwidth, buttonheight)
  rebootbtn.setFixedSize(buttonwidth, buttonheight)
  logoutbtn.setFixedSize(buttonwidth, buttonheight)
  Suspendbtn.setFixedSize(buttonwidth, buttonheight)
  hibernatebtn.setFixedSize(buttonwidth, buttonheight)

  shutdownbtn.clicked.connect(shutdowncmd)
  rebootbtn.clicked.connect(rebootcmd)
  logoutbtn.clicked.connect(logoutcmd)
  Suspendbtn.clicked.connect(Suspendcmd)
  hibernatebtn.clicked.connect(Suspendcmd)
  
  layout = QHBoxLayout()

  layout.addWidget(shutdownbtn)
  layout.addWidget(rebootbtn)
  layout.addWidget(logoutbtn)
  layout.addWidget(Suspendbtn)
  layout.addWidget(hibernatebtn)

  window.setLayout(layout)

  application.exec()

if __name__ == '__main__':
  main()
