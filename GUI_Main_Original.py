import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from GUI_Backend import Ui_Widget
import pyttsx3
import speech_recognition as sr
from newAI import edd
import threading

# Initialize the speech engine
engine = pyttsx3.init()

class GUIs_jarvis(QWidget):
    def __init__(self):
        super(GUIs_jarvis, self).__init__()
        self.jarvisUi = Ui_Widget()
        self.jarvisUi.setupUi(self)
        self.exec_gifs()
        self.jarvisUi.pushButton_2.clicked.connect(self.on_enter_pressed)
        self.jarvisUi.pushButton.clicked.connect(self.close)

        # Set the color of the text in plainTextEdit (Terminal output) to white
        self.jarvisUi.plainTextEdit.setStyleSheet("color: white; background-color: black;")
        
        # Set the text input box color (lineEdit) to white as well
        self.jarvisUi.lineEdit.setStyleSheet("color: white; background-color: black;")
        
        # Initially disable the text input box
        self.jarvisUi.lineEdit.setEnabled(True)

        # Start listening for speech input in a separate thread
        self.start_listening_thread()

        # Initialize flag to check if we are asking for company name input
        self.ask_for_company = False

    def exec_gifs(self):
        """Executes background GIFs."""
        # Background GIF
        self.jarvisUi.backk = QMovie("Jarviss_giphys/back.gif")
        self.jarvisUi.label_5.setMovie(self.jarvisUi.backk)
        self.jarvisUi.backk.start()

        # GIF for listening
        self.jarvisUi.listening = QMovie("Jarviss_giphys/lisnening.gif")
        self.jarvisUi.label_4.setMovie(self.jarvisUi.listening)
        self.jarvisUi.listening.start()
        # GIF for speaking
        self.jarvisUi.speak = QMovie("Jarviss_giphys/speaking.gif")
        self.jarvisUi.label_2.setMovie(self.jarvisUi.speak)
        self.jarvisUi.speak.start()
        # GIF for waiting
        self.jarvisUi.wait = QMovie("Jarviss_giphys/waiting.gif")
        self.jarvisUi.label_3.setMovie(self.jarvisUi.wait)
        self.jarvisUi.wait.start()

    def show_speaking_gif(self):
        self.jarvisUi.label_2.setVisible(True)  # Show speaking GIF
        self.jarvisUi.label_3.setVisible(False)  # Hide waiting GIF
        self.jarvisUi.label_4.setVisible(False)  # Hide listening GIF

    def show_listening_gif(self):
        self.jarvisUi.label_2.setVisible(False)  # Hide speaking GIF
        self.jarvisUi.label_3.setVisible(False)  # Hide waiting GIF
        self.jarvisUi.label_4.setVisible(True)   # Show listening GIF

    def show_waiting_gif(self):
        self.jarvisUi.label_2.setVisible(False)  # Hide speaking GIF
        self.jarvisUi.label_3.setVisible(True)   # Show waiting GIF
        self.jarvisUi.label_4.setVisible(False)  # Hide listening GIF


    def on_enter_pressed(self):
        """Handles user input on pressing Enter button."""
        user_input = self.jarvisUi.lineEdit.text().strip().lower()
        if user_input:
            self.process_input(user_input)

    def process_input(self, input_text):
        response = self.get_ai_response(input_text)
        self.jarvisUi.plainTextEdit.appendPlainText(f"Jarvis says: {response}")
        self.speak_response(response)

    def get_ai_response(self, input_text):
        return edd(input_text)
        
    def speak_response(self, response):
        """Speaks out the response using pyttsx3 and shows speaking GIF."""
        self.show_speaking_gif()
        engine.say(response)
        engine.runAndWait()
        self.show_waiting_gif()  # Return to waiting GIF after speaking

    def listen_for_speech(self):
        """Listens for speech input from the user and processes it in a loop."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            while True:  # Continuous loop for listening
                self.show_listening_gif()
                self.jarvisUi.plainTextEdit.appendPlainText("Listening for speech...")
                recognizer.adjust_for_ambient_noise(source)
                try:
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    self.jarvisUi.plainTextEdit.appendPlainText(f"You said: {command}")
                    self.process_input(command)
                except sr.UnknownValueError:
                    self.jarvisUi.plainTextEdit.appendPlainText("Sorry, I could not understand that.")
                except sr.RequestError:
                    self.jarvisUi.plainTextEdit.appendPlainText("Speech service is unavailable.")
                except Exception as e:
                    self.jarvisUi.plainTextEdit.appendPlainText(f"Error: {str(e)}")
                finally:
                    self.show_waiting_gif()  # Show waiting GIF after listening

    def start_listening_thread(self):
        """Start a separate thread to listen for speech."""
        listen_thread = threading.Thread(target=self.listen_for_speech)
        listen_thread.daemon = True  # Ensure the thread terminates when the main program ends
        listen_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GUIs_jarvis()
    widget.show()
    sys.exit(app.exec())
