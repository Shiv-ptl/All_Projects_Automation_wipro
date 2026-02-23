#generators-special type fun - return one value a time ,on demand

# yield -
#memory efficient
#use full large set of data
#files,retries,batching

#normal function

def numbers():
    return [1,2,3,4,5,6]

print(numbers())
#normal fun loads all the values int0 memory


#generator

def generator():
    print("printing 1 : ")
    yield 1

    print("printing 2 : ")
    yield 2

    print("printing 3 : ")
    yield 3

ret_values = generator()

print(next(ret_values))
print(next(ret_values))
print(next(ret_values))

