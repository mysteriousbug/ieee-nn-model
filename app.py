import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Sidebar for navigation (Top-right alternative)
st.sidebar.title("Navigation")
tab = st.sidebar.radio("Go to:", ["Python Code", "Translated Java Code", "Corrected Java Code"])

# Display content based on the selected tab
if tab == "Python Code":
    st.subheader("Input Code (Python)")
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
    st.code(python_code, language="python")

elif tab == "Translated Java Code":
    st.subheader("Translated Java Code")
    translated_java_code = """
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;

        for (int num : numbers) {
            sum += num;
        }

        System.out.println("Sum: " + sum);

        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(() -> System.out.println("Addition"));
        executor.submit(() -> System.out.println("Subtraction"));
        executor.shutdown();
    }
}
"""
    st.code(translated_java_code, language="java")

elif tab == "Corrected Java Code":
    st.subheader("Corrected Java Code")
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
    st.code(corrected_java_code, language="java")
