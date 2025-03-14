import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Title and Introduction
st.title("Cross-Language Code Translation Models")
st.markdown("""
This app evaluates the performance of three neural network models for cross-language code translation:
**TransCoder**, **CodeT5**, and **CodeBERT**. Select a model to view its translated Java output.
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
        ["Code Similarity Score (CSS)", "Overall Execution Score (OES)", "Precision", "Recall", "Exact Match"]
    )
    
    # Display results based on the selected model and metric
    if metric == "Code Similarity Score (CSS)":
        st.subheader(f"Code Similarity Score (CSS) for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Python → Java: **24.2**
            - Java → C++: **61.0**
            """)
        elif model == "CodeT5":
            st.write("""
            - Python → Java: **65.0**
            - Java → C++: **69.8**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Python → Java: **60.5**
            - Java → C++: **62.8**
            """)

    elif metric == "Overall Execution Score (OES)":
        st.subheader(f"Overall Execution Score (OES) for {model}")
        
        if model == "TransCoder":
           st.write("""
            - **OES: 65.4**
            """)
        elif model == "CodeT5":
            st.write("""
            - **OES: 72.4**
            """)
        elif model == "CodeBERT":
            st.write("""
            - **OES: 68.6**
            """)

    elif metric == "Precision":
        st.subheader(f"Precision for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Python → Java: **29.7**
            - Java → C++: **75.4**
            """)
        elif model == "CodeT5":
            st.write("""
            - Python → Java: **70.1**
            - Java → C++: **71.5**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Python → Java: **60.6**
            - Java → C++: **63.4**
            """)

    elif metric == "Recall":
        st.subheader(f"Recall for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Python → Java: **27.5**
            - Java → C++: **73.1**
            """)
        elif model == "CodeT5":
            st.write("""
            - Python → Java: **70.8**
            - Java → C++: **69.5**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Python → Java: **58.3**
            - Java → C++: **65.8**
            """)

   elif metric == "Exact Match":
        st.subheader(f"Exact Match for {model}")
        
        if model == "TransCoder":
            st.write("""
            - Python → Java: **18.3**
            - Java → C++: **22.6**
            """)
        elif model == "CodeT5":
            st.write("""
            - Python → Java: **63.2**
            - Java → C++: **64.4**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Python → Java: **53.1**
            - Java → C++: **55.4**
            """)
    
# Hardcoded Python multithreading function
python_code = """
import concurrent.futures

# Define a dictionary with two numbers
data = {'a': 10, 'b': 5}

# Define arithmetic operations
def add():
    return data['a'] + data['b']

def subtract():
    return data['a'] - data['b']

def multiply():
    return data['a'] * data['b']

def divide():
    return data['a'] / data['b'] if data['b'] != 0 else "Division by zero"

# Function mapping
operations = {
    'Addition': add,
    'Subtraction': subtract,
    'Multiplication': multiply,
    'Division': divide
}

# Execute operations in parallel and store results in a dictionary
results = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_operation = {executor.submit(func): name for name, func in operations.items()}
    for future in concurrent.futures.as_completed(future_to_operation):
        results[future_to_operation[future]] = future.result()

# Print results dictionary
print(results)
"""

# Hardcoded translated Java code with errors
translated_java_code = {
    "TransCoder": """
import java.util.concurrent.*;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> data = new HashMap<>();
        data.put("a", 10);
        data.put("b", 5);

        ExecutorService executor = Executors.newFixedThreadPool(4);
        Future<Integer> add = executor.submit(() -> data.get("a") + data.get("b"));
        Future<Integer> subtract = executor.submit(() -> data.get("a") - data.get("b"));
        Future<Integer> multiply = executor.submit(() -> data.get("a") * data.get("b"));
        Future<Integer> divide = executor.submit(() -> data.get("b") != 0 ? data.get("a") / data.get("b") : null); // Error: Null return type

        System.out.println("Results: " + add.get() + " " + subtract.get() + " " + multiply.get() + " " + divide.get());
        executor.shutdown();
    }
}
""",
    "CodeT5": """
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(4);
        int a = 10, b = 5;

        Future<Integer> add = executor.submit(() -> a + b);
        Future<Integer> subtract = executor.submit(() -> a - b);
        Future<Integer> multiply = executor.submit(() -> a * b);
        Future<Integer> divide = executor.submit(() -> a / b); // Error: No zero check

        System.out.println("Results: " + add.get() + " " + subtract.get() + " " + multiply.get() + " " + divide.get());
        executor.shutdown();
    }
}
"""
}

# Corrected Java Code
corrected_java_code = """
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

# Display in three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Input Code (Python)")
    st.code(python_code, language="python")

with col2:
    st.subheader(f"Translated Java Code ({model})")
    st.code(translated_java_code[model], language="java")

with col3:
    st.subheader("Corrected Java Code")
    st.code(corrected_java_code, language="java")

# Footer
st.markdown("---")
st.markdown("### About")
st.markdown("""
This app is part of a research project evaluating the performance of neural network models in cross-language code translation.
""")
