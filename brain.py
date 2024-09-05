from Speak2 import Speak
import os 
current_dir = os.getcwd()
file_name="SpeechRecognition.txt"
file_path = os.path.join(current_dir,file_name)
filename="his_chat.txt"
filepapth=os.path.join(current_dir,filename)
filenaam="data.txt"
fillepapth=os.path.join(current_dir,filenaam)

from bardapi import BardCookies
import datetime
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard 


def CookieScrapper():
    print("")
    print("*The extraction of essential cookies from GoogleBard has been accomplished successfully.*")
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
        pass

    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
     
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")
 
        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue ,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        print("")
        print(f"===> Cookie 1 - {SIDValue}")
        print(f"===> Cookie 2 - {TSValue}")
        print(f"===> Cookie 3 - {CCValue}")
        print("")
        return cookie_dict

    except Exception as e:
        Speak(e)

cookie_dict = CookieScrapper()

# Initializing the GoogleBard Reverse Engineering Program

try:
    bard = BardCookies(cookie_dict=cookie_dict)
    print("*The verification of cookies has been successfully completed.*")
    print("*All processes have been completed successfully, and you now have the capability to employ JARVIS as a backend model.")
    print("")

except Exception as e:
    print("*The verification of cookies has encountered an issue and has not been successful.*")
    print("*This issue may arise due to the unsuccessful extraction of cookies from the extension.*")
    print(e)
 
# Initiating the text modification function to generate a summarized version of the result text.

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