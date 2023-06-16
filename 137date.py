import sys
from PyQt5 import QtWidgets
from dateForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui=Ui_MainWindow()
        self.setGeometry(200,200,500,500)
        
        self.ui.setupUi(self)


app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())