# 🌿 SustaLens AI 
**Responsible Consumption and Production (SDG 12)**

SustaLens AI is a Deep Learning-based waste classifier designed to promote sustainable waste management. Using a Convolutional Neural Network (CNN), the application identifies whether waste is **Organic** or **Inorganic**, helping users segregate trash effectively at the source.

## 🚀 Live Demo
Check out the live application here: [sustalens-ai.streamlit.app](https://sustalens-ai.streamlit.app)

## 📌 Problem Statement
Improper waste segregation is a leading cause of environmental pollution. According to **UN Sustainable Development Goal 12**, sustainable consumption and production patterns are essential. SustaLens AI simplifies the segregation process for households and industries using real-time image recognition.

## 🛠️ Tech Stack
- **Framework:** Streamlit (Web UI)
- **Deep Learning Library:** TensorFlow / Keras
- **Computer Vision:** OpenCV & PIL
- **Model Architecture:** Convolutional Neural Network (CNN) - MobileNetV2 / Custom Build
- **Deployment:** GitHub & Streamlit Cloud (LFS for Model Hosting)

## 📂 Project Structure
```text
├── SustaLens_Model.h5    # The trained CNN model (134MB via Git LFS)
├── app.py                # Streamlit Web Application logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation