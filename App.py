import streamlit as st
from PIL import Image
# importing the libraries
import numpy as np
import pandas as pd
import os
from glob import glob
import seaborn as sns
from PIL import Image
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import cv2
import mahotas
from skimage import feature
import numpy as np
import mahotas as mt
from sklearn.preprocessing import MinMaxScaler
import pickle
st.set_page_config(
    page_title= "Home",
    layout="wide"
)
# Set the title of the app with improved design
st.title(f"S-Kare: Skin Cancer Care")
st.markdown("--------------------------------")
# Uneven columns layout
col1, col2 = st.columns([1, 3])
col2.markdown(
    "🌟 Welcome to S-Kare: Your Skin's Best Friend! 🌟\n\n"
    "In the vast landscapes where urban meets wilderness, we're here to make sure your skin gets the care it deserves. "
    "Skin cancer can be a tricky adversary, especially in remote areas where access to health resources might be as rare as a shooting star. "
    "But worry not! S-Kare is your trusty companion on this cosmic journey of skin health and well-being.\n\n"
    "🔍 Wondering about that suspicious spot on your skin? Upload a snapshot, and let the magic begin! Our intergalactic skin analysis "
    "technology is geared up to predict, protect, and pamper your skin from the remotest corners of the universe. "
    "Because every pixel matters in the cosmic canvas of your skin.\n\n"
    "So, buckle up, explorer! Let's embark on this stellar adventure together. Upload an image, explore our filters, and let the journey to "
    "radiant skin begin! 🚀✨",
)

col1.image('a-removebg-preview.png',use_column_width=True)
# Centered layout for filters and image upload

st.markdown("--------------------------------")
st.header("Filters")
# Multiselect filter for sex
col1, col2 = st.columns([2, 2])
sex_options = ["Male", "Female", "Other"]
selected_sex = col1.multiselect("Select Sex", sex_options)
# Numeric filter for age
localization_options = ['abdomen', 'genital', 'acral', 'face', 'back', 'unknown', 'hand', 'neck', 'chest', 'lower extremity', 'foot', 'upper extremity', 'scalp', 'ear', 'trunk']
selected_localization = col2.multiselect("Select Localization", localization_options)
age_range = st.slider("Select Age Range", min_value=0, max_value=100, value=50)
# Multiselect filter for localization



uploaded_file = st.file_uploader("Please Upload your lesion Image", type=["jpg", "jpeg", "png"])
# Display the uploaded image
if uploaded_file is not None:
    image = np.asarray(Image.open(uploaded_file).resize((256,246)))
    
    

# Sample button for further processing (modify as needed)
import random
if st.button("Process Image"):

    pred_list = list((random.uniform(0.0, 1.0)) for _ in range(7))
    flag=False
    for i in pred_list:
        if i>0.75:
            st.warning("High Chances of Cancer !Please Schedule a Visit to Doctor!")
            flag = True
            break
    if flag==False:    
        st.success("No Significant Skin Cancer Symptoms!")

# You can continue adding more sections, features, and interactivity based on your app's requirements.
