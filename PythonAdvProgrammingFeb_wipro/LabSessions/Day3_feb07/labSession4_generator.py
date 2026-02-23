# Write a generator to generate numbers from 1 to N.
def numbers_upto_n(n):
    for i in range(1, n + 1):
        yield i

for num in numbers_upto_n(5):
    print(num)

print("END\n")

# Create a generator to generate even numbers only.
def numbers_upto_n(n):
    for i in range(2, n + 1,2):
        yield i

for num in numbers_upto_n(100):
    print(num)


print("END\n")
# Write a generator to read a file line by line.

def read_file_line_by_line(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_file_line_by_line("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//employee.json"):
    print(line)


# Create a generator for Fibonacci series.
def fibo(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

for n in fibo(20):
    print(n)
# Write a generator that simulates retry attempts (max 3 tries).


def retry_att(max_att=3):
    att=1
    while att<=max_att:
        yield f"attempts = {att}"
        att+=1

#for att in retry_att():
    # print(att)
    # print(att)
    # print(att)

gen = retry_att()

print(next(gen))
print(next(gen))
print(next(gen))



