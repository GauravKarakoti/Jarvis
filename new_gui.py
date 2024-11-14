from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import time
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from newAI import edd
from Listen import MicExecution
from Speak2 import Speak
from clap import Tester
import speedtest
from awaj import jarvis_intro
import requests
from bs4 import BeautifulSoup
import pyautogui
import pywhatkit
import wikipedia as googlescrap
import datetime
from imggenrator import tt
from dictapp import openappweb, closeappweb
from location import system_locater, asked_location
from Comparision_Graph import graph_creator

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 709)
        Widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(690, 210, 461, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"Jarviss_giphys\speaking.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(690, 210, 471, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"Jarviss_giphys/waiting.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 1201, 691))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"Jarviss_giphys/back.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(1140, 660, 51, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(Jarviss_giphys/exit_button.jpg);")
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
        self.pushButton_2.setStyleSheet("border-image: url(Jarviss_giphys/Enter.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(680, 200, 471, 291))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(r"Jarviss_giphys/lisnening.gif"))
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

# Initialize the TTS engine
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
                    self.update_text_signal.emit(f"You said: {command}")  # Displaying command in text area
                    self.process_input(command, from_gui=False)  # Indicate that it's from the speech thread
                except sr.UnknownValueError:
                    self.update_text_signal.emit("Sorry, I could not understand that.")
                except sr.RequestError:
                    self.update_text_signal.emit("Speech service is unavailable. Retrying...")
                    time.sleep(3)  # Retry after a short delay
                except Exception as e:
                    self.update_text_signal.emit(f"Error: {str(e)}")

    def process_input(self, Data, from_gui=False):
        if len(Data) < 3:
            return
        
        Data = Data.lower()

        # Prevent duplicate calls to Speak by checking if it's GUI input or not
        if not from_gui:  # Only speak if it's from the SpeechRecognitionThread
            if "lkm" in Data:
                tt()
            elif 'the time' in Data:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                self.update_text_signal.emit(f"Sir, the time is {strtime}")  # Output to GUI
                Speak(f"Sir, the time is {strtime}")
            elif "vision" in Data:
                from test import computer_vision
                computer_vision()
            elif 'gmail' in Data:
                from gmail import gmail
                gmail()
            elif "youtube" in Data:
                from yt import searchYoutube
                searchYoutube(Data)
            elif 'google search' in Data:
                self.google_search(Data)
            elif "temperature" in Data:
                self.get_weather("temperature")
            elif "weather" in Data:
                self.get_weather("weather")
            elif "screenshot" in Data or 'ss' in Data:
                self.take_screenshot()
            elif "list" in Data:
                self.list_sustainable_goals()
            elif "shutdown the system" in Data:
                self.shutdown_system()
            elif 'go to sleep' in Data or 'you can go' in Data:
                Speak("Terminating")
                self.update_text_signal.emit("Terminating...")
                self.quit()
            else:
                self.get_reply(Data)
        else:  # If it's from GUI input, just handle it without speaking
            if "lkm" in Data:
                tt()
            elif 'the time' in Data:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                self.update_text_signal.emit(f"Sir, the time is {strtime}")  # Output to GUI
            elif "vision" in Data:
                from test import computer_vision
                computer_vision()
            elif 'gmail' in Data:
                from gmail import gmail
                gmail()
            elif "youtube" in Data:
                from yt import searchYoutube
                searchYoutube(Data)
            elif 'google search' in Data:
                self.google_search(Data)
            elif "temperature" in Data:
                self.get_weather("temperature")
            elif "weather" in Data:
                self.get_weather("weather")
            elif "screenshot" in Data or 'ss' in Data:
                self.take_screenshot()
            elif "list" in Data:
                self.list_sustainable_goals()
            elif "shutdown the system" in Data:
                self.shutdown_system()
            elif 'go to sleep' in Data or 'you can go' in Data:
                self.update_text_signal.emit("Terminating...")
                self.quit()
            else:
                self.get_reply(Data)

    def google_search(self, query):
        query = query.replace("google search", "").replace("google", "")
        self.update_text_signal.emit(f"Searching for: {query}")  # Output to GUI
        Speak("This is what I found on the web!")
        pywhatkit.search(query)
        try:
            results = googlescrap.summary(query, 1)
            self.update_text_signal.emit(results)  # Output to GUI
            Speak(results)
        except:
            self.update_text_signal.emit("No speakable data available.")  # Output to GUI
            Speak("No speakable data available.")

    def get_weather(self, query):
        search = f"{query} in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        self.update_text_signal.emit(f"Current {search} is {temp}")  # Output to GUI
        Speak(f"current {search} is {temp}")

    def take_screenshot(self):
        im = pyautogui.screenshot()
        im.save("ss.jpg")
        self.update_text_signal.emit("Screenshot Saved.")  # Output to GUI
        Speak("Screenshot Saved.")

    def list_sustainable_goals(self):
        goals = '''
        The 17 Sustainable Goals are as follows:
        1. No Poverty
        2. Zero Hunger
        3. Good Health and Wellbeing
        4. Quality Education
        5. Gender Equality
        6. Clean Water and Sanitation
        7. Affordable and Clean Energy
        8. Decent Work and Economic Growth
        9. Industry, Innovation and Infrastructure
        10. Reduced Inequalities
        11. Sustainable Cities and Communities
        12. Responsible Consumption and Production
        13. Climate Action
        14. Life Below Water
        15. Life on Land
        16. Peace, Justice and Strong Institutions
        17. Partnership Goals
        '''
        self.update_text_signal.emit(goals)  # Output to GUI
        Speak(goals)

    def shutdown_system(self):
        import os
        os.system("shutdown /s /t 1")

    def get_reply(self, Data):
        reply = edd(Data)
        self.update_text_signal.emit(reply)  # Output to GUI
        Speak(reply)

class GUIs_jarvis(QWidget):
    def __init__(self):
        super(GUIs_jarvis, self).__init__()
        self.jarvisUi = Ui_Widget()
        self.jarvisUi.setupUi(self)
        self.exec_gifs()
        
        # Connecting lineEdit returnPressed signal (Enter key press)
        self.jarvisUi.lineEdit.returnPressed.connect(self.on_enter_pressed)
        
        self.jarvisUi.pushButton.clicked.connect(self.close)
        self.jarvisUi.plainTextEdit.setStyleSheet("color: white; background-color: black;")
        self.jarvisUi.lineEdit.setStyleSheet("color: white; background-color: black;")
        self.jarvisUi.lineEdit.setEnabled(True)
        
        self.start_listening_thread()

    def exec_gifs(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        gif_dir = os.path.join(script_dir, 'Jarviss_giphys')
        
        self.jarvisUi.backk = QMovie(os.path.join(gif_dir, 'back.gif'))
        self.jarvisUi.label_5.setMovie(self.jarvisUi.backk)
        self.jarvisUi.backk.start()
        
        self.jarvisUi.listening = QMovie(os.path.join(gif_dir, 'lisnening.gif'))
        self.jarvisUi.label_4.setMovie(self.jarvisUi.listening)
        self.jarvisUi.listening.start()
        
        self.jarvisUi.speak = QMovie(os.path.join(gif_dir, 'speaking.gif'))
        self.jarvisUi.label_2.setMovie(self.jarvisUi.speak)
        self.jarvisUi.speak.start()
        
        self.jarvisUi.wait = QMovie(os.path.join(gif_dir, 'waiting.gif'))
        self.jarvisUi.label_3.setMovie(self.jarvisUi.wait)
        self.jarvisUi.wait.start()

    def on_enter_pressed(self):
        user_input = self.jarvisUi.lineEdit.text().strip().lower()
        if user_input:
            self.process_input(user_input, from_gui=True)

    def process_input(self, Data, from_gui=False):
        if len(Data) < 3:
            return
        Data = Data.lower()
        self.speech_thread.process_input(Data, from_gui=True)

    def start_listening_thread(self):
        self.speech_thread = SpeechRecognitionThread(self)
        self.speech_thread.update_text_signal.connect(self.update_gui_text)
        self.speech_thread.start()

    def update_gui_text(self, text):
        self.jarvisUi.plainTextEdit.appendPlainText(text)

    def closeEvent(self, event):
        if self.speech_thread.isRunning():
            self.speech_thread.quit()
            self.speech_thread.wait()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUIs_jarvis()
    window.show()
    sys.exit(app.exec_())
