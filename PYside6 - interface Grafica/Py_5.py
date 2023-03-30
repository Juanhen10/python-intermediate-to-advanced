import sys
from os import system

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

system('cls')


app = QApplication(sys.argv)

window = QMainWindow()
cenral_widget = QWidget()
window.setCentralWidget(cenral_widget)
window.setWindowTitle('Minha janela')

buttom = QPushButton('Texto do botão')
buttom.setStyleSheet('font-size: 80px; color: red')


buttom2 = QPushButton('Botão 2')
buttom2.setStyleSheet('font-size: 40px;')

buttom3 = QPushButton('Botão 3')
buttom3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
cenral_widget.setLayout(layout)

layout.addWidget(buttom, 1, 1, 1, 1)
layout.addWidget(buttom2, 1, 2, 1, 1)
layout.addWidget(buttom3, 3, 1, 1, 2)


@Slot()
def slot_example(stats_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def slot_2(checked):
    print('está marcado?', checked)


@Slot()
def slot_3(action):
    def inner():
        slot_2(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_action = primeiro_menu.addAction('Segunda  ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(slot_2)
segunda_action.hovered.connect(slot_3(segunda_action))

buttom.clicked.connect(slot_3(segunda_action))

window.show()  # mostre sua janela
app.exec()  # O loop da aplicação
