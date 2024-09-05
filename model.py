import os
from time import sleep
from Speak import Speak

current_dir = os.getcwd()
blend_name="hand.blend"
blend_path = os.path.join(current_dir,blend_name)
import speech_recognition as sr

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
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








def model():
    kk = MicExecution()
    kk = str(kk).replace(".","")
    if 'model' in kk or 'modal' in kk or 'hand' in kk or 'arm' in kk or 'robotic arm' in kk:
        Speak("Generating the three D model!")
        sleep(15)
        Speak("The model is ready. Have a look sir!")
        sleep(4)
        os.startfile(blend_path)
model()
    
        

    

        
