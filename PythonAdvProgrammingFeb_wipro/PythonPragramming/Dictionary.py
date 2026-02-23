#dictionary items- key value
#for integers,tuoles and strings - keys must be immutable
#list cannot be used in the key for dictionary as it is mutable in nature

country = {
    "India":"Delhi",
    "Canada":"Ottawa",
    "England":"London"
}
print(country)
print(country["Canada"])

country["Itely"]="Rome"
print(country)
#remove element
del country["India"]
print(country)

#clear
c = {
    "India":"Delhi",
    "Canada":"Ottawa",
    "England":"London"
}
print(c)
c.clear()
print(c)
#int as a key
my_dict = {1:"one",2:"two",3:'three',5:"five"}
print(my_dict)

my_dict = {1:"four",2:"two",3:'three',4:"one"}
print(my_dict)
my_dict[1]='one'
print(my_dict)

#tuple as a key
tup_dict={(1,2):"one two",(3,4):"three four",5:"five"}
print(tup_dict)
tup_dict={(1,2):"one two",(3,4):"three four",6:"five"}
print(tup_dict)

#iterate among the dict
for coun in country:
    print(coun)

#length
print(len(country))

#pop-remove the items with spec key
country.pop("England")
print(country)
#update()  - adds or change the dict
dict1={'a':100,'b':200}
print(dict1)
dict2={'b':300,'c':400}
print(dict2)
dict1.update(dict2)
print(dict1)
print(dict2)


#keys()
k=dict1.keys()
print(k)
#values()
v=dict1.values()
print(v)
#popitem() returns the last inserted keyward
print(dict1.popitem())


#copy()

x=dict1.copy()
print(x)

#dict inside the list
students=[
    {"id":1,"name":"Shivanshu","roll":85},
    {"id":2,"name":"Gaurav","roll":86},
    {"id":3,"name":"Jatin","roll":87}
]
print(students[0])

print(students[0]["name"])
for s in students:
    print(s["name"],s["roll"])

students.append({"id":4,"name":"Akash","roll":88})

print(students)

##print(students.pop(1))

print(students)

for stu in students:
    if stu["id"] ==3:
        print(f"name = {stu["name"]} roll= {stu["roll"]}")