import os
import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Paths
DATASET_PATH = "datasets/train"  # Folder where images are stored
CSV_FILE = "datasets/train.csv"  # Path to your CSV file

# Check if CSV file exists
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"Error: CSV file '{CSV_FILE}' not found!")

# Load Dataset (Assuming CSV format)
df = pd.read_csv(CSV_FILE)

# Image Size
IMG_SIZE = (128, 128)

# Prepare Data
X = []
y = []

missing_images = 0  # Counter for missing images

for index, row in df.iterrows():
    img_name = str(row['ID']).strip()  # Ensure it's a string
    label = row['Class']  # Age group (e.g., "18-24")

    # Full image path
    img_path = os.path.join(DATASET_PATH, img_name)

    # Check if image exists
    if os.path.exists(img_path):
        img = cv2.imread(img_path)
        img = cv2.resize(img, IMG_SIZE)  # Resize to 128x128
        img = img / 255.0  # Normalize pixels
        X.append(img)
        y.append(label)
    else:
        print(f"⚠ Warning: Missing image {img_path}")
        missing_images += 1

# Print missing image count
print(f"Total missing images: {missing_images}")

# Convert lists to NumPy arrays
X = np.array(X)

# Convert labels (age groups) into categorical format
AGE_BUCKETS = AGE_BUCKETS = ["18-24", "25-40", "41-60"]  # Updated age categories
y = np.array([AGE_BUCKETS.index(age) for age in y])  # Convert to numeric labels
y = to_categorical(y, num_classes=len(AGE_BUCKETS))  # One-hot encoding

# Split dataset into training and validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"✅ Total Images: {len(X)}, Training: {len(X_train)}, Validation: {len(X_val)}")

# ✅ Save Preprocessed Data for CNN
np.save("X_train.npy", X_train)
np.save("y_train.npy", y_train)
np.save("X_val.npy", X_val)
np.save("y_val.npy", y_val)

print("✅ Preprocessed data saved as .npy files!")

# Data Augmentation (For Training Set)
datagen = ImageDataGenerator(
    rotation_range=20, 
    width_shift_range=0.2, 
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

train_generator = datagen.flow(X_train, y_train, batch_size=32)

# Validation Data (Without Augmentation)
val_generator = ImageDataGenerator().flow(X_val, y_val, batch_size=32)

print("✅ Data augmentation applied to training set!")