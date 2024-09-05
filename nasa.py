import requests
import os
from PIL import Image

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import datetime
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


import speech_recognition as sr 
from googletrans import Translator 


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







def MicExecution():
    query = Listen()
    data = query
    return data



Api_Key = "v8cq2s9bXGBdTO3RBXzoAMIHRhpjCamA4l8AAC9m"

def NasaNews(Date):
    Speak("Extracting data from nasa")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key) 
    Params = {'date':str(Date)}
    r = requests.get(Url,params = Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    Filename = str(Date) + '.jpeg'
    with open(Filename,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\Ayush\\Desktop\\jarvis\\my ai\\" + str(Filename)
    Path_2 = "C:\\Users\\Ayush\\Desktop\\jarvis\\my ai\\nasa data\\" + str(Filename)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")



    




   

