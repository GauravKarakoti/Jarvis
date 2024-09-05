from Speak2 import Speak
import os 
current_dir = os.getcwd()
key_name="key.txt"
key_path = os.path.join(current_dir,key_name)

text_name="text.text"
text_path = os.path.join(current_dir,text_name)


# Api Key
fileopen = open(key_path,"r")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv import load_dotenv

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionAns(question,chat_log = None):
    FileLog = open(text_path,"r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open(text_path,"w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer



while True:
    kk = input("Enter:")
    print(QuestionAns(kk))

        






