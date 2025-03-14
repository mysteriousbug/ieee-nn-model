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
