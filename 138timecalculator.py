import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QDateTime,Qt
from PyQt5.QtWidgets import QApplication, QWidget
from kodzincirForm import Ui_Form

target_date = QDateTime(2023, 5, 8, 0, 0)

class CountdownWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        
        self.setupUi(self)

        self.btnGithub.clicked.connect(self.open_github)
        self.button_clicked = False

        self.update_widget()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_widget)
        self.timer.start(1000)

    def open_github(self):
        if not self.button_clicked:
            url = QtCore.QUrl("https://github.com/MehmetFarukAkbulut")
            QtGui.QDesktopServices.openUrl(url)
            self.button_clicked = True
        self.button_clicked = False

    def update_widget(self):
        current_time = QDateTime.currentDateTime()
        difference = current_time.daysTo(target_date)
        self.lcdNumber.display(-difference)

app = QApplication(sys.argv)
window = CountdownWidget()
window.setWindowFlags(Qt.WindowStaysOnTopHint)
window.show()
sys.exit(app.exec_())