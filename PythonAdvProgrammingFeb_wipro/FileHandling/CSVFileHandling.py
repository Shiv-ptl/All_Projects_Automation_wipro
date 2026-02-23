#csv - comma seperated values

import csv
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//write.csv","w",newline="")as file:
    writer= csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow(["1", "Shivanshu", "90"])
    writer.writerow(["2", "Nitin", "85"])

#appending th edata to csv file
with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//data.csv","a",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Jatin",25,'M',"Pune"])