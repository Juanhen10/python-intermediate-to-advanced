
import sys
from typing import Optional

import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.changeLabelResult)

    def changeLabelResult(self):
        text = self.lineEdit.text()
        self.labelResult.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
