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
    
    
    

# Additional content or analysis can be added based on your specific requirements
# For example, you can include a button for processing the image and providing results.
# feature-descriptor-1: Hu Moments
def fd_hu_moments(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature
# feature-descriptor-2: Haralick Texture
def fd_haralick(image):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the haralick texture feature vector
    haralick = mahotas.features.haralick(gray).mean(axis=0)
    # return the result
    return haralick
# feature-descriptor-3: Color Histogram
def fd_histogram(image, mask=None,bins=256):
    # convert the image to HSV color-space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # compute the color histogram
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    # normalize the histogram
    cv2.normalize(hist, hist)
    # return the histogram
    return hist.flatten()
def get_hog(image, _wind_size=8, _orientations=8):
    
    """generate Histogram of gradients as a feature vector for an given image """
    
    fd, hog_image = hog(image, orientations=_orientations, pixels_per_cell=(_wind_size, _wind_size),
                    cells_per_block=(1, 1), visualize=True, channel_axis=-1, feature_vector=True)
    
    return fd
# Sample button for further processing (modify as needed)
import random
if st.button("Process Image"):
    # Add your processing logic here
    # fv_hu_moments = fd_hu_moments(image)
    # fv_haralick   = fd_haralick(image)
    # fv_histogram  = fd_histogram(image)
    # fv_hog        = get_hog(image)
    ###################################
    # Concatenate global features
    ###################################
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
