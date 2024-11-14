import requests
from PIL import Image
from io import BytesIO
import datetime
import pyttsx3  # For text-to-speech functionality

# NASA APOD API URL and your API key
API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "qVnvwCyDg8fOUPULY1J9dEHBgguk78BHuroyzsxE"  # Replace with your actual API key

# Function for text-to-speech
def Speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def fetch_apod_image(date):
    # API parameters
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
            
            # Fetch the image
            image_response = requests.get(image_url)
            image_response.raise_for_status()  # Check if the image fetch was successful
            image = Image.open(BytesIO(image_response.content))

            # Display the image in a window
            image.show(title=title)

            # Print the title and description in the console
            print(f"Title: {title}")
            print(f"Description: {explanation}")

            # Speak the title and description
            Speak(f"Title: {title}")
            Speak(f"Description: {explanation}")
            
        else:
            print("The APOD for this date is not an image. Please try a different date.")
            Speak("The APOD for this date is not an image. Please try a different date.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from NASA: {e}")
        Speak(f"Error fetching data from NASA: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        Speak(f"An error occurred: {e}")

def NasaNews():
    # Get date input from user in YYYY-MM-DD format
    date_str = input("Enter a date (YYYY-MM-DD): ")
    try:
        # Validate date format
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        fetch_apod_image(date_str)
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        Speak("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Call main function
if __name__ == "__main__":
        NasaNews