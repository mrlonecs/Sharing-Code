import threading
import time


task_done_by_A = False
task_done_by_B = False

def worker_A():
    global task_done_by_A, task_done_by_B
    print("Worker A: starting and waiting for B to finish first...")
    # waits until B is done
    while not task_done_by_B:
        time.sleep(0.5)
    print("Worker A: now continuing after B.")
    task_done_by_A = True

def worker_B():
    global task_done_by_A, task_done_by_B
    print("Worker B: starting and waiting for A to finish first...")
    # waits until A is done
    while not task_done_by_A:
        time.sleep(0.5)
    print("Worker B: now continuing after A.")
    task_done_by_B = True

# Start both threads
t1 = threading.Thread(target=worker_A)
t2 = threading.Thread(target=worker_B)

t1.start()
t2.start()

t1.join()
t2.join()

print("This line will never print due to circular waiting!")
