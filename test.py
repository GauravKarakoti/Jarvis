import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_image(model, img_path):
    img_array = load_and_preprocess_image(img_path)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions)
    return decoded_predictions[0]

def main():
    # Load the MobileNetV2 model pre-trained on ImageNet data
    model = MobileNetV2(weights='imagenet')

    # Get the path to the image from the user
    image_path = input("Enter the path to the image: ")

    # Classify the image
    predictions = classify_image(model, image_path)

    # Display the top three predictions
    print("Top predictions:")
    for i, (imagenet_id, label, score) in enumerate(predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

if __name__ == "__main__":
    main()