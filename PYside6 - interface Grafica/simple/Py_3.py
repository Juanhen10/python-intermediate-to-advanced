# Qwidget e QLayout de Pyside6.QtWidgets
# QWidget - > gebérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys
from os import system

from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout,
                               QPushButton, QVBoxLayout, QWidget)

system('cls')


app = QApplication(sys.argv)

buttom = QPushButton('Texto do botão')
buttom.setStyleSheet('font-size: 80px; color: red')


buttom2 = QPushButton('Botão 2')
buttom2.setStyleSheet('font-size: 40px;')

buttom3 = QPushButton('Botão 3')
buttom3.setStyleSheet('font-size: 40px;')

cenral_widget = QWidget()

# layout = QVBoxLayout()#
# layout = QHBoxLayout()
layout = QGridLayout()
cenral_widget.setLayout(layout)

layout.addWidget(buttom, 1, 1, 1, 1)
layout.addWidget(buttom2, 1, 2, 1, 1)
layout.addWidget(buttom3, 3, 1, 1, 2)

cenral_widget.show()  # Entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
