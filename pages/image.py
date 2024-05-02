import streamlit as st
import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
from fun import *

st.set_page_config('Craiglist Image Detector',page_icon='🕵️‍♀️')

# st.set
css = """background: rgb(2,0,36);
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%); color:white"""

add_gradient_background(css)


# Streamlit UI
st.title("Craigslist Image Reverse Search")

# User inputs
craigslist_url = st.text_input("Enter Craigslist URL:")
shared_image_url = st.text_input("Enter Shared Image URL:")

# Button to initiate search
if st.button("Search"):
    # Download the shared image
    download_image(shared_image_url, "shared_image.jpg")
    
    # Fetch Craigslist page
    response = requests.get(craigslist_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract listings from Craigslist
    listings = soup.find_all(class_="result-row")

    # Loop through listings
    for listing in listings:
        # Extract image URL from listing
        image_tag = listing.find("img")
        if image_tag:
            listing_image_url = image_tag['src']
            # Download the listing image
            download_image(listing_image_url, "temp_image.jpg")
            # Load the images for comparison
            shared_image = cv2.imread("shared_image.jpg")
            listing_image = cv2.imread("temp_image.jpg")
            # Compare images
            similarity = compare_images(shared_image, listing_image)
            # Define a threshold for similarity
            threshold = 0.8
            if similarity > threshold:
                st.write("Match found in listing:", listing)

    # Clean up temporary image file
    import os
    os.remove("temp_image.jpg")
