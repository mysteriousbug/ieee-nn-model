import streamlit as st

# Set wide layout
st.set_page_config(layout="wide")

# Initialize session state for navigation
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "Introduction"

# Sidebar navigation with buttons
st.sidebar.title("Table of Contents")
if st.sidebar.button("Introduction"):
    st.session_state.selected_section = "Introduction"
if st.sidebar.button("Python to Java Translation"):
    st.session_state.selected_section = "Python to Java Translation"
if st.sidebar.button("Java to C++ Translation"):
    st.session_state.selected_section = "Java to C++ Translation"
if st.sidebar.button("Results"):
    st.session_state.selected_section = "Results"

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

        scores = {
            "Code Similarity Score (CSS)": {"TransCoder": "24.2", "CodeT5": "65.0", "CodeBERT": "60.5"},
            "Overall Execution Score (OES)": {"TransCoder": "65.4", "CodeT5": "72.4", "CodeBERT": "68.6"},
            "Precision": {
                "TransCoder": "Python → Java: **29.7**  |  Java → C++: **75.4**",
                "CodeT5": "Python → Java: **70.1**  |  Java → C++: **71.5**",
                "CodeBERT": "Python → Java: **60.6**  |  Java → C++: **63.4**"
            },
            "Recall": {
                "TransCoder": "Python → Java: **27.5**  |  Java → C++: **73.1**",
                "CodeT5": "Python → Java: **70.8**  |  Java → C++: **69.5**",
                "CodeBERT": "Python → Java: **58.3**  |  Java → C++: **65.8**"
            },
            "Exact Match": {
                "TransCoder": "Python → Java: **18.3**  |  Java → C++: **22.6**",
                "CodeT5": "Python → Java: **63.2**  |  Java → C++: **64.4**",
                "CodeBERT": "Python → Java: **53.1**  |  Java → C++: **55.4**"
            }
        }
        
        st.subheader(f"{metric} for {model}")
        st.write(scores[metric][model])

# Python to Java Translation Section
elif st.session_state.selected_section == "Python to Java Translation":
    st.header("Python to Java Code Translation")
    
    # Dropdown to select the model
    model = st.selectbox("Select a translation model:", ["TransCoder", "CodeT5", "CodeBERT"])
    
    # Hardcoded Python multithreading function
    python_code = """
import threading
import time
import random
from queue import Queue

# Constants
NUM_WORKERS = 5
TASKS_PER_WORKER = 3
TASK_COMPLETION_TIME_RANGE = (1, 5)

# Shared queue for tasks
task_queue = Queue()
# Lock for printing to avoid mixed output
print_lock = threading.Lock()

# Worker function
def worker(worker_id):
    while not task_queue.empty():
        task = task_queue.get()
        if task is None:
            break

        # Simulate task processing time
        processing_time = random.randint(*TASK_COMPLETION_TIME_RANGE)
        with print_lock:
            print(f"Worker {worker_id} is processing task {task} (will take {processing_time} seconds)")
        time.sleep(processing_time)

        with print_lock:
            print(f"Worker {worker_id} completed task {task}")

        task_queue.task_done()

# Manager function
def manager():
    for task_id in range(1, NUM_WORKERS * TASKS_PER_WORKER + 1):
        task_queue.put(task_id)
        with print_lock:
            print(f"Manager assigned task {task_id}")

    # Wait for all tasks to be completed
    task_queue.join()
    with print_lock:
        print("All tasks have been completed.")

    # Signal workers to exit
    for _ in range(NUM_WORKERS):
        task_queue.put(None)

# Main function
def main():
    # Create worker threads
    workers = []
    for worker_id in range(1, NUM_WORKERS + 1):
        worker_thread = threading.Thread(target=worker, args=(worker_id,))
        worker_thread.start()
        workers.append(worker_thread)

    # Create manager thread
    manager_thread = threading.Thread(target=manager)
    manager_thread.start()

    # Wait for all worker threads to finish
    for worker_thread in workers:
        worker_thread.join()

    # Wait for manager thread to finish
    manager_thread.join()

    print("All workers and manager have finished.")

if __name__ == "__main__":
    main()
"""

    translated_java_code = {
        "TransCoder": """
import java.util.concurrent.*;
import java.util.Random;

public class MultiThreadingExample {
    private static final int NUM_WORKERS = 5;
    private static final int TASKS_PER_WORKER = 3;
    private static final int[] TASK_COMPLETION_TIME_RANGE = {1, 5};

    private static BlockingQueue<Integer> taskQueue = new LinkedBlockingQueue<>();
    private static Object printLock = new Object();

    static class Worker implements Runnable {
        private int workerId;

        public Worker(int workerId) {
            this.workerId = workerId;
        }

        @Override
        public void run() {
            while (!taskQueue.isEmpty()) {
                Integer task = taskQueue.poll();
                if (task == null) {
                    break;
                }

                Random rand = new Random();
                int processingTime = rand.nextInt(TASK_COMPLETION_TIME_RANGE[1]) + TASK_COMPLETION_TIME_RANGE[0];

                synchronized (printLock) {
                    System.out.println("Worker " + workerId + " is processing task " + task + " (will take " + processingTime + " seconds)");
                }

                try {
                    Thread.sleep(processingTime * 1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                synchronized (printLock) {
                    System.out.println("Worker " + workerId + " completed task " + task);
                }
            }
        }
    }

    static class Manager implements Runnable {
        @Override
        public void run() {
            for (int taskId = 1; taskId <= NUM_WORKERS * TASKS_PER_WORKER; taskId++) {
                taskQueue.add(taskId);
                synchronized (printLock) {
                    System.out.println("Manager assigned task " + taskId);
                }
            }

            while (!taskQueue.isEmpty()) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            synchronized (printLock) {
                System.out.println("All tasks have been completed.");
            }

            for (int i = 0; i < NUM_WORKERS; i++) {
                taskQueue.add(null);
            }
        }
    }

    public static void main(String[] args) {
        Thread[] workers = new Thread[NUM_WORKERS];
        for (int i = 0; i < NUM_WORKERS; i++) {
            workers[i] = new Thread(new Worker(i + 1));
            workers[i].start();
        }

        Thread managerThread = new Thread(new Manager());
        managerThread.start();

        for (Thread worker : workers) {
            try {
                worker.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        try {
            managerThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("All workers and manager have finished.");
    }
}
""",
        "CodeT5": """
import java.util.concurrent.*;
import java.util.Random;

public class MultiThreadingExample {
    private static final int NUM_WORKERS = 5;
    private static final int TASKS_PER_WORKER = 3;
    private static final int TASK_COMPLETION_TIME_MIN = 1;
    private static final int TASK_COMPLETION_TIME_MAX = 5;

    private static BlockingQueue<Integer> taskQueue = new LinkedBlockingQueue<>();
    private static final Object printLock = new Object();

    static class Worker implements Runnable {
        private int workerId;

        public Worker(int workerId) {
            this.workerId = workerId;
        }

        @Override
        public void run() {
            try {
                while (true) {
                    Integer task = taskQueue.take();
                    if (task == null) {
                        break;
                    }

                    Random rand = new Random();
                    int processingTime = rand.nextInt(TASK_COMPLETION_TIME_MAX - TASK_COMPLETION_TIME_MIN + 1) + TASK_COMPLETION_TIME_MIN;

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " is processing task " + task + " (will take " + processingTime + " seconds)");
                    }

                    Thread.sleep(processingTime * 1000);

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " completed task " + task);
                    }
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    static class Manager implements Runnable {
        @Override
        public void run() {
            try {
                for (int taskId = 1; taskId <= NUM_WORKERS * TASKS_PER_WORKER; taskId++) {
                    taskQueue.put(taskId);
                    synchronized (printLock) {
                        System.out.println("Manager assigned task " + taskId);
                    }
                }

                taskQueue.join(); // Incorrect usage: BlockingQueue doesn't have a join() method

                synchronized (printLock) {
                    System.out.println("All tasks have been completed.");
                }

                for (int i = 0; i < NUM_WORKERS; i++) {
                    taskQueue.put(null); // Signal workers to exit
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Thread[] workers = new Thread[NUM_WORKERS];
        for (int i = 0; i < NUM_WORKERS; i++) {
            workers[i] = new Thread(new Worker(i + 1));
            workers[i].start();
        }

        Thread managerThread = new Thread(new Manager());
        managerThread.start();

        for (Thread worker : workers) {
            try {
                worker.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        try {
            managerThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("All workers and manager have finished.");
    }
}
""",
        "CodeBERT": """
import java.util.concurrent.*;
import java.util.Random;

public class MultiThreadingExample {
    private static final int NUM_WORKERS = 5;
    private static final int TASKS_PER_WORKER = 3;
    private static final int TASK_COMPLETION_TIME_MIN = 1;
    private static final int TASK_COMPLETION_TIME_MAX = 5;

    private static BlockingQueue<Integer> taskQueue = new LinkedBlockingQueue<>();
    private static final Object printLock = new Object();

    static class Worker implements Runnable {
        private int workerId;

        public Worker(int workerId) {
            this.workerId = workerId;
        }

        @Override
        public void run() {
            try {
                while (!taskQueue.isEmpty()) { // Incorrect: Workers may exit prematurely
                    Integer task = taskQueue.poll(); // Incorrect: Should use take() instead of poll()
                    if (task == null) {
                        continue; // Incorrect: Should break or handle null properly
                    }

                    Random rand = new Random();
                    int processingTime = rand.nextInt(TASK_COMPLETION_TIME_MAX) + TASK_COMPLETION_TIME_MIN; // Incorrect: Range calculation is wrong

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " is processing task " + task + " (will take " + processingTime + " seconds)");
                    }

                    Thread.sleep(processingTime); // Incorrect: Missing multiplication by 1000 for milliseconds

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " completed task " + task);
                    }
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    static class Manager implements Runnable {
        @Override
        public void run() {
            try {
                for (int taskId = 1; taskId <= NUM_WORKERS * TASKS_PER_WORKER; taskId++) {
                    taskQueue.put(taskId);
                    synchronized (printLock) {
                        System.out.println("Manager assigned task " + taskId);
                    }
                }

                // Incorrect: No mechanism to wait for tasks to complete
                while (!taskQueue.isEmpty()) {
                    Thread.sleep(1000); // Busy-waiting is inefficient
                }

                synchronized (printLock) {
                    System.out.println("All tasks have been completed.");
                }

                for (int i = 0; i < NUM_WORKERS; i++) {
                    taskQueue.put(null); // Incorrect: Workers may not handle null properly
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Thread[] workers = new Thread[NUM_WORKERS];
        for (int i = 0; i < NUM_WORKERS; i++) {
            workers[i] = new Thread(new Worker(i + 1));
            workers[i].start();
        }

        Thread managerThread = new Thread(new Manager());
        managerThread.start();

        for (Thread worker : workers) {
            try {
                worker.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        try {
            managerThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("All workers and manager have finished.");
    }
}
"""
    }

    corrected_java_code = """
import java.util.concurrent.*;
import java.util.Random;

public class MultiThreadingExample {
    private static final int NUM_WORKERS = 5;
    private static final int TASKS_PER_WORKER = 3;
    private static final int TASK_COMPLETION_TIME_MIN = 1;
    private static final int TASK_COMPLETION_TIME_MAX = 5;

    private static BlockingQueue<Integer> taskQueue = new LinkedBlockingQueue<>();
    private static final Object printLock = new Object();
    private static CountDownLatch taskLatch; // To wait for all tasks to complete

    static class Worker implements Runnable {
        private int workerId;

        public Worker(int workerId) {
            this.workerId = workerId;
        }

        @Override
        public void run() {
            try {
                while (true) {
                    Integer task = taskQueue.take(); // Wait for a task
                    if (task == null) {
                        break; // Exit if a null task is received
                    }

                    Random rand = new Random();
                    int processingTime = rand.nextInt(TASK_COMPLETION_TIME_MAX - TASK_COMPLETION_TIME_MIN + 1) + TASK_COMPLETION_TIME_MIN;

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " is processing task " + task + " (will take " + processingTime + " seconds)");
                    }

                    Thread.sleep(processingTime * 1000); // Simulate task processing

                    synchronized (printLock) {
                        System.out.println("Worker " + workerId + " completed task " + task);
                    }

                    taskLatch.countDown(); // Signal that a task is completed
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    static class Manager implements Runnable {
        @Override
        public void run() {
            try {
                for (int taskId = 1; taskId <= NUM_WORKERS * TASKS_PER_WORKER; taskId++) {
                    taskQueue.put(taskId); // Add tasks to the queue
                    synchronized (printLock) {
                        System.out.println("Manager assigned task " + taskId);
                    }
                }

                taskLatch.await(); // Wait for all tasks to complete

                synchronized (printLock) {
                    System.out.println("All tasks have been completed.");
                }

                // Signal workers to exit by adding null tasks
                for (int i = 0; i < NUM_WORKERS; i++) {
                    taskQueue.put(null);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        taskLatch = new CountDownLatch(NUM_WORKERS * TASKS_PER_WORKER); // Initialize latch

        Thread[] workers = new Thread[NUM_WORKERS];
        for (int i = 0; i < NUM_WORKERS; i++) {
            workers[i] = new Thread(new Worker(i + 1));
            workers[i].start();
        }

        Thread managerThread = new Thread(new Manager());
        managerThread.start();

        // Wait for all worker threads to finish
        for (Thread worker : workers) {
            try {
                worker.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Wait for the manager thread to finish
        try {
            managerThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("All workers and manager have finished.");
    }
}
"""

    # Display in three sections
    st.subheader("Input Python Code")
    st.code(python_code, language="python")
    
    st.subheader(f"Translated Java Code ({model})")
    st.code(translated_java_code[model], language="java")
    
    st.subheader("Corrected Java Code")
    st.code(corrected_java_code, language="java")

# Python to Java Translation Section
elif st.session_state.selected_section == "Java to C++ Translation":
    st.header("Java to C++ Translation")
    
    # Dropdown to select the model
    model = st.selectbox("Select a translation model:", ["TransCoder", "CodeT5", "CodeBERT"])
    
    # Hardcoded Python multithreading function
    python_code = """
import concurrent.futures

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero"
"""

    translated_java_code = {
        "TransCoder": """
public class Main {
    public static void main(String[] args) {
        System.out.println("Translated code by TransCoder");
    }
}
""",
        "CodeT5": """
public class Main {
    public static void main(String[] args) {
        System.out.println("Translated code by CodeT5");
    }
}
""",
        "CodeBERT": """
public class Main {
    public static void main(String[] args) {
        System.out.println("Translated code by CodeBERT");
    }
}
"""
    }

    corrected_java_code = """
public class Main {
    public static void main(String[] args) {
        System.out.println("Corrected Java Code");
    }
}
"""

    # Display in three sections
    st.subheader("Input Python Code")
    st.code(python_code, language="python")
    
    st.subheader(f"Translated Java Code ({model})")
    st.code(translated_java_code[model], language="java")
    
    st.subheader("Corrected Java Code")
    st.code(corrected_java_code, language="java")
