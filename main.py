import streamlit as st
from fun import *


st.set_page_config('Craiglist Listing Detector',page_icon='🕵️‍♀️')

# st.set
css = """background: rgb(2,0,36);
<<<<<<< Updated upstream
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%); color:white"""
=======
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);color:yellow"""
>>>>>>> Stashed changes
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
        # st.write(listing)
        out = " ".join([i for i in listing.splitlines() if i and ("QR Code" not in i)])
        st.markdown(f"""<p style=color:red;background-color:black;padding:5px>
                    {out}
                    </p>
                    """,unsafe_allow_html=True)
    except Exception as e:
        st.write(f'Not a valid URL {e}')
else:
    webp_bytes = open('smiley_else_url.png', 'rb').read()
    st.image(webp_bytes)
    
c1,c2 = st.columns(2)

with c1:
<<<<<<< Updated upstream
    st.markdown(f"""<p style=bottom-margin:-30px;color:white>Genuine/Fake</p>""",unsafe_allow_html=True)
    api = st.text_input('Enter Open AI API Key')
=======
    st.markdown(f"""<p style=margin-bottom:-100px;>Enter Open AI API Key</p>""",unsafe_allow_html=True)
    api = st.text_input(' ')
>>>>>>> Stashed changes
    if api:
        # logic for model
        with c2:
            ans = llm(api,listing)
            st.write(ans)
    else:
        # 
        with c2:
            
            st.write('Waiting for the API Key,')
            # st.write('Fake')