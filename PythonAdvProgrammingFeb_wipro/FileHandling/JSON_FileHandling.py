#JSON- javascript object notation
#data stored in name and value pairs

import json
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//employee.json",'r') as file:
    data = json.load(file)
#read the json file
print(data)
print(data["name"])

with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//NestedJSON.json",'r') as file:
    data = json.load(file)

print(data)
email = data["user"]["profile"]["email"]
print(email)
id = data["user"]["id"]
print(id)

#writing to the json file
data={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//WriteJSON.json",'w') as file:
    json.dump(data,file)



with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//UpdateJSON.json",'w') as file:
    json.dump(data,file)

with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//UpdateJSON.json",'r') as file:
    data= json.load(file)

print(data)
#update the value
data["experience"]=6

#write back
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//UpdateJSON.json",'w') as file:
    json.dump(data,file,indent=4)




