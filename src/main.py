from PyQt6.QtWidgets import *
import os
wintitle = "PowerMenu QT"

def main():
  application = QApplication([])
  window = QWidget()
  window.setWindowTitle(wintitle)
  window.show()

  shutdownbtn = QPushButton("Shutdown")
  rebootbtn = QPushButton("Reboot")
  
  shutdownbtn.clicked.connect(shutdown)
  rebootbtn.clicked.connect(reboot)

  def shutdown():
    os.system("shutdown -h now")
  def reboot():
    os.system("reboot")

  

  layout = QHBoxLayout()
  layout.addWidget(shutdownbtn)
  layout.addWidget(rebootbtn)
  window.setLayout(layout)

  application.exec()

if __name__ == '__main__':
  main()