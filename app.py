import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import cv2

# --- PAGE CONFIG ---
st.set_page_config(page_title="SustaLens AI", page_icon="🌿")

@st.cache_resource
def load_susta_model():
    return load_model("SustaLens_Model.h5")

model = load_susta_model()

# --- CUSTOM UI ---
st.markdown("""
    <style>
    .stButton button { background-color: #2ECC71; color: white; width: 100%; font-weight: bold; }
    .header { color: #1E3C72; text-align: center; font-size: 40px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header">🌿 SustaLens AI</div>', unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Responsible Waste Classification (SDG 12)</p>", unsafe_allow_html=True)

# --- LOGIC ---
def predict_waste(image):
    # Ensure image is RGB (to avoid errors with PNG transparency)
    img = image.convert("RGB")
    img = img.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0][0]
    
    if prediction > 0.5:
        return "INORGANIC", prediction * 100, (0, 0, 255)
    else:
        return "ORGANIC", (1 - prediction) * 100, (0, 255, 0)

# --- UI BODY ---
option = st.sidebar.radio("Input:", ["📸 Camera", "📤 Upload"])
image = None

if option == "📸 Camera":
    cap = st.camera_input("Scan waste")
    if cap: image = Image.open(cap)
else:
    file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"])
    if file: image = Image.open(file)

if image:
    st.image(image, use_container_width=True)
    if st.button("CLASSIFY"):
        label, conf, color = predict_waste(image)
        if label == "ORGANIC":
            st.success(f"Result: {label} ({conf:.1f}%)")
        else:
            st.error(f"Result: {label} ({conf:.1f}%)")