import xml.etree.ElementTree as ET

tree = ET.parse("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//employee.xml")
root = tree.getroot()
print(root.tag)


for x in  root:
    print(x.tag)
    print(x.attrib)

# Tag  → find()
# Attr → get()

#fetch all attributes in the child node
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)
    emp_name=employee.find("name").text
    print(emp_name)

for emp in root.findall("employee"):
    name=emp.find("name").text
    role= emp.find("role").text
    experience= emp.find("experience").text
    print(name,role,experience)


#write the data in xml
employees = ET.Element("employees")

# First employee
emp1 = ET.SubElement(employees, "employee", id="101")
ET.SubElement(emp1, "name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"

# Second employee
emp2 = ET.SubElement(employees, "employee", id="102")
ET.SubElement(emp2, "name").text = "Amit"
ET.SubElement(emp2, "role").text = "Developer"
ET.SubElement(emp2, "experience").text = "3"


tree=ET.ElementTree(root)
tree.write("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//WriteXML.xml",encoding="utf-8", xml_declaration=True)

#updating the xml

tree = ET.parse("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//Updatexml.xml")
root=tree.getroot()

for emp in root.findall("employee"):
    if emp.get("id")=="101":
        emp.find("experience").text="16"

ET.indent(tree, space="    ",level=0)
tree.write("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//Updatexml.xml",encoding="utf-8", xml_declaration=True)