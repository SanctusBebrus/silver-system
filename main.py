import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.doPaint = False
        self.initUI()

    def initUI(self):

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.doPaint:
            qp = QPainter()
            qp.begin(self)
            self.makeItCircles(qp)
            qp.end()

    def paint(self):
        self.doPaint = True
        self.repaint()

    def makeItCircles(self, qp):
        qp.setBrush(QColor('Yellow'))
        center = QPoint(randint(1, 800), randint(1, 800))
        w = h = randint(1, 300)
        qp.drawEllipse(center, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
