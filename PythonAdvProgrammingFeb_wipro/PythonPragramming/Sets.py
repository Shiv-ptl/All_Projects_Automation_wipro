#unorderd collection,unique values
student_id={111,112,113,114,115,113}
print(student_id)
letters = {'a','b','c','d' }
print(letters)
mix_set={"Hello",123,4,-2,5,'Z',2.3}
print(mix_set)

#empty set
empty_set= set()

student_id.add(117)
print(student_id)

x=student_id.copy()
print(x)

#x.clear()
x.add(56)
x.add(12)
print(x)
print(x.difference(student_id))
print(x-student_id)

x.discard(12)
print(x)
print(student_id)
print(x<=student_id)
print(student_id<=x)


