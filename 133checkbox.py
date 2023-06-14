import sys
from PyQt5 import QtWidgets
from checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
            
        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbKitap.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)
        
        
    def show_state(self,value):
        cb=self.sender()
        print(value)
        print(cb.text())
        print(cb.isChecked())

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())
    
app()