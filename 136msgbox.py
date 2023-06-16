import sys
from PyQt5 import QtWidgets
from msgboxForm import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui=Ui_MainWindow()
        self.setGeometry(200,200,500,500)
        
        self.ui.setupUi(self)
        
        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):
        msg=QMessageBox()
        msg.setWindowTitle('Close Application')
        msg.setGeometry(450,450,500,500)
        
        msg.setText('Are you sure?')
        # msg.setIcon(QMessageBox.Question)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.setDetailedText('details...')
        msg.buttonClicked.connect(self.popup_button)
        
        x=msg.exec_()
        print(x)
        
        
    def popup_button(self,i):
        print(i.text())
        
        if i.text()=='OK':
            print('OKEY...')
            QtWidgets.qApp.quit()
        elif i.text()=='Cancel':
            print('Cancel...')
        elif i.text()=='Ignore':
            print('Ignore...')
    
app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())