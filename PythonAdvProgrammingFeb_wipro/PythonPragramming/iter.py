#iter() method
# iterations - looping in the collection of items
# create an iterator from an iterable

a = [ 10,20,30,40,50,60,70,80,90]

#convert the list into an iterator
iterator= iter(a)

#next(0) allow the user to access the elements

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the string into an iterator

s= "Shivanshu"

iterator = iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the dict into an iterator
students={20:"Shivanshu",
          21:"Jatin",
          22:"Sutam",
          23:"Nitish",
          24:"shubham",
          25:"Abhinash"}

iterator = iter(students)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("hello")
for key in iterator:
    print(key)

it = iter(students.items())
for key,value in it:
    print(key, "-> ",value)

#iter(callable, sentinel)
# it = iter(input,"quit")
#
# for value in it:
#     print("You Enter : ",value)
#
def get_input():
    return input("Enter value: ")

for value in iter(get_input,"quit"):
    print("you entered: " , value)

print("Loop ended.")