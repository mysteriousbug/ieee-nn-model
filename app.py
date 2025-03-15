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
        Future<Integer> divide = executor.submit(() -> data.get("b") != 0 ? data.get("a") / data.get("b") : null);

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
        Future<Integer> divide = executor.submit(() -> a / b);

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

# Hardcoded Java multithreading function
java_code = """
import java.util.*;
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        Map<String, Integer> data = new HashMap<>();
        data.put("A", 10);
        data.put("B", 20);
        data.put("C", 30);

        List<Future<Integer>> results = new ArrayList<>();
        for (String key : data.keySet()) {
            results.add(executor.submit(() -> data.get(key) * 2));
        }

        try {
            for (Future<Integer> result : results) {
                System.out.println(result.get());
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }

        executor.shutdown();
    }
}
"""

# Hardcoded translated C++ code with errors
translated_cpp_code = {
    "TransCoder": """
#include <iostream>
#include <thread>
#include <future>
#include <unordered_map>
using namespace std;

int compute(int value) {
    return value * 2;
}

int main() {
    unordered_map<string, int> data = { {"A", 10}, {"B", 20}, {"C", 30} };
    vector<future<int>> results;

    for (auto pair : data) {
        results.push_back(async(launch::async, compute, pair.second));
    }

    for (auto& result : results) {
        cout << result.get() << endl;
    }

    return 0;
}
""",  # Missing proper thread management and incorrect use of string keys in unordered_map

    "CodeT5": """
#include <iostream>
#include <map>
#include <future>
using namespace std;

int multiply(int x) { return x * 2; }

int main() {
    map<string, int> data = { {"A", 10}, {"B", 20}, {"C", 30} };
    vector<future<int>> results;

    for (auto &[key, value] : data) {
        results.push_back(async(launch::async, multiply, value));
    }

    for (auto &result : results) {
        cout << result.get() << endl;
    }

    return 0;
}
""",  # Minor issues with unnecessary use of map instead of unordered_map

    "CodeBERT": """
#include <iostream>
#include <unordered_map>
#include <future>
#include <vector>
using namespace std;

int doubleValue(int val) { return val * 2; }

int main() {
    unordered_map<string, int> data = { {"A", 10}, {"B", 20}, {"C", 30} };
    vector<future<int>> results;

    for (const auto &entry : data) {
        results.push_back(async(launch::async, doubleValue, entry.second));
    }

    for (auto &res : results) {
        cout << res.get() << endl;
    }

    return 0;
}
"""  # Uses better syntax but lacks exception handling
}

# Corrected C++ Code
corrected_cpp_code = """
#include <iostream>
#include <unordered_map>
#include <future>
#include <vector>
using namespace std;

int doubleValue(int val) { return val * 2; }

int main() {
    unordered_map<string, int> data = { {"A", 10}, {"B", 20}, {"C", 30} };
    vector<future<int>> results;

    for (const auto &entry : data) {
        results.push_back(async(launch::async, doubleValue, entry.second));
    }

    try {
        for (auto &res : results) {
            cout << res.get() << endl;
        }
    } catch (const exception &e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}
"""

# Display in three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Input Code (Java)")
    st.code(java_code, language="java")

with col2:
    st.subheader(f"Translated C++ Code ({model})")
    st.code(translated_cpp_code[model], language="cpp")

with col3:
    st.subheader("Corrected C++ Code")
    st.code(corrected_cpp_code, language="cpp")
