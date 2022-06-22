from PyQt6.QtWidgets import *
import os
wintitle = "PowerMenu QT"


def shutdowncmd():
  os.system("shutdown -h now")
def rebootcmd():
  os.system("reboot")


def main():
  application = QApplication([])
  window = QWidget()
  window.setWindowTitle(wintitle)
  window.show()

  shutdownbtn = QPushButton("Shutdown")
  rebootbtn = QPushButton("Reboot")
  
  shutdownbtn.clicked.connect(shutdowncmd)
  rebootbtn.clicked.connect(rebootcmd)

  

  layout = QHBoxLayout()
  layout.addWidget(shutdownbtn)
  layout.addWidget(rebootbtn)
  window.setLayout(layout)

  application.exec()

if __name__ == '__main__':
  main()