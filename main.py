import sys

from PyQt5.QtCore import QPoint
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 800))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "CLICK!"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        center = QPoint(randint(1, 800), randint(1, 800))
        w = h = randint(1, 300)
        qp.drawEllipse(center, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
