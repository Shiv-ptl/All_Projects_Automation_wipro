import threading
import time

count =0
lock = threading.Lock()

def increment():
    global count
    with lock:
        for _ in range(10000):
            count += 1
# def increment():
#     global count
#     for _ in range(10000):
#             count += 1

t1=threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)