from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Speak2 import Speak
import pathlib
from Listen import MicExecution
import keyboard



scriptDirectory = pathlib.Path().absolute()

chrome_option= Options()
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_option.add_argument("--profile-directory=Default")
chrome_option.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = r"E:\JARIVS_MAIN\Driver\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
print("Initializing The Whatsapp Software.")
sleep(5)
keyboard.press_and_release('alt +tab')


ListWeb = {'ayush' : "+919873482808",
            'sir': "+91",
            'gaurav': "+91",
            'papa' : "+91"}

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH, value="//div//button/span[@data-icon='send']").click()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")