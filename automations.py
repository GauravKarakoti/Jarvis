import datetime 
import os

from Speak2 import Speak


import speech_recognition as sr 
current_dir = os.getcwd()
file_name="nOTEPAD"
file_path = os.path.join(current_dir,file_name)
def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)
    
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

def NotePad():
   
    Speak("Tell Me The Query!")
    Speak("I am ready to write")

    writes = MicExecution()

    strtime = datetime.datetime.now().strftime("%H:%M:%S")

    filenam = str(strtime).replace(":","-") + "-note.txt"

    with open(filenam,"w") as file:

        file.write(writes)

    path_1 = file_path + str(filenam)
    
    path_2 = file_path+ str(filenam)

    os.rename(path_1,path_2)

    os.startfile(path_2)