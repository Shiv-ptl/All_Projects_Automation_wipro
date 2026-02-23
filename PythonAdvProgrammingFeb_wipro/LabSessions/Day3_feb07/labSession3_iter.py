# Create a custom iterator that prints numbers from 1 to 5.
class OneToFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

for i in OneToFive():
    print(i)

# Write an iterator class that returns next even number.
# Explain and demonstrate the use of __iter__() and __next__()

class Demo:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 8:
            val = self.x
            self.x += 1
            return val
        else:
            raise StopIteration

obj = Demo()

for i in obj:
    print(i)
