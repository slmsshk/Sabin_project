import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_description = soup.find('section', id='postingbody').get_text().strip()
    return job_description


def add_gradient_background(css):
    """
    Add a gradient background to the Streamlit app.

    Parameters:
        css (str): The CSS code defining the gradient background.

    Example:
        add_gradient_background("background: rgb(2,0,36);background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);")
    """
    # Generate CSS code for gradient background
    gradient_bg_css = f"""
    <style>
    .stApp {{
        {css}
    }}
    </style>
    """

    # Display the CSS code
    st.markdown(gradient_bg_css, unsafe_allow_html=True)