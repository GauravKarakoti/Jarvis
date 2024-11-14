import pyttsx3
import pywhatkit
import webbrowser as web
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0


def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation



# 3 - Connect

def MicExecution():
    query = Listen()
    data = query
    return data

MicExecution()


def Speak(Text):
     engine = pyttsx3.init("sapi5")
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     engine.setProperty('rate',170)
     print("")
     print(f"You : {Text}.")
     print("")
     engine.say(Text)
     engine.runAndWait()

def searchYoutube(query):
    if "youtube" in query:
        Speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Speak("Done, Sir")
