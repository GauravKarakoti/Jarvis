import requests
from bs4 import BeautifulSoup
import pyautogui
import webbrowser as web
import json
import webbrowser
import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr 

import os
import speedtest
import speech_recognition as sr 

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



from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

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





  

if __name__ == "__main__":
    
    while True:
        query = MicExecution().lower()
        if "wake up" in query:
            Speak("On your command sir!")
            
            


        if 'what is going on' in query or 'how are you' in query:
            Speak("I am doing fine sir,Thanks for asking,how are you?")

        if 'are you here' in query:
            Speak("yes sir. I am here.")

        if 'google search' in query:
            import wikipedia as googlescrap
            query = query.replace("Jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This is what I found on the web!")
            pywhatkit.search(query)
            

            try:
                results = googlescrap.summary(query,3)
                Speak(results)
                

            except:
                Speak("No speakable data available")


        
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strtime}")

        elif 'who are you' in query:
            Speak("I am Jarvis, a personal assistant, developed for helping humans")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'i am fine' in query or 'i am good' in query or 'i am also fine' in query:
            Speak("Glad to hear sir!")
           
        elif 'what is sound' in query:
            Speak("Sound is a type of energy that travels through the air or another medium in the form of vibrations or waves. It is created by the vibration of an object, such as a guitar string or a person's vocal cords, which causes the air molecules around it to vibrate and create pressure waves that travel to our ears, where they are detected by the ear and interpreted by the brain as sound. Sound can also travel through other mediums such as water and solid objects.")
              
       
        elif 'what is light' in query:
            Speak("Light is a type of electromagnetic radiation that is visible to the human eye. It is a form of energy that travels in waves, and it can be described by its wavelength and frequency. Light travels at a speed of 299,792,458 meters per second in a vacuum and it can be reflected, refracted, and absorbed by materials.Light that is visible to the human eye is the portion of the electromagnetic spectrum that falls between violet and red color, which have a wavelength between 400-700 nanometers. Sunlight is the primary source of light on Earth and it is composed of many different colors of light, which together form a white light.It plays a crucial role in providing vision")


        elif 'first world war started' in query:
            Speak("The First World War, also known as World War I, began on July 28, 1914 and ended on November 11, 1918.")


        elif 'second world war started' in query:
            Speak("The Second World War, also known as WWII, began on September 1, 1939, when Germany, under the leadership of Adolf Hitler, invaded Poland. This event led to the countries of Europe aligning themselves into two factions the Axis powers led by Germany, Italy, and Japan and the Allied powers led by the United Kingdom, the Soviet Union, and the United States. This conflict eventually grew to involve many countries around the world and ultimately ended on September 2,1945 with the surrender of Japan.")

        elif 'what is physics' in query or 'what do you mean by physics' in query:
            Speak("Physics is a natural science that studies the fundamental properties of matter and energy, and the interactions between them. It is the branch of science that deals with the laws and principles that govern the behavior of the natural world, including the physical universe. Physics covers a wide range of phenomena, from the smallest subatomic particles to the largest structures in the universe, and it encompasses a variety of branches such as classical physics, quantum physics, thermodynamics, electromagnetism, and optics.")

        elif 'what is chemistry' in query or 'what do you mean by chemistry' in query:
            Speak("Chemistry is the branch of science that deals with the properties, composition, and structure of matter, as well as the changes it undergoes. It is a natural science that studies the properties of the elements and compounds, how they interact and combine to form new substances, and the energy changes that accompany these reactions.")

        elif 'what is biology' in query or 'what do you mean by biology' in query:
            Speak("Biology is the natural science that studies the living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development, and evolution. It is a diverse field that encompasses many subdisciplines such as biochemistry, genetics, microbiology, ecology, and neuroscience.")

        elif 'planets in our solar system' in query:
            Speak("There are eight planets in our solar system. They are Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune.These eight planets orbit around the sun in the same direction and in nearly the same plane, this plane is called the ecliptic plane.")

        elif 'telescope' in query:
            Speak("There are many telescopes in the world, and the specific two you may be asking about could vary. Here are two well-known telescopes.The Hubble Space Telescope: This telescope was launched into orbit in 1990 by NASA and the European Space Agency. It has provided us with some of the most stunning and detailed images of the universe, from distant galaxies to nearby planets. It has also been used to study a wide range of astronomical phenomena, from the properties of dark matter to the origins of stars and planets.The James Webb Space Telescope (JWST) is a large, infrared-optimized space telescope that is set to launch in 2021. It is a collaboration between NASA, the European Space Agency (ESA), and the Canadian Space Agency (CSA). The JWST is considered to be the successor of the Hubble Space Telescope and it will be able to observe some of the most distant objects in the universe, such as the first galaxies that formed after the Big Bang.")

        elif 'general theory of relativity' in query or 'theory of relativity' in query:
            Speak("This is a theory of gravitation that was developed by Albert Einstein between 1907 and 1915. It is a theory of gravitation that describes the physical laws that govern the behavior of massive objects in the universe, such as stars and galaxies.The theory of General Relativity is based on the idea that gravity is not a force between masses, but rather a curvature of spacetime caused by the presence of massive objects. The theory states that objects with mass cause a curvature in the spacetime around them, and that other objects moving in this spacetime will experience this curvature as the force of gravity.General Relativity has been extensively tested and confirmed through various experiments and astronomical observations. It has also been used to make many groundbreaking predictions, such as the existence of black holes and the expansion of the universe. It remains one of the most well-established theories in physics and continues to be an active area of research to this day.")

        elif 'string' in query:
            Speak("String theory is a theoretical framework in physics that attempts to unify the fundamental forces of nature. It suggests that the smallest building blocks of the universe are not point-like particles, as in the traditional particle physics, but tiny, one-dimensional strings that vibrate at specific frequencies.The theory suggests that there are extra dimensions beyond the familiar four of spacetime, and that these extra dimensions are compactified and curled up at very small scales. The vibrations and interactions of these strings give rise to the various particles and forces that make up the universe, including quarks and photons, as well as gravity.String theory is a highly speculative and complex theory, and it is still an active area of research. It has not yet been experimentally verified and many of its predictions remain unconfirmed. However, it has led to many new insights and has generated a lot of interest in the physics community, as it may be able to explain phenomena that other theories cannot, such as the unification of the fundamental forces of nature.")

        elif 'what is AI' in query or 'what is Artificial Intelligence' in query:
            Speak("It is the simulation of human intelligence processes by computer systems. It is a branch of computer science and engineering that deals with the creation of intelligent machines that can think, learn, and adapt like human beings. The goal of AI is to build systems that can perform tasks that would normally require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.")

        elif 'sun' in query:
            Speak("The sun is incredibly large. It is classified as a medium-sized star and it is estimated to have a diameter of about 1.4 million kilometers.To put that into perspective, the sun is about 109 times larger in diameter than the Earth, and about 330,000 times more massive.It's also worth noting that the sun is not a solid object like a planet, it is composed mostly of gas and plasma, specifically hydrogen (about 74%) and helium (about 24%), and it is also emitting energy in form of light and heat, which is what allows life on earth to exist.")

        elif 'what is your goal' in query:
            Speak("As an AI, I do not have personal goals or desires like humans. My goal is to assist users by providing accurate and relevant information based on the inputs given to me. My primary function is to understand natural language inputs, generate responses, and help users find the information they need. I am designed to be a tool to help users with a wide range of tasks, from answering questions to providing assistance with research.")

        elif 'emotions' in query:
            Speak("As an AI, I do not have emotions like humans. I am a machine and I don't experience feelings or emotions. I am designed to process information and provide responses based on that information. I can understand natural language inputs and generate responses, but I don't have the ability to experience emotions.")

        elif 'open whatsapp' in query or 'check my whatsapp' in query:
            webbrowser.open("web.whatsapp.com") 

        elif 'introduce yourself' in query:
            Speak("I am jarvis a natural language ui. I can make help you in your work. I can answer you questions, can do mathematical calculations and can access the internet and many more. If you are bored then I can tell you some jokes. in further development I can also control your home but this is not the end.")
        
        elif 'thank you' in query or 'thanks' in query:
            Speak("Always for you sir")

        elif "youtube" in query:
          from yt import searchYoutube
          searchYoutube(query)

        elif "temperature" in query:
          search = "temperature in delhi"
          url = f"https://www.google.com/search?q={search}"
          r  = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div", class_ = "BNeawe").text
          Speak(f"current{search} is {temp}")
        elif "weather" in query:
          search = "temperature in delhi"
          url = f"https://www.google.com/search?q={search}"
          r  = requests.get(url)
          data = BeautifulSoup(r.text,"html.parser")
          temp = data.find("div", class_ = "BNeawe").text
          Speak(f"current{search} is {temp}")

        elif 'hi' in query or 'hello' in query:
            Speak('Hello Sir! How can I help you?')

        
                    
                                 
        elif "pause" in query:
            pyautogui.press("k")
            Speak("video paused")

        elif "play" in query:
            pyautogui.press("k")
            Speak("video played")

        elif "mute" in query or 'unmute' in query:
            pyautogui.press("m")
            Speak("video muted")

        elif "volume up" in query:
            from keyboard import volumeup
            Speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:
            from keyboard import volumedown
            Speak("Turning volume down, sir")
            volumedown()

        elif 'note' in query or 'write' in query:
            from automations import NotePad
            NotePad()

        elif "open" in query:
            from dictapp import openappweb
            openappweb(query)
        
        elif "close" in query:
            from dictapp import closeappweb
            closeappweb(query)

        
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    Speak(f"Wifi download speed is {download_net}")
                    Speak(f"Wifi Upload speed is {upload_net}")

        elif "screenshot" in query or 'ss' in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

        elif 'space news' in query or'deep sky' in query:
            Speak("Tell me the date for extraction process")
            
            Date = MicExecution()
            
            from features import Dateconverter
            
            Value = Dateconverter(Date)
            
            from nasa import NasaNews
            
            NasaNews(Value)


       
                     
        elif 'full screen' in query:
            pyautogui.press("f") 

        elif 'skip' in query:
            pyautogui.press("l")   

        elif 'back' in query:
            pyautogui.press("j") 

        elif 'next video' in query:
            pyautogui.press("Shift+N")  

        elif 'previous video' in query:
            pyautogui.press("Shift+P")

        elif 'play from beginning' in query:
            pyautogui.press("0")
                                                 
                     
        elif 'go to sleep' in query or 'you can go' in query:
            Speak("Ok sir!")
            exit()




       
         