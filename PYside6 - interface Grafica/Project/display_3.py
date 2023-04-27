

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils_7 import isEmpty, isNumOrDot
from variables_2 import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    enterPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)

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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter or text == '=':
            self.enterPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            print('delete')
            return event.ignore()

        if isEsc or text == 'c':
            self.clearPressed.emit()
            print('esc')
            return event.ignore()

        # return super().keyPressEvent(event)
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            print('aaa')
            self.inputPressed.emit(text)
            return event.ignore()
