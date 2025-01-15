from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pathlib
import time
import keyboard

def Whatsapp(Recipient_name, msg_recipient):
    # Define the recipient name and message
    Name = Recipient_name  # Ensure case consistency
    mesg = msg_recipient

    # WhatsApp contact dictionary (Update numbers as needed)
    ListWeb = {
        'yash': "+917683015091"
    }

    # Check if the recipient exists in the dictionary
    if Name not in ListWeb:
        print(f"Error: Sir {Name} not found in your contact list.")
        exit()  # Exit the function if the recipient is not found
        return

    # Set up Chrome options
    scriptDirectory = pathlib.Path().absolute()
    chrome_option = Options()
    chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_option.add_argument("--profile-directory=Default")
    chrome_option.add_argument(f"user-data-dir={scriptDirectory}\\userdata")  # Use existing WhatsApp login session

    # Initialize WebDriver
    PathofDriver = "..\chromedriver.exe"  # Make this dynamic if possible
    driver = webdriver.Chrome(options=chrome_option)
    
    try:
        driver.maximize_window()
        driver.get("https://web.whatsapp.com/")
        print("Initializing WhatsApp Web...")
        
        # Wait for the QR code scan/login
        time.sleep(10)
        keyboard.press_and_release('alt + tab')

        # Generate the WhatsApp Web message URL
        Number = ListWeb[Name]
        LinkWeb = f'https://web.whatsapp.com/send?phone={Number}&text={mesg}'
        driver.get(LinkWeb)

        # Wait for the chat box to load
        time.sleep(5)

        # Find and click the send button
        send_button_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span'
        try:
            send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, send_button_xpath)))
            send_button.click()
            print("Message Sent Successfully!")
        except Exception as e:
            print("Error: Could not send message.", e)

    except Exception as e:
        print("Unexpected Error:", e)
    
    finally:
        # Keep the browser open for a while before closing
        time.sleep(2)
    