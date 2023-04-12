# snake_case
# PascalCase
# camelCase

import sys

from buttons_6 import Button, ButtonsGrid
from display_3 import Display
from info_4 import Info
from main_window_1 import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles_5 import setupTheme
from variables_2 import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # INFO
    info = Info('sua conta ')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('◅')
    window.addWidgetToVLayout(display)

    # Grid - Buttons
    buttons_grid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttons_grid)

    # theme
    # theme_1(app, 'dark_blue.xml')
    setupTheme()

    # executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
