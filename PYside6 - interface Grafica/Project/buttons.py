from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        # Type/ style font
        font.setBold(True)
        self.setFont(font)
        # size
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setLegacyWeight(True)
        self.setMinimumSize(75, 75)
        # prorpiedade


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)
