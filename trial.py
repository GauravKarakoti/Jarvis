from PyQt5 import QtCore, QtGui, QtWidgets
def machine():
    import sys
    from newAI import edd
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5.QtGui import QMovie
    from PyQt5.QtCore import Qt, QThread, pyqtSignal
    import pyttsx3
    import speech_recognition as sr

    class Ui_Widget(object):
        def setupUi(self, Widget):
            Widget.setObjectName("Widget")
            Widget.resize(1200, 709)
            Widget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.label_2 = QtWidgets.QLabel(Widget)
            self.label_2.setGeometry(QtCore.QRect(690, 210, 461, 291))
            self.label_2.setText("")
            self.label_2.setPixmap(QtGui.QPixmap(r"C:\Python_Prac\JARVIS_2.0\Jarviss_giphys\speaking.gif"))
            self.label_2.setScaledContents(True)
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(Widget)
            self.label_3.setGeometry(QtCore.QRect(690, 210, 471, 291))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap(r"C:\Python_Prac\JARVIS_2.0\Jarviss_giphys/waiting.gif"))
            self.label_3.setScaledContents(True)
            self.label_3.setObjectName("label_3")
            self.label_5 = QtWidgets.QLabel(Widget)
            self.label_5.setGeometry(QtCore.QRect(0, 10, 1201, 691))
            self.label_5.setText("")
            self.label_5.setPixmap(QtGui.QPixmap(r"C:\Python_Prac\JARVIS_2.0\Jarviss_giphys/back.gif"))
            self.label_5.setScaledContents(True)
            self.label_5.setObjectName("label_5")
            self.pushButton = QtWidgets.QPushButton(Widget)
            self.pushButton.setGeometry(QtCore.QRect(1140, 660, 51, 51))
            self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton.setStyleSheet("border-image: url(C:/Python_Prac/JARVIS_2.0/Jarviss_giphys/exit_button.jpg);")
            self.pushButton.setText("")
            self.pushButton.setObjectName("pushButton")
            self.frame = QtWidgets.QFrame(Widget)
            self.frame.setGeometry(QtCore.QRect(90, 90, 501, 531))
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.lineEdit = QtWidgets.QLineEdit(self.frame)
            self.lineEdit.setGeometry(QtCore.QRect(0, 460, 501, 71))
            self.lineEdit.setObjectName("lineEdit")
            self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
            self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 501, 461))
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.pushButton_2 = QtWidgets.QPushButton(self.frame)
            self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 51, 51))
            self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_2.setStyleSheet("border-image: url(C:/Python_Prac/JARVIS_2.0/Jarviss_giphys/Enter.png);")
            self.pushButton_2.setText("")
            self.pushButton_2.setObjectName("pushButton_2")
            self.label_4 = QtWidgets.QLabel(Widget)
            self.label_4.setGeometry(QtCore.QRect(680, 200, 471, 291))
            self.label_4.setText("")
            self.label_4.setPixmap(QtGui.QPixmap(r"C:\Python_Prac\JARVIS_2.0\Jarviss_giphys/lisnening.gif"))
            self.label_4.setScaledContents(True)
            self.label_4.setObjectName("label_4")
            self.label_5.raise_()
            self.label_2.raise_()
            self.label_3.raise_()
            self.pushButton.raise_()
            self.frame.raise_()
            self.label_4.raise_()

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

    engine = pyttsx3.init()

    class SpeechRecognitionThread(QThread):
        update_text_signal = pyqtSignal(str)

        def __init__(self, parent=None):
            super(SpeechRecognitionThread, self).__init__(parent)

        def run(self):
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                while True:
                    recognizer.adjust_for_ambient_noise(source)
                    try:
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        self.update_text_signal.emit(f"You said: {command}")
                        self.process_input(command)
                    except sr.UnknownValueError:
                        self.update_text_signal.emit("Sorry, I could not understand that.")
                    except sr.RequestError:
                        self.update_text_signal.emit("Speech service is unavailable.")
                    except Exception as e:
                        self.update_text_signal.emit(f"Error: {str(e)}")

        def process_input(self, input_text):
            response = edd(input_text)
            self.update_text_signal.emit(f"Jarvis says: {response}")
            speak_response(response)

    def speak_response(response):
        engine.say(response)
        engine.runAndWait()

    class GUIs_jarvis(QWidget):
        def __init__(self):
            super(GUIs_jarvis, self).__init__()
            self.jarvisUi = Ui_Widget()
            self.jarvisUi.setupUi(self)
            self.exec_gifs()
            self.jarvisUi.pushButton_2.clicked.connect(self.on_enter_pressed)
            self.jarvisUi.pushButton.clicked.connect(self.close)
            self.jarvisUi.plainTextEdit.setStyleSheet("color: white; background-color: black;")
            self.jarvisUi.lineEdit.setStyleSheet("color: white; background-color: black;")
            self.jarvisUi.lineEdit.setEnabled(True)
            self.start_listening_thread()

        def exec_gifs(self):
            self.jarvisUi.backk = QMovie(r"M:\HackCBS\Jarviss_giphys\back.gif")
            self.jarvisUi.label_5.setMovie(self.jarvisUi.backk)
            self.jarvisUi.backk.start()
            self.jarvisUi.listening = QMovie(r"M:\HackCBS\Jarviss_giphys\lisnening.gif")
            self.jarvisUi.label_4.setMovie(self.jarvisUi.listening)
            self.jarvisUi.listening.start()
            self.jarvisUi.speak = QMovie(r"M:\HackCBS\Jarviss_giphys\speaking.gif")
            self.jarvisUi.label_2.setMovie(self.jarvisUi.speak)
            self.jarvisUi.speak.start()
            self.jarvisUi.wait = QMovie(r"M:\HackCBS\Jarviss_giphys\waiting.gif")
            self.jarvisUi.label_3.setMovie(self.jarvisUi.wait)
            self.jarvisUi.wait.start()

        def on_enter_pressed(self):
            user_input = self.jarvisUi.lineEdit.text().strip().lower()
            if user_input:
                self.process_input(user_input)

        def process_input(self, input_text):
            response = edd(input_text)
            self.jarvisUi.plainTextEdit.appendPlainText(f"Jarvis says: {response}")
            speak_response(response)

        def start_listening_thread(self):
            self.listen_thread = SpeechRecognitionThread()
            self.listen_thread.update_text_signal.connect(self.update_text)
            self.listen_thread.start()

        def update_text(self, text):
            self.jarvisUi.plainTextEdit.appendPlainText(text)

        def closeEvent(self, event):
            if self.listen_thread.isRunning():
                self.listen_thread.quit()
                self.listen_thread.wait()
            event.accept()

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = GUIs_jarvis()
        widget.show()
        sys.exit(app.exec())
machine()