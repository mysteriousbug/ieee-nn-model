import streamlit as st
import pandas as pd
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")
st.balloons()

# Initialize session state for navigation
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "Introduction"

st.title("Experience Seamless Code Translation with NeuroCode")

st.markdown("""
### Authors:
**Amrutha Muralidhar, Ananya Aithal, G Sanjana Hebbar, Kavitha Sooda**  
Department of Computer Science and Engineering, B.M.S. College of Engineering, Bangalore, India
""")

st.markdown("### Abstract")
st.markdown("""
This work evaluates the performance of three neural network models—**TransCoder**, **CodeT5**, and **CodeBERT**—for cross-language code synthesis and translation. Using the **CodeXGlue** dataset, we assess these models based on two key metrics: **Code Similarity Score (CSS)** and **Overall Execution Score (OES)**.
""")
    

