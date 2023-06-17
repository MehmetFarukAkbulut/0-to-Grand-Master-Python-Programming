import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog,QLineEdit
from listForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui=Ui_MainWindow()
        self.setGeometry(200,200,500,500)
        
        self.ui.setupUi(self)

        self.loadStudents()
        self.ui.btnAdd.clicked.connect(self.addStudent)
        self.ui.btnEdit.clicked.connect(self.editStudent)
        self.ui.btnRemove.clicked.connect(self.removeStudent)
        self.ui.btnUp.clicked.connect(self.upStudent)
        self.ui.btnDown.clicked.connect(self.downStudent)
        self.ui.btnSort.clicked.connect(self.sortStudent)
        self.ui.btnExit.clicked.connect(self.exitStudent)

    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet','Ali','Faruk','Fatih'])
        self.ui.listItems.setCurrentRow(0)
    def addStudent(self):
        currentIndex=self.ui.listItems.currentRow()
        text,ok=QInputDialog.getText(self,'New Student', 'Student Name')
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex,text)
    def editStudent(self):
        index=currentIndex=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        
        if item is not None:
            text,ok=QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)
    def removeStudent(self):
        pass
        
    def upStudent(self):
        pass
        
    def downStudent(self):
        pass
        
    def sortStudent(self):
        pass
        
    def exitStudent(self):
        pass
        
        
app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())