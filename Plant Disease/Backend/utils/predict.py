import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import json

# Load model
model = load_model("model/plant_disease_model.keras")

# Load class labels
with open("model/class_labels.json") as f:
    class_labels = json.load(f)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = class_labels[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return predicted_class, confidence
