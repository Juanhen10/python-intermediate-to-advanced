# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys
from os import system

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


def slot_example(stats_bar):
    status_bar.showMessage('O meu slot foi executado')


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))


window.show()  # mostre sua janela
app.exec()  # O loop da aplicação
