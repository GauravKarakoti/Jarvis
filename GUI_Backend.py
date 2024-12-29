from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 709)
        Widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Background GIF
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 1201, 691))
        self.label_5.setPixmap(QtGui.QPixmap("Jarviss_giphys/back.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        # Speaking GIF
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(690, 210, 471, 291))
        self.label_2.setPixmap(QtGui.QPixmap("Jarviss_giphys/speaking.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)  # Hide initially

        # Waiting GIF
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(690, 210, 471, 291))
        self.label_3.setPixmap(QtGui.QPixmap("Jarviss_giphys/waiting.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setVisible(False)  # Hide initially

        # Listening GIF
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(690, 210, 471, 291))
        self.label_4.setPixmap(QtGui.QPixmap("Jarviss_giphys/lisnening.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setVisible(False)  # Hide initially

        # Exit Button
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(1140, 660, 51, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(Jarviss_giphys/exit_button.jpg);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        # Text Input and Display Frame
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(90, 90, 501, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Text Input Box
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 460, 501, 71))
        self.lineEdit.setObjectName("lineEdit")
        
        # Terminal Output Display
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 501, 461))
        self.plainTextEdit.setObjectName("plainTextEdit")

        # Enter Button
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 51, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(Jarviss_giphys/Enter.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        # Layering setup to control widget visibility
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.label_4.raise_()

        # Final setup and translation for window title
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.lineEdit.setText(_translate("Widget", "Enter Command"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())