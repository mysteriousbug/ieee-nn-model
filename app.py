import streamlit as st

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
            - Execution Time: **1.8s**
            - Memory Usage: **450 MB**
            - **OES: 82.4**
            """)
        elif model == "CodeT5":
            st.write("""
            - Error Rate: **5.1%**
            - Execution Time: **2.0s**
            - Memory Usage: **480 MB**
            - **OES: 78.9**
            """)
        elif model == "CodeBERT":
            st.write("""
            - Error Rate: **6.3%**
            - Execution Time: **2.4s**
            - Memory Usage: **500 MB**
            - **OES: 72.5**
            """)

# Hardcoded Python multithreading function
python_code = """
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
"""

# Hardcoded translated Java code with errors
translated_java_code = {
    "TransCoder": """
import java.lang.Thread;

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println(i);
            }
        });
        thread.start();
        thread.join(); // Error: join needs try-catch
    }
}
""",
    "CodeT5": """
import java.util.concurrent;

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println(i);
            }
        });
        thread.start();
        thread.join(); // Error: join needs try-catch
    }
}
""",
    "CodeBERT": """
import java.lang.Thread;

class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println(i);
                }
            }
        });
        thread.start();
        thread.join(); // Error: Missing try-catch
    }
}
"""
}

# Corrected Java Code
corrected_java_code = """
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println(i);
            }
        });
        thread.start();
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
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
