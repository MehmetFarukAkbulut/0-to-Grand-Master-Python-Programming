import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
from tableForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui=Ui_MainWindow()
        self.setGeometry(200,200,500,500)
        
        self.ui.setupUi(self)
        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)
        
    
    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(),item.column(),item.text())    
    
    def saveProduct(self):
        name=self.ui.txtName.text()
        price=self.ui.txtPrice.text()
        if name and price is not None:
            rowCount=self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))
        
    def loadProducts(self):
        
        products=[
            {'name': 'Samsung S5', 'price': '5000'},
            {'name': 'Samsung S6', 'price': '6000'},
            {'name': 'Samsung S7', 'price': '7000'},
            {'name': 'Samsung S8', 'price': '8000'},
            ]
        
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name','Price'))
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)
        
        rowIndex=0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(product['price']))
            rowIndex+=1

app=QtWidgets.QApplication(sys.argv)
win=Window()
win.show()
sys.exit(app.exec_())