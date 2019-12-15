
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QTextEdit, QLabel, QGridLayout
from qtconsole.qt import QtGui, QtCore

import main

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)


class UIWindow(object):
    def setupUI(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Search Engine For News")
        MainWindow.setMinimumWidth(resolution.width() / 1)
        MainWindow.setMinimumHeight(resolution.height() / 1)
        MainWindow.setStyleSheet(
            "QWidget {background-color: #fdfdfe;} QScrollBar:horizontal {width: 1px; height: 1px;"
            "background-color: #460F54;} QScrollBar:vertical {width: 1px; height: 1px;"
            "background-color: #460F54;}")

        self.textf = QTextEdit(self.centralwidget)
        self.textf.setFixedHeight(100)
        self.textf.setFixedWidth(1890)

        self.textf.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: #460F54; color: #fdfdfe;"
            "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: #460F54;")
        self.text = self.textf.toPlainText()

        self.ToolsBTN = QPushButton('search', self.centralwidget)
        self.ToolsBTN.move(50, 350)
        self.ToolsBTN.setFont(font_but)
        self.ToolsBTN.clicked.connect(self.on_but1)

        lb1 = QLabel(self.centralwidget)
        img = QtGui.QPixmap('logo.png')
        lb1.setPixmap(img.scaled(420, 200))

        grid1 = QGridLayout(self.centralwidget)
        grid1.addWidget(self.textf, 1, 0, 3, 3)
        grid1.addWidget(self.ToolsBTN, 2, 1, 4, 1)
        grid1.addWidget(lb1, 0, 1, 1, 1)
        grid1.setContentsMargins(10, 10, 10, 10)
        MainWindow.setLayout(grid1)

    def on_but1(self):
        txt = self.textf.toPlainText()
        main.get_input(txt)

        return txt


class UIToolTab(object):
    def setupUI(self, MainWindow):
        MainWindow.setWindowTitle("result")
        self.centralwidget = QWidget(MainWindow)
        self.CPSBTN = QPushButton("back", self.centralwidget)
        self.CPSBTN.move(900, 700)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiToolTab = UIToolTab()
        self.startUIWindow()

    def startUIToolTab(self):
        self.uiToolTab.setupUI(self)
        self.uiToolTab.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.ToolsBTN.clicked.connect(self.on_but1)
        self.show()

    def on_but1(self):
        self.startUIToolTab()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    resolution = desktop.availableGeometry()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
