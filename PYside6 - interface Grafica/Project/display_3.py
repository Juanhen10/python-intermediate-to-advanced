

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables_2 import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margin = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(TEXT_MARGIN * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margin)
