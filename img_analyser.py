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
    print("*The extraction of essential data from homeserver has been accomplished successfully.*")
    webbrowser.open("https://bard.google.com")
    sleep(5)
    pyautogui.click(x=1212, y=55)
    sleep(2)
    pyautogui.click(x=968, y=204)
    sleep(2)
    pyautogui.click(x=996, y=91)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading data has been executed without any issues, and the data are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        print("data Loaded Unsuccessfully")
        print("""*The error has been identified as a result of unsuccessful data replication from the homeserver, 
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
        print(f"===> data 1 - {SIDValue}")
        print(f"===> data 2 - {TSValue}")
        print(f"===> data 3 - {CCValue}")
        print("")
        return cookie_dict

    except Exception as e:
        print(e)

cookie_dict = CookieScrapper()


try:
    bard = BardCookies(cookie_dict=cookie_dict)
    print("*The verification of data has been successfully completed.*")
    print("*All processes have been completed successfully, and you now have the capability to use this function.")
    print("")

except Exception as e:
    print("*The verification of data has encountered an issue and has not been successful.*")
    print("*This issue may arise due to the unsuccessful extraction of data from the homeserver.*")
    print(e)


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


def imgdetection():

    while True:

        try:
            imagename = str(input("Enter The Image Name : "))
            image = open(imagename,'rb').read()
            bard = BardCookies(cookie_dict=cookie_dict)
            results = bard.ask_about_image('what is in the image?',image=image)['content']
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H%M%S")
            filenamedate = str(formatted_time) + str(".txt")
            filenamedate = r"E:\MIST_AI\database" + filenamedate
            print(split_and_save_paragraphs(results, filename=filenamedate))
            
        except Exception as ex:
            print(ex)

imgdetection()