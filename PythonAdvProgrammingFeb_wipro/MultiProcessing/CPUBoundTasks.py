# Threading is not efficient for CPU-heavy tasks
# Solution → Multiprocessing

# Multiprocessing:

# Creates separate processes
# Each process has its own Python interpreter
# Uses multiple CPU cores

# I/O-Bound  File read, API calls   Threading
# CPU-Bound  Math, data processing  Multiprocessing


import time

from fontTools.ttx import process


def square_nums():
    for i in range(10_000_000):
        i*i

start = time.time()

square_nums()
square_nums()

print("time: ",time.time()-start)


#using multiprocessing
from multiprocessing import Process
def square_nums():
    for i in range(10_000_000):
        i*i

if __name__=="__main__":
    start = time.time()
    p1 = Process(target=square_nums)
    p2 = Process(target=square_nums)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Time : ",time.time()-start)


#using Pool(recommended methods)
from multiprocessing import Pool
import time

def square(n):
    return n*n

if __name__=="__main__":
    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:
        results = pool.map(square,numbers)

        print(results)




