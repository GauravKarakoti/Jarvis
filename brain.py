from Speak2 import Speak
import os 
current_dir = os.getcwd()
file_name="SpeechRecognition.txt"
file_path = os.path.join(current_dir,file_name)
filename="his_chat.txt"
filepapth=os.path.join(current_dir,filename)
filenaam="data.txt"
fillepapth=os.path.join(current_dir,filenaam)

from bardapi import Bard
import datetime
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard 


def CookieScrapper():
    print("\n*The extraction of essential cookies from GoogleBard has been accomplished successfully.*")
    webbrowser.open("https://bard.google.com")
    sleep(10)
    pyautogui.click(x=1215, y=59)
    sleep(5)
    pyautogui.click(x=1035, y=83)
    sleep(5)
    keyboard.press_and_release('ctrl + w')
    sleep(5)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print(f"Error: {e}")
        return None 

    SIDValue = next((item['value'] for item in json_data if item['name'] == "__Secure-1PSID"), None)
    TSValue = next((item['value'] for item in json_data if item['name'] == "__Secure-1PSIDTS"), None)
    CCValue = next((item['value'] for item in json_data if item['name'] == "__Secure-1PSIDCC"), None)

    if SIDValue and TSValue and CCValue:
        cookie_dict = {
            "__Secure-1PSID": SIDValue,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }
        print(f"Cookie 1: {SIDValue}")
        print(f"Cookie 2: {TSValue}")
        print(f"Cookie 3: {CCValue}")
        return cookie_dict
    else:
        print("Missing cookies.")
        return None

cookie_dict = CookieScrapper()

if cookie_dict:
    try:
        bard = Bard(cookie_dict=cookie_dict, multi_cookies_bool=True)
        print("*Cookies verified successfully. You can now use Bard.*")
    except Exception as e:
        print(f"Error during Bard initialization: {e}")
else:
    print("Failed to initialize Bard due to missing or invalid cookies.")

def split_and_save_paragraphs(data, filename):
        
        try:
            paragraphs = data.split('\n\n')
            with open(filename, 'w') as file:
                file.write(data)
            data = paragraphs[:2]
            separator = ', '
            joined_string = separator.join(data)
            return joined_string
        except Exception as e:
            print(e)
 

def MainExecution():

    while True:
        try:
            File = open(file_path,"r")
            Data = File.read()
            File.close()
            FileHistory = open(filepapth,"r")
            DataHistory = FileHistory.read()
            FileHistory.close()

            if str(Data)==str(DataHistory):
                sleep(0.5)
                pass

            else:
                RealQuestion = str(Data)
                results = bard.get_answer(RealQuestion)['content']
                current_datetime = datetime.datetime.now()
                formatted_time = current_datetime.strftime("%H%M%S")
                filenamedate = str(formatted_time) + str(".txt")
                filenamedate = fillepapth + filenamedate
                print(split_and_save_paragraphs(results, filename=filenamedate))

                FileHistory = open(filename,"w")
                FileHistory.write(Data)
                FileHistory.close()

        except Exception as e:
            Speak(e)

MainExecution()