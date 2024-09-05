import os
current_dir = os.getcwd()
key_name="key.txt"
key_path = os.path.join(current_dir,key_name)
fileopen = open(key_path,"r")
chat_name="chatlog.txt"
chat_path=os.path.join(current_dir,chat_name)
API = fileopen.read()
fileopen.close()


import openai
from dotenv import load_dotenv



openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    FileLog = open(chat_path,"r")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open(chat_path,"w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer







