from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib
from Listen import MicExecution
import os 

current_dir = os.getcwd()
chrome_name="chromedriver.exe"
chrome_path = os.path.join(current_dir,chrome_name)
pi_name="piHistory.txt"
pi_path=os.path.join(current_dir,pi_name)

chatpi_name="Chatnumberpi.txt"
chatpi_path=os.join(current_dir,chatpi_name)


warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
scriptDirectory = pathlib.Path().absolute()
chrome_driver_path = chrome_path
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(20)

def Introduction():

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys("Hello")
    
    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys("Hello")

    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
    sleep(1)

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
    
    except:
        pass

    try:
        VoicesToBeChoosen = "1"
        XPathVoice = f"/html/body/div/main/div/div/div[2]/div/div[2]/button[{VoicesToBeChoosen}]"
        driver.find_element(by=By.XPATH,value=XPathVoice).click()
        sleep(1)

        try:
            driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
        except:
            pass

    except:
        pass

    FileHistory = open(chatpi_path,"w")
    FileHistory.write('1')
    FileHistory.close()
    FileReadNow = open(pi_path,"w")
    FileReadNow.write('1')
    FileReadNow.close()

def PopUpRemover():

    try:
        popup = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[4]/div/div/div[1]").is_enabled()
        if str(popup)=="True":
            driver.refresh()
            sleep(2)

        else:
            pass

    except:
        pass

def QuerySender(Query):

    Query = str(Query)

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(Query)

    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(Query)

    sleep(0.5)

def ButtonClicker():

    while True:

        SendButton = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").is_enabled()

        if True==SendButton:
            driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
            sleep(1)
            break

def CheckBackSoon(Query):

    Button = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div").text

    if "Apologies, an unexpected error has occurred. Please check back again soon."==str(Button):
        driver.refresh()
        driver.refresh()
        driver.refresh()
        sleep(2)
        QuerySender(Query=Query)
        ButtonClicker()

    else:
        pass

def AnswerReturn(Query):

    Query = str(Query)

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(Query)

    except:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(Query)

    sleep(0.5)

    while True:

        SendButton = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/button").is_enabled()

        if True==SendButton:

            try:
                Text = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div").text
                print(Text)
                sleep(0.5)
                try:
                    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                except:
                    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                sleep(0.5)

            
            except:
                Text = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div').text
                print(Text)
                sleep(0.5)
                try:
                    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                except:
                    driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                sleep(0.5)
            
            FileHistory = open(chatpi_path,"w")
            FileHistory.write('1')
            FileHistory.close()

            break
        
        else:
            FileRead = open(chatpi_path,"r")
            Data = FileRead.read()
            FileRead.close()

            if str(Data)=='80':
                driver.refresh()
                sleep(2)

                try:
                    Text = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div").text
                    print(Text)
                    sleep(0.5)

                    try:
                        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                    except:
                        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                    sleep(0.5)

                except:
                    Text = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div').text
                    print(Text)
                    sleep(0.5)
                    try:
                        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").clear()

                    except:
                        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").clear()

                    sleep(0.5)
                    
                break

            else:
                FileRead = open(chatpi_path,"r")
                Data = FileRead.read()
                FileRead.close()
                FileHistory = open(chatpi_path,"w")
                NewData = int(Data) + 1
                NewData = str(NewData)
                FileHistory.write(NewData)
                FileHistory.close()
                sleep(0.5)

def NotNowChecker():

    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
        sleep(1)

    except:
        pass
    
    try:
        driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
        sleep(1)

    except:
        pass
    
PopUpRemover()
Introduction()

while True:
    Query = MicExecution()
    Query = str(Query).replace(".","")
    File = open(pi_path,"r")
    DataRead = File.read()
    File.close()

    if str(DataRead)=="49":
        driver.delete_all_cookies()
        sleep(2)
        driver.refresh()
        driver.refresh()
        driver.refresh()
        sleep(2)
        QuerySender(Query=Query)
        ButtonClicker()
        CheckBackSoon(Query=Query)
        NotNowChecker()
        AnswerReturn(Query=Query)
        FileReadNow = open(pi_path,"w")
        FileReadNow.write('1')
        FileReadNow.close()
        
    else:
        try:
            QuerySender(Query=Query)
            ButtonClicker()
            CheckBackSoon(Query=Query)
            NotNowChecker()
            AnswerReturn(Query=Query)
            FileReadNow = open(pi_path,"w")
            NewDataRead = int(DataRead) + 1
            FileReadNow.write(str(NewDataRead))
            FileReadNow.close()

        except Exception as e:
            print(e)