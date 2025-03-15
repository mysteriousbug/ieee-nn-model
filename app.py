import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Initialize session state for navigation
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "Introduction"

# Sidebar navigation with buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Introduction"):
    st.session_state.selected_section = "Introduction"
if st.sidebar.button("Results"):
    st.session_state.selected_section = "Results"
if st.sidebar.button("Python to Java Translation"):
    st.session_state.selected_section = "Python to Java Translation"

# Display content based on the selected section
st.title("Neural Network Models for Cross-Language Code Synthesis and Translation")

if st.session_state.selected_section == "Introduction":
    st.markdown("""
    ### Authors:
    **Amrutha Muralidhar, Ananya Aithal, G Sanjana Hebbar, Kavitha Sooda**  
    Department of Computer Science and Engineering, B.M.S. College of Engineering, Bangalore, India
    """)
    
    st.markdown("### Abstract")
    st.markdown("""
    This work evaluates the performance of three neural network models—**TransCoder**, **CodeT5**, and **CodeBERT**—for cross-language code synthesis and translation. Using the **CodeXGlue** dataset, we assess these models based on two key metrics: **Code Similarity Score (CSS)** and **Overall Execution Score (OES)**.
    """)

elif st.session_state.selected_section == "Results":
    st.subheader("Results: Model Performance")
    st.markdown("""
    - **CodeT5** achieves the highest translation accuracy.
    - **TransCoder** struggles with semantic errors.
    - **CodeBERT** performs reasonably well but faces challenges in complex control flow translations.
    """)

elif st.session_state.selected_section == "Python to Java Translation":
    st.subheader("Python to Java Code Translation")

    # Python Code
    python_code = """
import concurrent.futures

data = {'a': 10, 'b': 5}

def add():
    return data['a'] + data['b']

def subtract():
    return data['a'] - data['b']

def multiply():
    return data['a'] * data['b']

def divide():
    return data['a'] / data['b'] if data['b'] != 0 else "Division by zero"

operations = {
    'Addition': add,
    'Subtraction': subtract,
    'Multiplication': multiply,
    'Division': divide
}

results = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_operation = {executor.submit(func): name for name, func in operations.items()}
    for future in concurrent.futures.as_completed(future_to_operation):
        results[future_to_operation[future]] = future.result()

print(results)
"""
    st.code(python_code, language="python")

    # Translated Java Code
    translated_java_code = """
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(4);
        int a = 10, b = 5;

        Future<Integer> add = executor.submit(() -> a + b);
        Future<Integer> subtract = executor.submit(() -> a - b);
        Future<Integer> multiply = executor.submit(() -> a * b);
        Future<Integer> divide = executor.submit(() -> b != 0 ? a / b : null);

        System.out.println("Results: " + add.get() + " " + subtract.get() + " " + multiply.get() + " " + (divide.get() != null ? divide.get() : "Division by zero"));
        executor.shutdown();
    }
}
"""
    st.code(translated_java_code, language="java")
