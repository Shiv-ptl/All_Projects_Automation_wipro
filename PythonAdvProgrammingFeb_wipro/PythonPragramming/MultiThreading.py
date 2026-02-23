#multi threading

import threading
import time

def nums():
    for i in range(5):
        print("Number: ",i)

def letters():
    for k in "ABCDE":
        print("Letter : ",k)

t1 = threading.Thread(target=nums)
t2 = threading.Thread(target=letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread terminated.")