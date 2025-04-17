import streamlit as st
import pandas as pd
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")
st.balloons()

# Initialize session state for navigation
col1, col2 = st.columns([1,1])
with col1:
    st.title("Experience Seamless Code Translation with NeuroCode")

with col2:
    st.image("img1.png")

col3, col4, col5 = st.columns([1,1,1])
with col3:
     st.image("img1.png")

with col4:
     st.image("img1.png")
    
with col5:
     st.image("img1.png")

    

