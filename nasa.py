import requests
from PIL import Image
from io import BytesIO
import datetime
import os
from GUI import SetAssistantStatus,ShowTextToScreen
from TextToSpeech import TextToSpeech

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "qVnvwCyDg8fOUPULY1J9dEHBgguk78BHuroyzsxE"  # Replace with your actual API key

# Function to save the image and data
def save_apod_image_and_data(date, title, explanation, image_url):
    # Define the directory where you want to save the image and data
    save_directory = r"Data\NASA_data"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Save the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()  # Ensure the image is fetched successfully
    image = Image.open(BytesIO(image_response.content))
    
    # Construct a filename for the image
    image_filename = os.path.join(save_directory, f"{date}_apod_image.jpeg")
    image.save(image_filename)

    # Save the title and explanation to a text file
    text_filename = os.path.join(save_directory, f"{date}_apod_data.txt")
    with open(text_filename, "w") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Description: {explanation}\n")

    ShowTextToScreen(f"Image saved as {image_filename}")
    ShowTextToScreen(f"Data saved as {text_filename}")
    

def fetch_apod_image(date):
    params = {
        "api_key": API_KEY,
        "date": date,
    }

    try:
        # Make a GET request to the NASA APOD API
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        data = response.json()

        # Check if the media type is an image
        if data.get("media_type") == "image":
            image_url = data["url"]  # Image URL from the API
            title = data.get("title", "Astronomy Picture of the Day")
            explanation = data.get("explanation", "No description available.")
            
            # Display the image in a window
            image_response = requests.get(image_url)
            image_response.raise_for_status()  # Check if the image fetch was successful
            image = Image.open(BytesIO(image_response.content))
            image.show(title=title)

            # Print the title and description in the console
            print(f"Title: {title}")
            print(f"Description: {explanation}")

            # Save the image and data to files
            save_apod_image_and_data(date, title, explanation, image_url)
            
        else:
            print("The APOD for this date is not an image. Please try a different date.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NASA: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def NasaNews(extraction_date):
    date_str = extraction_date
    
    try:
        # Validate date format
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        fetch_apod_image(date_str)
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")