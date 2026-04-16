from flask import Flask, request, jsonify
import os
import json
from utils.predict import predict_image

app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load solutions
with open("solutions.json") as f:
    solutions = json.load(f)

@app.route("/")
def home():
    return "Plant Disease Detection API Running"

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    disease_full, confidence = predict_image(file_path)

    plant, disease = disease_full.split("___")
    info = solutions.get(disease_full, {})

    if confidence < 0.4 or  "Corn" in disease_full or "Maize" in disease_full or "Tomato" in disease_full:
        return jsonify({
            "error": "Please upload a clear plant leaf image"})
    
    else:
        return jsonify({
            "plant": plant,
            "disease": disease,
            "confidence": round(confidence, 4),
            "description": info.get("description", "No data available"),
            "treatment": info.get("treatment", "No data available"),
            "prevention": info.get("prevention", "No data available"),
            "organic": info.get("organic", "No data available")
        })

if __name__ == "__main__":
    app.run(debug=True)
