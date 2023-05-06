import sys
import time
from typing import Optional

import PySide6.QtCore
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # MOver o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worke1progressed)
        worker.finished.connect(self.worker1finished)

        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('Worker iniciado')

    def worke1progressed(self, value):
        self.label1.setText(value)
        print('em progresso')

    def worker1finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)
        print('finalizado')

    def hardWork2(self):
        self.label2.setText('OK')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
