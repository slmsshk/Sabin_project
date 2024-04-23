import streamlit as st
from fun import *


# st.set
css = """background: rgb(2,0,36);
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);"""
add_gradient_background(css)

st.markdown(f"""
            <h1 style = color:green;text-align:center> Craig List Listing Detector </h1>
            """,unsafe_allow_html=True)

# st.markdown(f"""
#             <p style = color:white;text-align:center> Enter a valid craiglist url</p>
#             """,unsafe_allow_html=True)

url = st.text_input('Enter a valid craiglist url')

if url:
    try:
        listing = scrape_job_description(url)
        st.write(listing)
    except Exception as e:
        st.write(f'Not a valid URL {e}')
else:
    webp_bytes = open('smiley_else_url.png', 'rb').read()
    st.image(webp_bytes, caption='Add Url')

c1,c2 = st.columns(2)

with c1:
    but = st.button('balloon 🎈')

    if but :
        st.balloons()
with c2:    
    if st.button('make it snow❄'):
        st.snow()

 