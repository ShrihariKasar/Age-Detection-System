import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load Model
model = tf.keras.models.load_model("age_detection_model.h5")

# Load Preprocessed Data
X_val = np.load("X_val.npy")
y_val = np.load("y_val.npy")

# Evaluate Model
loss, accuracy = model.evaluate(X_val, y_val, verbose=1)

print(f"Validation Accuracy: {accuracy * 100:.2f}%")

# Plot Validation Accuracy (Pie Chart)
labels = ["Correct Predictions", "Incorrect Predictions"]
sizes = [accuracy * 100, 100 - (accuracy * 100)]
colors = ['green', 'red']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title("Model Validation Accuracy Distribution")
plt.show()