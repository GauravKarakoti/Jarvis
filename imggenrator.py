import requests
from PIL import Image
from io import BytesIO

# Pollinations API URL
# def img_gen():

API_URL = "https://image.pollinations.ai/prompt/"

def fetch_image_from_pollinations(prompt):
        # Make a GET request to Pollinations.ai API with the prompt
        response = requests.get(API_URL + prompt)

        if response.status_code == 200:
            # The API returns the generated image directly
            image = Image.open(BytesIO(response.content))
            
            # Display the image in a window
            image.show(title=f"Generated Image for: {prompt}")
        else:
            print("Failed to fetch image. Please try again with a different prompt.")

def tt():
        # Get text prompt input from user
        prompt = input("Enter a text prompt for image generation: ")
        fetch_image_from_pollinations(prompt)
