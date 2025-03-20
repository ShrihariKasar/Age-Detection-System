import numpy as np
import cv2
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("age_detection_model.h5")

# Define Age Buckets (Same as training)
AGE_BUCKETS = AGE_BUCKETS = ["18-24", "25-40", "41-60"]  # Updated categories

# Function to predict age from an image
def predict_age(image_path):
    IMG_SIZE = (128, 128)

    # Load and preprocess image
    img = cv2.imread(image_path)
    img = cv2.resize(img, IMG_SIZE)
    img = img / 255.0  # Normalize pixels
    img = np.expand_dims(img, axis=0)  # Add batch dimension

    # Predict
    prediction = model.predict(img)
    age_category = AGE_BUCKETS[np.argmax(prediction)]

    print(f"Predicted Age Group: {age_category}")

# Test on a new image
predict_age("datasets/test/29.jpg")