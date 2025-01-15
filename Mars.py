import requests
from PIL import Image
from io import BytesIO
import os

# NASA API Key
API_KEY = "0TG3HQUdRfeXfPzgWCRhoPwqXdCyqY8WWtX6E8DK"

# Directory to save Mars images and metadata
SAVE_DIRECTORY = "Mars_data"

def save_mars_image_and_data(rover_name, date, image_url, camera_name, metadata):
    """ Saves the Mars Rover image and metadata to a file. """
    
    # Ensure the save directory exists
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    # Fetch and save the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    image = Image.open(BytesIO(image_response.content))
    
    # Construct filenames
    image_filename = os.path.join(SAVE_DIRECTORY, f"{rover_name}{date}{camera_name}.jpeg")
    text_filename = os.path.join(SAVE_DIRECTORY, f"{rover_name}{date}{camera_name}.txt")

    # Save image
    image.save(image_filename)

    # Save metadata
    with open(text_filename, "w") as file:
        file.write("==== MARS ROVER IMAGE DATA ====\n")
        for key, value in metadata.items():
            file.write(f"{key}: {value}\n")

    print(f"✅ Image saved: {image_filename}")
    print(f"✅ Metadata saved: {text_filename}\n")


def MarsImg():
    """ Fetches, displays, and saves Mars Rover images with metadata. """
    rover_name = 'curiosity'  # Choose: curiosity, opportunity, spirit, perseverance
    date = '2015-03-09'  # Change this to any valid Earth date

    # Construct API URL
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos?earth_date={date}&api_key={API_KEY}"

    print(f"🚀 Fetching Mars Rover images for {rover_name} on {date}...\n")

    try:
        # Fetch data from NASA API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract photos
        photos = data.get("photos", [])
        if not photos:
            print("⚠ No photos available for this date.")
            return

        # Display rover information
        rover_info = photos[0]["rover"]
        print(f"🔍 Rover Name: {rover_info['name']}")
        print(f"📅 Launch Date: {rover_info['launch_date']}")
        print(f"🛬 Landing Date: {rover_info['landing_date']}")
        print(f"🔴 Mission Status: {rover_info['status']}\n")

        # Process up to 5 images
        for i, photo in enumerate(photos[:5]):
            image_url = photo["img_src"]
            camera_name = photo["camera"]["full_name"]

            # Metadata for saving
            metadata = {
                "Rover Name": rover_info["name"],
                "Launch Date": rover_info["launch_date"],
                "Landing Date": rover_info["landing_date"],
                "Mission Status": rover_info["status"],
                "Earth Date": date,
                "Camera": camera_name,
                "Image URL": image_url
            }

            print(f"📸 Image {i+1}: Captured by {camera_name}")
            print(f"🌍 Image URL: {image_url}\n")

            # Fetch and show image
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image = Image.open(BytesIO(image_response.content))
            image.show()

            # Save image and metadata
            save_mars_image_and_data(rover_name, date, image_url, camera_name, metadata)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data from NASA API: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Run the function
MarsImg()