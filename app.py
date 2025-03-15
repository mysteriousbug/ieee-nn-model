import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Define three tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Model Evaluation", "Code Comparison"])

# ---------- TAB 1: Overview ----------
with tab1:
    st.title("Neural Network Models for Cross-Language Code Synthesis and Translation")
    st.markdown("""
    ### Authors:
    **Amrutha Muralidhar,  Ananya Aithal,  G Sanjana Hebbar,  Kavitha Sooda**\n
    Department of Computer Science and Engineering, B.M.S. College of Engineering, Bangalore, India
    """)
    
    # Abstract
    st.markdown("### Abstract")
    st.markdown("""
    This work evaluates the performance of three neural network models—**TransCoder**, **CodeT5**, and **CodeBERT**—for cross-language code synthesis and translation. Using the **CodeXGlue** dataset, we assess these models based on two key metrics: **Code Similarity Score (CSS)** and **Overall Execution Score (OES)**. Our findings indicate that **CodeT5** achieves the highest translation accuracy, while **TransCoder** struggles with semantic errors. **CodeBERT** performs reasonably well but faces challenges in complex control flow translations. These insights can guide the development of improved code translation models for software engineering and programming education.
    """)

# ---------- TAB 2: Model Evaluation ----------
with tab2:
    st.header("Model Evaluation")

    # Dropdown for selecting a model
    model = st.selectbox("Choose a model:", ["TransCoder", "CodeT5", "CodeBERT"])

    # Dropdown for selecting a dataset
    dataset = st.selectbox("Choose a dataset:", ["CodeXGlue", "CodeSearchNet", "Conala"])

    # Dropdown for selecting a metric
    if model:
        metric = st.selectbox(f"Select a metric for {model}:", 
                              ["Code Similarity Score (CSS)", "Overall Execution Score (OES)", 
                               "Precision", "Recall", "Exact Match"])

        # Display results based on the selected model and metric
        if metric == "Code Similarity Score (CSS)":
            st.subheader(f"Code Similarity Score (CSS) for {model}")
            scores = {"TransCoder": "24.2", "CodeT5": "65.0", "CodeBERT": "60.5"}
            st.write(f"- Python → Java: **{scores[model]}**")

        elif metric == "Overall Execution Score (OES)":
            st.subheader(f"Overall Execution Score (OES) for {model}")
            scores = {"TransCoder": "65.4", "CodeT5": "72.4", "CodeBERT": "68.6"}
            st.write(f"- **OES: {scores[model]}**")

        elif metric == "Precision":
            st.subheader(f"Precision for {model}")
            precision_scores = {
                "TransCoder": "Python → Java: **29.7**  |  Java → C++: **75.4**",
                "CodeT5": "Python → Java: **70.1**  |  Java → C++: **71.5**",
                "CodeBERT": "Python → Java: **60.6**  |  Java → C++: **63.4**"
            }
            st.write(precision_scores[model])

        elif metric == "Recall":
            st.subheader(f"Recall for {model}")
            recall_scores = {
                "TransCoder": "Python → Java: **27.5**  |  Java → C++: **73.1**",
                "CodeT5": "Python → Java: **70.8**  |  Java → C++: **69.5**",
                "CodeBERT": "Python → Java: **58.3**  |  Java → C++: **65.8**"
            }
            st.write(recall_scores[model])

        elif metric == "Exact Match":
            st.subheader(f"Exact Match for {model}")
            exact_match_scores = {
                "TransCoder": "Python → Java: **18.3**  |  Java → C++: **22.6**",
                "CodeT5": "Python → Java: **63.2**  |  Java → C++: **64.4**",
                "CodeBERT": "Python → Java: **53.1**  |  Java → C++: **55.4**"
            }
            st.write(exact_match_scores[model])

# ---------- TAB 3: Code Comparison ----------
with tab3:
    st.header("Code Comparison")

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

    # Execute operations in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {op: executor.submit(func).result() for op, func in 
                   {'Addition': add, 'Subtraction': subtract, 'Multiplication': multiply, 'Division': divide}.items()}

    print(results)
    """

    # Hardcoded translated Java code
    translated_java_code = {
        "TransCoder": """ 
        // TransCoder output (Incorrect Syntax)
        import java.util.concurrent.*;

        public class Main {
            public static void main(String[] args) {
                ExecutorService executor = Executors.newFixedThreadPool(2);
                executor.submit(() -> System.out.println("Addition"));
                executor.shutdown();
            }
        }
        """,
        "CodeT5": """
        // CodeT5 output
        import java.util.*;

        public class Main {
            public static void main(String[] args) {
                int x = 10, y = 5;
                System.out.println("Sum: " + (x + y));
            }
        }
        """,
        "CodeBERT": """
        // CodeBERT output (Syntax error in elif)
        import java.util.*;

        public class Main {
            public static void main(String[] args) {
                int x = 10, y = 5;
                if (x > y) {
                    System.out.println("x is greater than y");
                } elif (x == y) {
                    System.out.println("x is equal to y");
                } else {
                    System.out.println("x is less than y");
                }
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
