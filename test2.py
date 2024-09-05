import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
import warnings

warnings.filterwarnings("ignore")

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_image(model, img_path):
    img_array = load_and_preprocess_image(img_path)
    predictions = model.predict(img_array)
    return predictions

def main():
    base_model = EfficientNetB0(weights='imagenet', include_top=True)
    image_path = input("Enter the path to the image: ")

    try:
        raw_predictions = classify_image(base_model, image_path)
        print("Raw predictions:")
        print(raw_predictions)

        decoded_predictions = decode_predictions(raw_predictions)
        print("Top predictions:")
        for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
            print(f"{i + 1}: {label} ({score:.2f})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()