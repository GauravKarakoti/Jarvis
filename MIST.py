from brain3 import ReplyBrain
from Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from clap import Tester
import speedtest
print(">> Started The Jarvis : Wait For Few Seconds More")
from main import MainTaskExecution
from intro import intro

def MainExecution():
    
    intro()         
    from Speak import Speak
        #Speak(" MIST onboard sir!")
        #Speak("Initiating all commands!")
        #Speak("Everything operational sir!")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif 'the time' in Data:
            import datetime
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strtime}")
        
        elif "vision" in Data:
            from hand_automations import computer_vision
            computer_vision()

        elif 'gmail' in Data:
            from gmail import gmail
            gmail()

        elif "play games" in Data :
            from game import game_play ,  guessing_game, tic_tac_toe,ludo
            print('''Press "A": Rock , Paper , Scissor 
                     Press "B": Guessing Game 
                     Press "C": Tic-Tac-Toe 
                     
                     Press "Q" : Quit''')
            while True :
                alpha=input("Enter Your Choice : ")
                if len(alpha)> 1 :
                    Speak("Choose from above options") 
                elif "A" == alpha :
                    game_play()
                elif "B" == alpha :
                    guessing_game()
                elif "C" == alpha :
                    tic_tac_toe()
               
                elif "Q" == alpha :
                    break
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

        elif "3d model" in Data :
            from model import model
            model()


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

        elif "internet speed" in Data:
                   
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    Speak(f"Wifi download speed is {download_net}")
                    Speak(f"Wifi Upload speed is {upload_net}")

        elif 'note' in Data or 'write' in Data:
            from automations import NotePad
            NotePad()
            
        elif "screenshot" in Data or 'ss' in Data:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")


        elif 'nasa Data' in Data:
            Speak("Tell me the date for extraction process")
            from nasa import NasaNews
            NasaNews() 

        elif "news" in Data :
            from news import latestnews
            latestnews()    

        elif "list " in Data or 'list of  17  ' in Data :
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

        
        elif 'graph' in Data:
            from Comparision_Graph import graph_creator
            Speak("Processing")    
            graph_creator()

        elif "whatsapp message" in Data:
            from whatsapp import WhatsappSender
            WhatsappSender()

        elif "current location" in Data :
            from location import system_locater
            system_locater()
        
        elif "find location" in Data :
            from location import asked_location
            asked_location()
            
        elif "shutdown the system" in Data:
            import os
            os.system("shutdown /s /t 1")
        
        elif 'go to sleep' in Data or 'you can go' in Data:
            Speak("Terminating")
            break
        
        else:
           Reply = ReplyBrain(Data)
           Speak(Reply)

'''def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
        
    else:
        pass

ClapDetect()'''
MainExecution()





