from flask import Flask, render_template, request, jsonify
import os
import uuid
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load trained CNN model
MODEL_PATH = "age_detection_model.h5"

try:
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None  # Handle model loading failure

# Upload directory for images
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure Flask to serve static files correctly
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.static_folder = "static"

# Define image size (Ensure this matches the model training size)
IMG_SIZE = (128, 128)  # Change if your model was trained on a different size

# Updated age categories to match dataset folder names
AGE_BUCKETS = ["18-24", "25-40", "41-60"]

def predict_age(img_path):
    """Predicts age category from an image file path."""
    try:
        if model is None:
            raise ValueError("Model is not loaded.")

        # Load and preprocess image
        img = image.load_img(img_path, target_size=IMG_SIZE)
        img_array = image.img_to_array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict age category
        predictions = model.predict(img_array)

        if app.debug:
            print("🔍 Model Input Shape:", model.input_shape)
            print("📊 Model Output Shape:", predictions.shape)
            print("📈 Raw Predictions:", predictions)

        if predictions is None or len(predictions) == 0:
            raise ValueError("Model returned empty predictions.")

        predicted_index = np.argmax(predictions)  # Get highest probability class

        if app.debug:
            print("🎯 Predicted Index:", predicted_index)

        if predicted_index >= len(AGE_BUCKETS):
            raise ValueError(f"Predicted index {predicted_index} out of range for AGE_BUCKETS.")

        predicted_age = AGE_BUCKETS[predicted_index]  # Map to age bucket
        return predicted_age

    except Exception as e:
        print(f"❌ Error in age prediction: {e}")
        return "undefined"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files or request.files["image"].filename == "":
        return jsonify({"error": "No image uploaded or filename is empty"}), 400

    file = request.files["image"]

    # Validate file extension
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    if "." not in file.filename or file.filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "Invalid file format. Please upload a PNG, JPG, or JPEG image."}), 400

    # Save the uploaded file
    filename = f"{uuid.uuid4().hex}.{file.filename.rsplit('.', 1)[1].lower()}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Ensure file is readable
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return jsonify({"error": "Uploaded image is not readable. Please try again."}), 400

    # Predict age
    if model:
        try:
            age = predict_age(file_path)
            if age == "undefined":
                return jsonify({"error": "Failed to detect age. Ensure the image is clear and try again."}), 500
        except Exception as e:
            return jsonify({"error": f"Prediction error: {str(e)}"}), 500
    else:
        return jsonify({"error": "Model not loaded. Please check server logs."}), 500

    return jsonify({"age": age, "image_url": f"/{file_path}"})  # Ensure proper URL format

if __name__ == "__main__":
    app.run(debug=True)