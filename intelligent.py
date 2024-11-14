from newAI import edd
from Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from awaj import jarvis_intro
print(">> Started The Jarvis : Wait For Few Seconds More")

def MainExecution():
    jarvis_intro()
    from Speak2 import Speak

    while True:
        Data = MicExecution()
        Data = str(Data).replace(".","")

        if len(Data)<3:
            pass

        elif "creative execution" in Data:
            from imggenrator import tt
            tt()

        elif 'the time' in Data:
            import datetime
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strtime}")

        elif "youtube" in Data:
            from yt import searchYoutube
            searchYoutube(Data)

        elif 'google search' in Data:
            import wikipedia as googlescrap
            Data = Data.replace("Jarvis","")
            Data = Data.replace("google search","")
            Data = Data.replace("google","")
            Speak("This is what I found on the web!")
            import pywhatkit
            pywhatkit.search(Data)

            try:
                results = googlescrap.summary(Data,1)
                Speak(results)

            except:
                Speak("No speakable data available")

        elif "temperature" in Data:
            import requests
            from bs4 import BeautifulSoup
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"current{search} is {temp}")

        elif "weather" in Data:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"current{search} is {temp}")

        elif "screenshot" in Data or 'ss' in Data:
            import pyautogui 
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            Speak("Screenshot Saved")

        elif 'nasa news' in Data:
            Speak("Tell me the date for extraction process")
            from nasa import NasaNews
            NasaNews() 

        elif "list " in Data or 'list of  17  ' in Data:
            from Speak2 import Speak
            Speak('''The 17 Sustainable Goals are as follows :
1 No Poverty
2 Zero Hunger
3 Good Health and Wellbeing
4 Quality Education
5 Gender Equality
6 Clean water and Sanitation
7 Affordable and Clean Energy
8 Decent Work and Economic Growth
9 Industry, Innovation and Infrastructure
10 Reduced Inequalities
11 Sustainable Cities and Communities
12 Responsible Consumption and Production
13 Climate Action
14 Life Below Water
15 Life on Land
16 Peace, Justice and Strong Institutions
17 Partnership Goals''')

        elif 'full screen' in Data:
            import pyautogui
            pyautogui.press("f") 

        elif 'skip' in Data:
            import pyautogui
            pyautogui.press("l")   

        elif 'back' in Data:
            import pyautogui
            pyautogui.press("j") 

        elif 'next video' in Data:
            import pyautogui
            pyautogui.press("Shift, N")  

        elif 'previous video' in Data:
            import pyautogui
            pyautogui.press("Shift, P")

        elif 'play from beginning' in Data:
            import pyautogui
            pyautogui.press("0")

        elif "pause" in Data:
            import pyautogui
            pyautogui.press("k")
            Speak("video paused")

        elif "play" in Data:
            import pyautogui
            pyautogui.press("k")
            Speak("video played")

        elif "mute" in Data or 'unmute' in Data:
            import pyautogui
            pyautogui.press("m")
            Speak("video muted")

        elif "open" in Data:
            from dictapp import openappweb
            openappweb(Data)

        elif "close" in Data:
            from dictapp import closeappweb
            closeappweb(Data)

        elif "what is your name" in Data:
            Speak("My Name is jarvis , programmed by meambers of team Jarvis")

        elif 'graph' in Data:
            from Comparision_Graph import graph_creator
            Speak("Processing")    
            graph_creator()

        elif "whatsapp message" in Data:
            pass

        elif "shutdown the system" in Data:
            import os
            os.system("shutdown /s /t 1")

        elif 'go to sleep' in Data or 'you can go' in Data:
            Speak("Terminating")
            break

        else:
            Reply = edd(Data)
            Speak(Reply)

MainExecution()
