# IO bound tasks
'''

An I/O-bound task is a task where:

The program waits for data from external resources

CPU is mostly idle while waiting

Performance is limited by disk, network, or database speed

Examples of external resources:

Files

Network requests

Databases

APIs

User input

'''


import  time
from sys import implementation


#example - without using the threading concept

def task():
    print("task started")
    time.sleep(3)
    print("task Compleated")

task()
task()

#total time 6seconds

import threading

#multi tasks concurrently within a single process
#Threads share the same memory space of the process
#this allows faster communication between them

def task():
    print("task started")
    time.sleep(3)
    print("task Compleated")

import threading

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

#fetch the api details
def fetch_data(api_name):
    print(f"fetching from {api_name}")
    time.sleep(2)
    print(f"fetching Compleated {api_name}")

apis = ["API1","API2","API3"]

threads = []
for api in apis:
    t =threading.Thread(target=fetch_data,args=(api,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All API calls compleated")

#file reading
def read_file(filename):
    with open(filename,"r") as f:
        data = f.read()
        print(f"{filename} read Compleated")

files = ["file1.txt","file2.txt","file3.txt"]

for file in files:
    t = threading.Thread(target=read_file,args=(file,))
    t.start()

for t in threads:
    t.join()