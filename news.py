import requests
import json


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


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=438564c18a6443a999bae60e66956d87",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=438564c18a6443a999bae60e66956d87",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=438564c18a6443a999bae60e66956d87",
            "science" :"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=438564c18a6443a999bae60e66956d87",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=438564c18a6443a999bae60e66956d87",
            "technology" :"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=438564c18a6443a999bae60e66956d87"
}

    content = None
    url = None
    Speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
        if url is True:
            print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news['articles']
    for articles in arts :
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    Speak("thats all")