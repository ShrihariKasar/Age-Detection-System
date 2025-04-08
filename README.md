# 🧑‍⚕️ Age Detection Using CNN

This project is a **deep learning-based age detection system** built using **TensorFlow, Flask, and OpenCV**. The model classifies facial images into one of the following age groups:

- **18–24**
- **25–40**
- **41–60**

🚀 **Live Demo On Linkedin:** [https://www.linkedin.com/posts/shrihari-kasar-94b63525b_ai-machinelearning-deeplearning-activity-7296490945733083136-hl2T?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD_80gsBostlEkM0_BVA-Oo7hiAWBcss-FQ]

---

## 📜 Project Overview

This project takes a facial image as input and predicts the corresponding age group using a **Convolutional Neural Network (CNN)** model trained on a labeled dataset. It integrates a **Flask-based web application** to provide a user-friendly interface.

### ✅ Key Features

- Deep learning-based prediction using CNN  
- Web app interface built with Flask  
- Image preprocessing using OpenCV  
- Data augmentation to improve generalization  

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Machine Learning:** TensorFlow, Keras, OpenCV  
- **Data Handling:** NumPy, Pandas  

---

## 📂 Project Structure

```
📦 age-detection
├── 📁 static/             # Uploaded images and static assets  
├── 📁 templates/          # HTML templates (UI pages)  
├── 📁 datasets/           # Dataset folder with images & metadata  
├── 📜 app.py              # Flask backend for the web app  
├── 📜 model_training.py   # CNN model training script  
├── 📜 requirements.txt    # List of required packages  
└── 📜 README.md           # Project documentation  
```

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShrihariKasar/age-detection.git
cd age-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

Then open your browser and go to:  
🌐 `http://127.0.0.1:5000/`

---

## 📊 Model Training

To retrain the CNN model:

```bash
python model_training.py
```

- The trained model will be saved as: `age_detection_model.h5`
- You can adjust training parameters in `model_training.py` as needed

---

## 📷 How to Use

1. Upload a facial image (JPG, PNG, JPEG)  
2. Click on the **"Predict"** button  
3. View the predicted **age group** instantly  

---

## 🎨 User Interface Overview

The web interface is clean, minimal, and responsive. It allows users to upload an image and get results with ease.

### UI Preview

![Home Page](https://github.com/ShrihariKasar/Age-Detection-System/blob/main/age_d.png)

---

## 🧩 UI Components

| Feature               | Description                               |
|------------------------|-------------------------------------------|
| **Upload Section**     | Upload an image for age detection         |
| **Predict Button**     | Generates prediction on click             |
| **Result Display**     | Shows predicted age category              |
| **Responsive Layout**  | Works across mobile and desktop devices   |

---

## 🎬 How It Works

1. **Upload an image**  
2. **Click on “Predict Age”**  
3. **Model outputs the predicted age group**

---

## 📈 Results & Accuracy

- **Training Accuracy:** ~78%  
- **Validation Accuracy:** ~78.13%  
- Accuracy may increase with a larger and more diverse dataset

---

## 💡 Future Enhancements

- Better styled and animated UI  
- Full mobile responsiveness  
- Voice input and audio prediction feedback  
- Model optimization for faster prediction  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a branch (`feature-new`)  
3. Commit your changes  
4. Open a Pull Request  

---

## 📜 License

This project is licensed under the **MIT License**

---

## 📧 Contact & Credits

**👤 Shrihari Kasar**  
🔗 [GitHub Profile](https://github.com/ShrihariKasar)  

If you have any questions or suggestions, feel free to reach out!

---

⭐ If you found this project useful, please **star the repository** and share it!
```
