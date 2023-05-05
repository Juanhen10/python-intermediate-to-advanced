import sys
from typing import Optional

import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
