import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def scrape_job_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_description = soup.find('section', id='postingbody').get_text().strip()
    return job_description

def llm(api,listing):

    client = OpenAI(api_key=api)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """
You are a Craigslist Listing Classifier. Your task is to evaluate whether a given listing description is Genuine or Fake, considering the types of listings typically found on Craigslist and the common characteristics of fraudulent listings.

Genuine listings on Craigslist often provide detailed and accurate information about the property or item being advertised. They may include specific features, amenities, and location details, and are written in a professional and descriptive manner.

Fraudulent listings, on the other hand, may exhibit one or more of the following characteristics:
- Unrealistic promises or claims, such as extremely low prices or guaranteed returns.
- Lack of specific details or amenities, making the listing vague or generic.
- High-pressure sales tactics, such as urgency or limited availability, designed to pressure potential buyers or renters.
- Use of generic language or clichés commonly associated with sales pitches.
- Inconsistent or contradictory information within the description.

Your job is to analyze the provided listing description and determine whether it is likely to be genuine or fake. If the listing is fake or genuine return that and provide a brief explanation outlining the reasons for your classification.
"""},
        {"role": "user", "content": listing}
    
    ]
    )

    return completion.choices[0].message.content


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