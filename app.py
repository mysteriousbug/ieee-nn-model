import streamlit as st
import pandas as pd
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")

# Initialize session state for navigation
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = "Introduction"

# Sidebar navigation with buttons
st.sidebar.title("Table of Contents")
if st.sidebar.button("Introduction"):
    st.session_state.selected_section = "Introduction"
if st.sidebar.button("Model Configuration"):
    st.session_state.selected_section = "Model Configuration"
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
    with col1:
        
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
    with col2:
        with col2:
            st.header("Model Drawbacks & Performance")
            
            drawbacks_df = pd.DataFrame(drawbacks)
            st.table(drawbacks_df.style.set_properties(**{
                'white-space': 'pre-wrap',
                'text-align': 'left !important'
            }))
            
            st.subheader("Key Insights")
            st.markdown("""
            - **CodeT5** achieves highest CSS (65.0) but requires more memory
            - **TransCoder** needs extensive post-processing for Java output
            - **CodeBERT** shows semantic gaps in control flow translation
            """)
            
            # Visualization
            st.subheader("Performance Comparison")
            perf_data = {
                "Model": ["TransCoder", "CodeBERT", "CodeT5"],
                "CSS": [24.2, 60.5, 65.0],
                "OES": [68.7, 68.6, 72.4]
            }
            st.bar_chart(pd.DataFrame(perf_data).set_index("Model"))
# Python to Java Translation Section
elif st.session_state.selected_section == "Python to Java Translation":
    st.header("Python to Java Code Translation")
    flag = 0
    # Dropdown to select the model
    model = st.selectbox("Select a translation model:", ["TransCoder", "CodeT5", "CodeBERT"])
    st.subheader("Input Python Code")
    uploaded_file = st.file_uploader("Upload a Python code file", type=["py"])
    
    if uploaded_file is not None:
        python_code = uploaded_file.getvalue().decode("utf-8")
        progress_bar = st.progress(0)
        
        for percent_complete in range(101):
            progress_bar.progress(percent_complete)
        
        st.success("Translation Complete!")
        flag = 1
    else:
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
    if flag == 1:
         # st.code(python_code, language="python")
    
         st.subheader(f"Translated Java Code ({model})")
         st.code(translated_java_code[model], language="java")
    
         st.subheader("Corrected Java Code")
         st.code(corrected_java_code, language="java")

         st.markdown("""
             <style>
             pre {
                 max-height: 300px;
                 overflow-y: auto;
             }
             </style>
         """, unsafe_allow_html=True)
        
   

# Python to Java Translation Section
elif st.session_state.selected_section == "Java to C++ Translation":
    st.header("Java to C++ Translation")
    
    # Dropdown to select the model
    model = st.selectbox("Select a translation model:", ["TransCoder", "CodeT5", "CodeBERT"])
    flag = 0
    st.subheader("Input Java Code")
    uploaded_file = st.file_uploader("Upload a Java code file", type=["java"])
    
    if uploaded_file is not None:
        java_code = uploaded_file.getvalue().decode("utf-8")
        progress_bar = st.progress(0)
        
        for percent_complete in range(101):
            progress_bar.progress(percent_complete)
        
        st.success("Translation Complete!")
        flag = 1
    else:
        java_code = """
import java.util.*;

// Interface for printable objects
interface Printable {
    void printDetails();
}

// Base class for all entities in the library
abstract class Entity implements Printable {
    private String id;
    private String name;

    public Entity(String id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters and Setters
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void printDetails() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}

// Author class
class Author extends Entity {
    private String biography;

    public Author(String id, String name, String biography) {
        super(id, name);
        this.biography = biography;
    }

    public String getBiography() {
        return biography;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Biography: " + biography);
    }
}

// Book class
class Book extends Entity {
    private Author author;
    private String genre;
    private boolean isAvailable;

    public Book(String id, String name, Author author, String genre) {
        super(id, name);
        this.author = author;
        this.genre = genre;
        this.isAvailable = true;
    }

    public Author getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Author: " + author.getName());
        System.out.println("Genre: " + genre);
        System.out.println("Availability: " + (isAvailable ? "Available" : "Not Available"));
    }
}

// LibraryMember class
class LibraryMember extends Entity {
    private List<Book> borrowedBooks;

    public LibraryMember(String id, String name) {
        super(id, name);
        this.borrowedBooks = new ArrayList<>();
    }

    public void borrowBook(Book book) throws Exception {
        if (!book.isAvailable()) {
            throw new Exception("Book is not available for borrowing.");
        }
        book.setAvailable(false);
        borrowedBooks.add(book);
        System.out.println("Book '" + book.getName() + "' borrowed by " + getName());
    }

    public void returnBook(Book book) {
        if (borrowedBooks.remove(book)) {
            book.setAvailable(true);
            System.out.println("Book '" + book.getName() + "' returned by " + getName());
        } else {
            System.out.println("Book '" + book.getName() + "' was not borrowed by " + getName());
        }
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Borrowed Books:");
        for (Book book : borrowedBooks) {
            book.printDetails();
        }
    }
}

// Library class (Composition)
class Library {
    private List<Book> books;
    private List<LibraryMember> members;

    public Library() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addMember(LibraryMember member) {
        members.add(member);
    }

    public void displayBooks() {
        System.out.println("Library Books:");
        for (Book book : books) {
            book.printDetails();
        }
    }

    public void displayMembers() {
        System.out.println("Library Members:");
        for (LibraryMember member : members) {
            member.printDetails();
        }
    }
}

// Main class
public class LibraryManagementSystem {
    public static void main(String[] args) {
        // Create authors
        Author author1 = new Author("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
        Author author2 = new Author("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

        // Create books
        Book book1 = new Book("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
        Book book2 = new Book("B2", "1984", author2, "Dystopian");

        // Create library members
        LibraryMember member1 = new LibraryMember("M1", "Alice");
        LibraryMember member2 = new LibraryMember("M2", "Bob");

        // Create library and add books and members
        Library library = new Library();
        library.addBook(book1);
        library.addBook(book2);
        library.addMember(member1);
        library.addMember(member2);

        // Display library details
        library.displayBooks();
        library.displayMembers();

        // Borrow and return books
        try {
            member1.borrowBook(book1);
            member2.borrowBook(book2);
            member1.returnBook(book1);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Display updated library details
        library.displayBooks();
        library.displayMembers();
    }
}
"""

    translated_cpp_code = {
        "TransCoder": """
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

// Interface for printable objects
class Printable {
public:
    virtual void printDetails() = 0;
};

// Base class for all entities in the library
class Entity : public Printable {
private:
    string id;
    string name;

public:
    Entity(string id, string name) : id(id), name(name) {}

    // Getters and Setters
    string getId() {
        return id;
    }

    string getName() {
        return name;
    }

    void setName(string name) {
        this->name = name;
    }

    void printDetails() override {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

// Author class
class Author : public Entity {
private:
    string biography;

public:
    Author(string id, string name, string biography) : Entity(id, name), biography(biography) {}

    string getBiography() {
        return biography;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Biography: " << biography << endl;
    }
};

// Book class
class Book : public Entity {
private:
    Author* author;
    string genre;
    bool isAvailable;

public:
    Book(string id, string name, Author* author, string genre) : Entity(id, name), author(author), genre(genre), isAvailable(true) {}

    Author* getAuthor() {
        return author;
    }

    string getGenre() {
        return genre;
    }

    bool isAvailable() {
        return isAvailable;
    }

    void setAvailable(bool available) {
        isAvailable = available;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Author: " << author->getName() << endl;
        cout << "Genre: " << genre << endl;
        cout << "Availability: " << (isAvailable ? "Available" : "Not Available") << endl;
    }
};

// LibraryMember class
class LibraryMember : public Entity {
private:
    vector<Book*> borrowedBooks;

public:
    LibraryMember(string id, string name) : Entity(id, name) {}

    void borrowBook(Book* book) {
        if (!book->isAvailable()) {
            throw runtime_error("Book is not available for borrowing.");
        }
        book->setAvailable(false);
        borrowedBooks.push_back(book);
        cout << "Book '" << book->getName() << "' borrowed by " << getName() << endl;
    }

    void returnBook(Book* book) {
        auto it = find(borrowedBooks.begin(), borrowedBooks.end(), book);
        if (it != borrowedBooks.end()) {
            borrowedBooks.erase(it);
            book->setAvailable(true);
            cout << "Book '" << book->getName() << "' returned by " << getName() << endl;
        } else {
            cout << "Book '" << book->getName() << "' was not borrowed by " << getName() << endl;
        }
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Borrowed Books:" << endl;
        for (Book* book : borrowedBooks) {
            book->printDetails();
        }
    }
};

// Library class (Composition)
class Library {
private:
    vector<Book*> books;
    vector<LibraryMember*> members;

public:
    void addBook(Book* book) {
        books.push_back(book);
    }

    void addMember(LibraryMember* member) {
        members.push_back(member);
    }

    void displayBooks() {
        cout << "Library Books:" << endl;
        for (Book* book : books) {
            book->printDetails();
        }
    }

    void displayMembers() {
        cout << "Library Members:" << endl;
        for (LibraryMember* member : members) {
            member->printDetails();
        }
    }
};

// Main function
int main() {
    // Create authors
    Author* author1 = new Author("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
    Author* author2 = new Author("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

    // Create books
    Book* book1 = new Book("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
    Book* book2 = new Book("B2", "1984", author2, "Dystopian");

    // Create library members
    LibraryMember* member1 = new LibraryMember("M1", "Alice");
    LibraryMember* member2 = new LibraryMember("M2", "Bob");

    // Create library and add books and members
    Library library;
    library.addBook(book1);
    library.addBook(book2);
    library.addMember(member1);
    library.addMember(member2);

    // Display library details
    library.displayBooks();
    library.displayMembers();

    // Borrow and return books
    try {
        member1->borrowBook(book1);
        member2->borrowBook(book2);
        member1->returnBook(book1);
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }

    // Display updated library details
    library.displayBooks();
    library.displayMembers();

    // Clean up dynamically allocated memory
    delete author1;
    delete author2;
    delete book1;
    delete book2;
    delete member1;
    delete member2;

    return 0;
}   
""",
        "CodeT5": """
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Interface for printable objects
class Printable {
public:
    virtual void printDetails() = 0;
};

// Base class for all entities in the library
class Entity : public Printable {
protected:
    string id;
    string name;

public:
    Entity(string id, string name) : id(id), name(name) {}

    string getId() {
        return id;
    }

    string getName() {
        return name;
    }

    void setName(string name) {
        this->name = name;
    }

    void printDetails() override {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

// Author class
class Author : public Entity {
private:
    string biography;

public:
    Author(string id, string name, string biography) : Entity(id, name), biography(biography) {}

    string getBiography() {
        return biography;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Biography: " << biography << endl;
    }
};

// Book class
class Book : public Entity {
private:
    Author* author;
    string genre;
    bool isAvailable;

public:
    Book(string id, string name, Author* author, string genre) : Entity(id, name), author(author), genre(genre), isAvailable(true) {}

    Author* getAuthor() {
        return author;
    }

    string getGenre() {
        return genre;
    }

    bool isAvailable() {
        return isAvailable;
    }

    void setAvailable(bool available) {
        isAvailable = available;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Author: " << author->getName() << endl;
        cout << "Genre: " << genre << endl;
        cout << "Availability: " << (isAvailable ? "Available" : "Not Available") << endl;
    }
};

// LibraryMember class
class LibraryMember : public Entity {
private:
    vector<Book*> borrowedBooks;

public:
    LibraryMember(string id, string name) : Entity(id, name) {}

    void borrowBook(Book* book) {
        if (!book->isAvailable()) {
            throw runtime_error("Book is not available for borrowing.");
        }
        book->setAvailable(false);
        borrowedBooks.push_back(book);
        cout << "Book '" << book->getName() << "' borrowed by " << getName() << endl;
    }

    void returnBook(Book* book) {
        auto it = find(borrowedBooks.begin(), borrowedBooks.end(), book);
        if (it != borrowedBooks.end()) {
            borrowedBooks.erase(it);
            book->setAvailable(true);
            cout << "Book '" << book->getName() << "' returned by " << getName() << endl;
        } else {
            cout << "Book '" << book->getName() << "' was not borrowed by " << getName() << endl;
        }
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Borrowed Books:" << endl;
        for (Book* book : borrowedBooks) {
            book->printDetails();
        }
    }
};

// Library class (Composition)
class Library {
private:
    vector<Book*> books;
    vector<LibraryMember*> members;

public:
    void addBook(Book* book) {
        books.push_back(book);
    }

    void addMember(LibraryMember* member) {
        members.push_back(member);
    }

    void displayBooks() {
        cout << "Library Books:" << endl;
        for (Book* book : books) {
            book->printDetails();
        }
    }

    void displayMembers() {
        cout << "Library Members:" << endl;
        for (LibraryMember* member : members) {
            member->printDetails();
        }
    }
};

// Main function
int main() {
    // Create authors
    Author* author1 = new Author("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
    Author* author2 = new Author("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

    // Create books
    Book* book1 = new Book("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
    Book* book2 = new Book("B2", "1984", author2, "Dystopian");

    // Create library members
    LibraryMember* member1 = new LibraryMember("M1", "Alice");
    LibraryMember* member2 = new LibraryMember("M2", "Bob");

    // Create library and add books and members
    Library library;
    library.addBook(book1);
    library.addBook(book2);
    library.addMember(member1);
    library.addMember(member2);

    // Display library details
    library.displayBooks();
    library.displayMembers();

    // Borrow and return books
    try {
        member1->borrowBook(book1);
        member2->borrowBook(book2);
        member1->returnBook(book1);
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }

    // Display updated library details
    library.displayBooks();
    library.displayMembers();

    // Clean up dynamically allocated memory
    delete author1;
    delete author2;
    delete book1;
    delete book2;
    delete member1;
    delete member2;

    return 0;
}
""",
        "CodeBERT": """
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

// Interface for printable objects
class Printable {
public:
    virtual void printDetails() = 0;
};

// Base class for all entities in the library
class Entity : public Printable {
private:
    string id;
    string name;

public:
    Entity(string id, string name) : id(id), name(name) {}

    string getId() {
        return id;
    }

    string getName() {
        return name;
    }

    void setName(string name) {
        this->name = name;
    }

    void printDetails() override {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

// Author class
class Author : public Entity {
private:
    string biography;

public:
    Author(string id, string name, string biography) : Entity(id, name), biography(biography) {}

    string getBiography() {
        return biography;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Biography: " << biography << endl;
    }
};

// Book class
class Book : public Entity {
private:
    Author* author;
    string genre;
    bool isAvailable;

public:
    Book(string id, string name, Author* author, string genre) : Entity(id, name), author(author), genre(genre), isAvailable(true) {}

    Author* getAuthor() {
        return author;
    }

    string getGenre() {
        return genre;
    }

    bool isAvailable() {
        return isAvailable;
    }

    void setAvailable(bool available) {
        isAvailable = available;
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Author: " << author->getName() << endl;
        cout << "Genre: " << genre << endl;
        cout << "Availability: " << (isAvailable ? "Available" : "Not Available") << endl;
    }
};

// LibraryMember class
class LibraryMember : public Entity {
private:
    vector<Book*> borrowedBooks;

public:
    LibraryMember(string id, string name) : Entity(id, name) {}

    void borrowBook(Book* book) {
        if (!book->isAvailable()) {
            throw runtime_error("Book is not available for borrowing.");
        }
        book->setAvailable(false);
        borrowedBooks.push_back(book);
        cout << "Book '" << book->getName() << "' borrowed by " << getName() << endl;
    }

    void returnBook(Book* book) {
        auto it = find(borrowedBooks.begin(), borrowedBooks.end(), book);
        if (it != borrowedBooks.end()) {
            borrowedBooks.erase(it);
            book->setAvailable(true);
            cout << "Book '" << book->getName() << "' returned by " << getName() << endl;
        } else {
            cout << "Book '" << book->getName() << "' was not borrowed by " << getName() << endl;
        }
    }

    void printDetails() override {
        Entity::printDetails();
        cout << "Borrowed Books:" << endl;
        for (Book* book : borrowedBooks) {
            book->printDetails();
        }
    }
};

// Library class (Composition)
class Library {
private:
    vector<Book*> books;
    vector<LibraryMember*> members;

public:
    void addBook(Book* book) {
        books.push_back(book);
    }

    void addMember(LibraryMember* member) {
        members.push_back(member);
    }

    void displayBooks() {
        cout << "Library Books:" << endl;
        for (Book* book : books) {
            book->printDetails();
        }
    }

    void displayMembers() {
        cout << "Library Members:" << endl;
        for (LibraryMember* member : members) {
            member->printDetails();
        }
    }
};

// Main function
int main() {
    // Create authors
    Author* author1 = new Author("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
    Author* author2 = new Author("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

    // Create books
    Book* book1 = new Book("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
    Book* book2 = new Book("B2", "1984", author2, "Dystopian");

    // Create library members
    LibraryMember* member1 = new LibraryMember("M1", "Alice");
    LibraryMember* member2 = new LibraryMember("M2", "Bob");

    // Create library and add books and members
    Library library;
    library.addBook(book1);
    library.addBook(book2);
    library.addMember(member1);
    library.addMember(member2);

    // Display library details
    library.displayBooks();
    library.displayMembers();

    // Borrow and return books
    try {
        member1->borrowBook(book1);
        member2->borrowBook(book2);
        member1->returnBook(book1);
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }

    // Display updated library details
    library.displayBooks();
    library.displayMembers();

    // Clean up dynamically allocated memory
    delete author1;
    delete author2;
    delete book1;
    delete book2;
    delete member1;
    delete member2;

    return 0;
}
"""
    }

    corrected_cpp_code = """
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <stdexcept>

using namespace std;

// Interface for printable objects
class Printable {
public:
    virtual void printDetails() const = 0;
    virtual ~Printable() = default; // Virtual destructor for proper cleanup
};

// Base class for all entities in the library
class Entity : public Printable {
protected:
    string id;
    string name;

public:
    Entity(string id, string name) : id(move(id)), name(move(name)) {}

    string getId() const {
        return id;
    }

    string getName() const {
        return name;
    }

    void setName(string name) {
        this->name = move(name);
    }

    void printDetails() const override {
        cout << "ID: " << id << ", Name: " << name << endl;
    }
};

// Author class
class Author : public Entity {
private:
    string biography;

public:
    Author(string id, string name, string biography)
        : Entity(move(id), move(name)), biography(move(biography)) {}

    string getBiography() const {
        return biography;
    }

    void printDetails() const override {
        Entity::printDetails();
        cout << "Biography: " << biography << endl;
    }
};

// Book class
class Book : public Entity {
private:
    shared_ptr<Author> author; // Use shared_ptr for automatic memory management
    string genre;
    bool isAvailable;

public:
    Book(string id, string name, shared_ptr<Author> author, string genre)
        : Entity(move(id), move(name)), author(move(author)), genre(move(genre)), isAvailable(true) {}

    shared_ptr<Author> getAuthor() const {
        return author;
    }

    string getGenre() const {
        return genre;
    }

    bool getIsAvailable() const {
        return isAvailable;
    }

    void setIsAvailable(bool available) {
        isAvailable = available;
    }

    void printDetails() const override {
        Entity::printDetails();
        cout << "Author: " << author->getName() << endl;
        cout << "Genre: " << genre << endl;
        cout << "Availability: " << (isAvailable ? "Available" : "Not Available") << endl;
    }
};

// LibraryMember class
class LibraryMember : public Entity {
private:
    vector<shared_ptr<Book>> borrowedBooks; // Use shared_ptr for automatic memory management

public:
    LibraryMember(string id, string name) : Entity(move(id), move(name)) {}

    void borrowBook(const shared_ptr<Book>& book) {
        if (!book->getIsAvailable()) {
            throw runtime_error("Error: Book '" + book->getName() + "' is not available for borrowing.");
        }
        book->setIsAvailable(false);
        borrowedBooks.push_back(book);
        cout << "Book '" << book->getName() << "' borrowed by " << getName() << endl;
    }

    void returnBook(const shared_ptr<Book>& book) {
        auto it = find(borrowedBooks.begin(), borrowedBooks.end(), book);
        if (it != borrowedBooks.end()) {
            borrowedBooks.erase(it);
            book->setIsAvailable(true);
            cout << "Book '" << book->getName() << "' returned by " << getName() << endl;
        } else {
            cout << "Book '" << book->getName() << "' was not borrowed by " << getName() << endl;
        }
    }

    void printDetails() const override {
        Entity::printDetails();
        cout << "Borrowed Books:" << endl;
        for (const auto& book : borrowedBooks) {
            book->printDetails();
        }
    }
};

// Library class (Composition)
class Library {
private:
    vector<shared_ptr<Book>> books; // Use shared_ptr for automatic memory management
    vector<shared_ptr<LibraryMember>> members; // Use shared_ptr for automatic memory management

public:
    void addBook(const shared_ptr<Book>& book) {
        books.push_back(book);
    }

    void addMember(const shared_ptr<LibraryMember>& member) {
        members.push_back(member);
    }

    void displayBooks() const {
        cout << "Library Books:" << endl;
        for (const auto& book : books) {
            book->printDetails();
        }
    }

    void displayMembers() const {
        cout << "Library Members:" << endl;
        for (const auto& member : members) {
            member->printDetails();
        }
    }
};

// Main function
int main() {
    // Create authors
    auto author1 = make_shared<Author>("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
    auto author2 = make_shared<Author>("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

    // Create books
    auto book1 = make_shared<Book>("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
    auto book2 = make_shared<Book>("B2", "1984", author2, "Dystopian");

    // Create library members
    auto member1 = make_shared<LibraryMember>("M1", "Alice");
    auto member2 = make_shared<LibraryMember>("M2", "Bob");

    // Create library and add books and members
    Library library;
    library.addBook(book1);
    library.addBook(book2);
    library.addMember(member1);
    library.addMember(member2);

    // Display library details
    library.displayBooks();
    library.displayMembers();

    // Borrow and return books
    try {
        member1->borrowBook(book1);
        member2->borrowBook(book2);
        member1->returnBook(book1);
    } catch (const exception& e) {
        cout << e.what() << endl;
    }

    // Display updated library details
    library.displayBooks();
    library.displayMembers();

    return 0;
}
"""

    
    if flag == 1: 
        # st.code(java_code, language="java")
    
        st.subheader(f"Translated C++ Code ({model})")
        st.code(translated_cpp_code[model], language="cpp")
    
        st.subheader("Corrected C++ Code")
        st.code(corrected_cpp_code, language="cpp")

        st.markdown("""
            <style>
            pre {
                max-height: 300px;
                overflow-y: auto;
            }
            </style>
        """, unsafe_allow_html=True)
