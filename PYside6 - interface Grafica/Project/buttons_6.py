import math
from typing import TYPE_CHECKING

from display_3 import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils_7 import convertToNumber, isEmpty, isNumOrDot, isValidNumber
from variables_2 import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display_3 import Display
    from info_4 import Info
    from main_window_1 import MainWindow


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

# ======================================================================================
# =============================== Criação dos buttons ==================================
# ======================================================================================


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self.window = window
        self._equationInitialValue = ''
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.enterPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty(
                        'cssClass', 'specialButton')  # type: ignore
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, button_text)
                self._configSpecialButton(button)
                self._connectButtonClicked(button, slot)

# ===============================================================================
# =========================== Configuração Buttons ===============================
# ===============================================================================
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
            slot = self._makeSlot(self._clear, 'msg')
            self._connectButtonClicked(button, slot)
            # button.clicked.connect(self.display.clear)
        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, text))

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

# ===========================================================================
# ========================== Criação de Ações ================================
# ===========================================================================

    @Slot()
    def _clear(self, msg):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue

        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _configLeftOp(self, text):
     # +-/*
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # limpa o display
        self.display.setFocus()

        # Se clicou no operador sem número
        if not isValidNumber(displayText) and self._left is None:
            self._showInfo('Você não digitou nada')
            return

        # se tiver número e clicar no operador
        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op}'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)

            print(result)
        except (ZeroDivisionError):
            self._showError('Não divide zero')
        except OverflowError:
            self._showInfo('numero muito grande')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        print(self.equation)
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

# ===============================================================
# ======================== Erros ==================================
# ================================================================
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.clearFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox
        self.display.setFocus()

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
