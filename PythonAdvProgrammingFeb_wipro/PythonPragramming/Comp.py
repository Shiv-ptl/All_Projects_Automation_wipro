#Comprihentions- create lists using a single line of code insted of loops

#syntax
# [expression for item in iterable if condition]

#square of a number
sqs= [x**2 for x in range(1,6)]
print(sqs)

#with the condition
evennums = [x for x in range(10) if x%2==0]
print(evennums)

#dictionary comprihention - increasing by 10%
salary = { "A":50000,"B":60000,"C": 70000}
updatedsalary = {k:y+0.1*y for k,y in salary.items()}
print(updatedsalary)

#sq_dict =

#filtering of dict

sal = {k:v for k ,v in salary.items() if v>=60000}
print(sal)
#set comphention
sqs = {x**2 for x in range(1,10)}
print(sqs)
#with the condition
evennums = {x for x in range(10) if x%2==0}
print(evennums)

sqs = [x**2 for x in range(1,10)]
print(sqs)