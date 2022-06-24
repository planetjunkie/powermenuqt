from PyQt6.QtWidgets import *
import os
wintitle = "PowerMenu QT"


def shutdowncmd():
  os.system("shutdown -h now")

def rebootcmd():
  os.system("reboot")

def logoutcmd():
  os.system("kill -9 -1")

buttonwidth = 150
buttonheight = 100

def main():
  application = QApplication([])
  window = QWidget()
  window.setWindowTitle(wintitle)
  window.setGeometry(200, 200, 200, 200)
  window.show()

  shutdownbtn = QPushButton("Shutdown")
  rebootbtn = QPushButton("Reboot")
  logoutbtn = QPushButton("Logout")

  shutdownbtn.setFixedSize(buttonwidth, buttonheight)
  rebootbtn.setFixedSize(buttonwidth, buttonheight)
  logoutbtn.setFixedSize(buttonwidth, buttonheight)
  

  shutdownbtn.clicked.connect(shutdowncmd)
  rebootbtn.clicked.connect(rebootcmd)
  logoutbtn.clicked.connect(logoutcmd)
  
  

  layout = QHBoxLayout()
  layout.addWidget(shutdownbtn)
  layout.addWidget(rebootbtn)
  layout.addWidget(logoutbtn)
  window.setLayout(layout)

  application.exec()

if __name__ == '__main__':
  main()