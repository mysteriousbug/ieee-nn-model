import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Title and Introduction
st.title("Neural Network Models for Cross-Language Code Synthesis and Translation")
st.markdown("""
### Authors:
**Amrutha Muralidhar,  Ananya Aithal,  G Sanjana Hebbar,  Dr. Kavitha Sooda**\n
Department of Computer Science and Engineering, B.M.S. College of Engineering, Bangalore, India
""")

# Abstract
st.markdown("### Abstract")
st.markdown("""
This work evaluates the performance of three neural network models—**TransCoder**, **CodeT5**, and **CodeBERT**—for cross-language code synthesis and translation. Using the **CodeXGlue** dataset, we assess these models based on two key metrics: **Code Similarity Score (CSS)** and **Overall Execution Score (OES)**. Our findings indicate that **CodeT5** achieves the highest translation accuracy, while **TransCoder** struggles with semantic errors. **CodeBERT** performs reasonably well but faces challenges in complex control flow translations. These insights can guide the development of improved code translation models for software engineering and programming education.
""")

# Dropdown for selecting a model
model = st.selectbox(
    "Choose a model:",
    ["TransCoder", "CodeT5", "CodeBERT"]
)

# Dropdown for selecting a dataset
dataset = st.selectbox(
    "Choose a dataset:",
    ["CodeXGlue", "CodeSearchNet", "Conala"]
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

public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;

        for (int num : numbers) {
            sum += num;
        }

        print("Sum: " + sum);

        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(() -> System.out.println("Thread 1"));
        executor.submit(() -> System.out.println("Thread 2"));
        executor.shutdown();
    }

    public static void print(String message) {
        System.out.println(message);
    }
}
""",
    "CodeT5": """
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int x = 10;
        int y = 5;
        int result = 0;

        if (x > y) {
            if (y != 0) {
                if (x % y == 0) {
                    if (x / y > 1) {
                        result = x / y;
                    } else {
                        result = y / x;
                    }
                } else {
                    result = x * y;
                }
            } else {
                result = x + y;
            }
        } else {
            result = x - y;
        }

        System.out.println("Result: " + result);

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    System.out.println(i + " " + j + " " + k);
                }
            }
        }
    }
}
""",
 "CodeBERT": """
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int x = 10;
        int y = 5;

        if (x > y) {
            System.out.println("x is greater than y");
        } elif (x == y) {
            System.out.println("x is equal to y");
        } else {
            System.out.println("x is less than y");
        }

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        numbers.forEach(num -> {
            if (num % 2 == 0) {
                System.out.println(num + " is even");
            } else {
                System.out.println(num + " is odd");
            }
        });

        List<Integer> subList = numbers.subList(1, 3); 
        System.out.println("Sublist: " + subList);
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
