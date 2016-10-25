from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
import sys

sheet = '''
QLineEdit {
    border: 2px solid gray;
    border-radius: 10px;
    height:25px;
    font-size:15px;
    color:#0a0505;
    padding: 0 8px;
    background: yellow;
    selection-background-color: darkgray;
}

QPushButton {

	box-shadow: 0px 10px 14px -7px #276873;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #599bb3, stop: 1 #408c99);
	background-color:#599bb3;
	border-radius:8px;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	padding:5px 20px;
	font-weight:bold;
	text-decoration:none;
	text-shadow:0px 1px 0px #3d768a;
}

QPushButton:hover {
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #408c99, stop: 1 #599bb3);
	background-color:#408c99;
}

QPushButton:pressed {
	top:1px;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3d808c, stop: 1 #327c89);
}
'''


class qWindow(QWidget):
    def __init__(self, parent=None):
        super(qWindow, self).__init__(parent)
        self.wrap_layout = QVBoxLayout()
        self.wrap_layout.setSpacing(0)
        self.wrap_layout.setMargin(0)
        self.topUI()
        self.mainUI()
        self.wrap_layout.addWidget(self.top_window)
        self.wrap_layout.addWidget(self.main_window)
        self.setLayout(self.wrap_layout)
        self.top_search.setAutoFillBackground(False)
        self.setStyleSheet(sheet)
        # self.wrap_layout.addLayout(self.main_layout)

    def topUI(self):
        self.top_window = QWidget()
        self.top_window.setObjectName("topwindow")
        self.top_window.setMinimumHeight(100)
        self.top_window.setMaximumHeight(200)
        self.top_window.setStyleSheet(
            "QWidget#topwindow{background-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dce6dd, stop: 1 #c8cec8);;}")
        top_layout = QHBoxLayout()
        self.top_search = QLineEdit()
        self.top_search.setMaximumWidth(300)
        self.top_search_button = QPushButton("search")
        top_layout.addStretch()
        top_layout.addWidget(self.top_search)
        top_layout.addWidget(self.top_search_button)
        top_layout.addStretch()
        self.top_window.setLayout(top_layout)

    def mainUI(self):
        self.main_window = QWidget()
        self.main_window.setMinimumHeight(300)
        self.main_window.setMinimumWidth(1000)
        # self.main_window.setStyleSheet("*{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8bf192, stop: 1 #41c34a);}")


app = QApplication(sys.argv)
wind = qWindow()
wind.show()
sys.exit(app.exec_())