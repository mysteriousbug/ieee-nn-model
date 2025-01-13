import streamlit as st

# Title and Introduction
st.title("Cross-Language Code Translation Models")
st.markdown("""
This app evaluates the performance of three neural network models for cross-language code translation: 
**TransCoder**, **CodeT5**, and **CodeBERT**. Select a model and a metric to view its performance.
""")

# Dropdown for selecting a model
model = st.selectbox(
    "Choose a model:",
    ["TransCoder", "CodeT5", "CodeBERT"]
)

# Dropdown for selecting a metric
if model:
    metric = st.selectbox(
        f"Select a metric for {model}:",
        ["Code Similarity Score (CSS)", "Overall Execution Score (OES)"]
    )
    
    # Display results based on the selected model and metric
    if metric == "Code Similarity Score (CSS)":
        st.subheader(f"Code Similarity Score (CSS) for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Python → Java: **85.2**
            - JavaScript → C++: **82.0**
            """)
        elif model == "CodeT5":
            st.write("""
            - Python → Java: **83.0**
            - JavaScript → C++: **79.8**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Python → Java: **76.5**
            - JavaScript → C++: **73.8**
            """)

    elif metric == "Overall Execution Score (OES)":
        st.subheader(f"Overall Execution Score (OES) for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Error Rate: **4.2%**
            - Execution Time: **
