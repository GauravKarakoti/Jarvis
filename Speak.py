from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from time import sleep

import os 
current_dir = os.getcwd()
chrome_name="chromedriver.exe"
chrome_path = os.path.join(current_dir,chrome_name)

chrome_option= Options()
#chrome_option.add_argument('--headless')
chrome_option.headless = True
Path =chrome_path
driver = webdriver.Chrome(options=chrome_option)
driver.minimize_window()


website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[3]/div[2]/form/select'))
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
        driver.find_element(by=By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(by=By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()

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
