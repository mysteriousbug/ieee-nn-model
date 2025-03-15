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
