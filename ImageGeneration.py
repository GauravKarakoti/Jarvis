import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os
from time import sleep

# Constants
DATA_DIR = os.path.join(os.getcwd(), "Data")
FRONTEND_DIR = os.path.join(os.getcwd(), "Frontend", "Files")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {get_key('.env', 'HuggingFaceAPIKey')}"}

os.makedirs(DATA_DIR, exist_ok=True)  # Ensure the Data directory exists
os.makedirs(FRONTEND_DIR, exist_ok=True)  # Ensure the Frontend/Files directory exists

# Function to open and display images
def open_images(prompt):
    prompt = prompt.replace(" ", "_")  # Replace spaces with underscores
    files = [f"{prompt}{i}.jpg" for i in range(1, 5)]  # List of image filenames

    for file_name in files:
        image_path = os.path.join(DATA_DIR, file_name)

        try:
            img = Image.open(image_path)
            print(f"Opening image: {image_path}")
            img.show()
            sleep(1)  # Pause for 1 second before showing the next image
        except IOError:
            print(f"Unable to open {image_path}")

# Async function to query the API
async def query(payload):
    response = await asyncio.to_thread(requests.post, API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        print(f"API error: {response.status_code} - {response.text}")
        return None

# Async function to generate images
async def generate_images(prompt: str):
    tasks = []

    # Create 4 image generation tasks
    for i in range(4):
        seed = randint(0, 1000000)
        payload = {
            "inputs": f"{prompt}, quality=4K, sharpness=maximum, Ultra High details, high resolution, seed={seed}",
        }
        task = asyncio.create_task(query(payload))
        tasks.append(task)

    # Wait for all tasks to complete
    image_bytes_list = await asyncio.gather(*tasks)

    # Save the generated images to files
    for i, image_bytes in enumerate(image_bytes_list, start=1):
        if image_bytes:
            file_path = os.path.join(DATA_DIR, f"{prompt.replace(' ', '_')}{i}.jpg")
            with open(file_path, "wb") as f:
                f.write(image_bytes)
        else:
            print(f"Failed to generate image {i} for prompt '{prompt}'")

# Wrapper function to generate and open images
def GenerateImages(prompt: str):
    asyncio.run(generate_images(prompt))  # Run the async image generation
    open_images(prompt)  # Open the generated images

# Main loop to monitor and handle image generation requests
while True:
    try:
        data_file_path = os.path.join(FRONTEND_DIR, "ImageGeneration.data")
        
        with open(data_file_path, "r") as f:
            data = f.read().strip()

        # Read prompt and status from the file
        if not data:
            sleep(1)
            continue

        prompt, status = data.split(",")
        prompt = prompt.strip()
        status = status.strip()

        # If the status indicates an image generation request
        if status.lower() == "true":
            print("Generating Images ...")
            GenerateImages(prompt=prompt)

            # Update the file to indicate the request is processed
            with open(data_file_path, "w") as f:
                f.write("False,False")
                break  # Exit the loop after processing the request

        else:
            sleep(1)  # Wait before checking again

    except FileNotFoundError:
        print(f"File '{data_file_path}' not found. Waiting...")
        sleep(1)

    except:
        pass

