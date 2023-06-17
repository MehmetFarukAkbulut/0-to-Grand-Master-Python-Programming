import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox
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
        self.ui.btnIndexUp.clicked.connect(self.indexUp)
        self.ui.btnIndexDown.clicked.connect(self.indexDown)
        self.ui.btnUp.clicked.connect(self.upStudent)
        self.ui.btnDown.clicked.connect(self.downStudent)
        self.ui.btnSort.clicked.connect(self.sortStudents)
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
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        
        if item is not None:
            text,ok=QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)
    def removeStudent(self):
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        if item is None:
            return
        q=QMessageBox.question(self,"Remove Student","Do you want to remove student: "+item.text(),QMessageBox.Yes | QMessageBox.No) 
        if q==QMessageBox.Yes:
            item=self.ui.listItems.takeItem(index)
            del item
    
    def indexUp(self):
        #seçili studentın üstündeki studentı seç
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        if item is None:
            return
        if index == 0:
            return
        self.ui.listItems.setCurrentRow(index-1)        
        
    def indexDown(self):
        #seçili studentın altındaki studentı seç 
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        c=self.ui.listItems.count()-1
        if item is None:
            return
        if index == c:
            return
        self.ui.listItems.setCurrentRow(index+1)
        
    def upStudent(self):

        index=self.ui.listItems.currentRow()
        if index>=1:
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1,item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):

        index=self.ui.listItems.currentRow()
        if index<=self.ui.listItems.count()-1:
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1,item)
            self.ui.listItems.setCurrentItem(item)

        
        
    def sortStudents(self):
        self.ui.listItems.sortItems()
        
        
    def exitStudent(self):
        quit()
        
        
app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())