import sys
from os import system

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

system('cls')


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela')

        # Botão
        self.buttom1 = self.make_button('Texto botao')
        self.buttom1.clicked.connect(self.segunda_action)

        self.buttom2 = QPushButton('Botão 2')
        self.buttom2.setStyleSheet('font-size: 40px;')

        self.buttom3 = QPushButton('Botão 3')
        self.buttom3.setStyleSheet('font-size: 40px;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.buttom1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.buttom2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.buttom3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.slot_example)

        self.segunda_action = self.primeiro_menu.addAction('Segunda  ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.slot_2)
        self.segunda_action.hovered.connect(self.slot_2)

    @Slot()
    def slot_example(self):
        def inner():
            self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def slot_2(self):
        print('está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px; color: red')
        btn.clicked.connect(self.slot_2)
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()  # mostre sua janela
    app.exec()  # O loop da aplicação
