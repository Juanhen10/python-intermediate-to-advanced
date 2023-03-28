# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O widget principal da aplicação
# QPushButton -> Um botão
# Pyside6>QtWidgets -> Onde estão os widgets do PySide6


import sys
from os import system

from PySide6.QtWidgets import QApplication, QPushButton

system('cls')


app = QApplication(sys.argv)

buttom = QPushButton('Texto do botão')
buttom.setStyleSheet('font-size: 40px; color: red')
buttom.show()  # Adiciona o widget na hieraquia e exibe a janela

buttom2 = QPushButton('Botão 2')
buttom2.setStyleSheet('font-size: 40px;')


app.exec()  # O loop da aplicação
