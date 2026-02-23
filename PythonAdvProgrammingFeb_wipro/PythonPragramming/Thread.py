#threading - exicution of tasls
#multithreading- exicution of many tasls at a time - cuncurrent execution
#multiprocessing

#threading - imported

#process - exicution unit
#threads - light weight unit inside the process

#simple thread

import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread Finished")

t =threading.Thread(target=task)
t.start()
t.join()

print("Thread Terminated")


