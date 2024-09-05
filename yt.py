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


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):

    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass

    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()

        if lengthoftext>=30:
            sleep(4)

        elif lengthoftext>=40:
            sleep(6)

        elif lengthoftext>=55:
            sleep(8)

        elif lengthoftext>=70:
            sleep(10)

        elif lengthoftext>=100:
            sleep(13)

        elif lengthoftext>=120:
            sleep(14)

        else:
            sleep(2)


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
