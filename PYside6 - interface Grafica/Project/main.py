import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout,
                               QWidget)
from variables import WINDOW_ICON_PATH


def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px')
    return label1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
