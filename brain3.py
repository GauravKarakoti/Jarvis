import os
import openai

current_dir = os.getcwd()
key_name = "key.txt"
key_path = os.path.join(current_dir, key_name)
chat_name = "chatlog.txt"
chat_path = os.path.join(current_dir, chat_name)

with open(key_path, "r") as fileopen:
    API = fileopen.read().strip()

openai.api_key = API

def ReplyBrain(question, chat_log=None):

    with open(chat_path, "r") as filelog:
        chat_log_template = filelog.read()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You: {question}\nJarvis: '

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    answer = response.choices[0].text.strip()

    chat_log_template_update = chat_log_template + f"\nYou: {question}\nJarvis: {answer}"
    
    with open(chat_path, "w") as filelog:
        filelog.write(chat_log_template_update)

    return answer
ReplyBrain("hi")
