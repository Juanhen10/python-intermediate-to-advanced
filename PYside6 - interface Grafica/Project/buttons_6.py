from typing import TYPE_CHECKING

from display_3 import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils_7 import isEmpty, isNumOrDot, isValidNumber
from variables_2 import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display_3 import Display
    from info_4 import Info


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


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
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
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._configSpecialButton(button)
                self._connectButtonClicked(button, slot)

############################################# Configuração Buttons #####################################################
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
            slot = self._makeSlot(self._clear, 'msg')
            self._connectButtonClicked(button, slot)
            # button.clicked.connect(self.display.clear)

        if text in '+-/*':
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button))

        if text in '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(button_text)
######################################## Criação de Ações ############################################################

    def _clear(self, msg):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue

        self.display.clear()

    def _operatorClicked(self, button):
        buttontext = button.text()  # +-/*
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # limpa o display

        # Se clicou no operador sem número
        if not isValidNumber(displayText) and self._left is None:
            print('não tem nada para colocar no valor da esquerda')
            return

        # se tiver número e clicar no operador
        if self._left is None:
            self._left = float(displayText)

        self._op = buttontext
        self.equation = f'{self._left} {self._op}'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print('Sem nada para a direita')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0
        try:
            result = eval(self.equation)
            print(result)
        except ZeroDivisionError:
            print('zero erro')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
