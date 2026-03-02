import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1,2,3,4,5]
y= [1,11,18,-3,8]

plt.plot(x,y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple-Plot')

#show method will display the data
plt.show()

#simple data
subjects = ["Maths","Science","English","History","Computer"]
marks = [85,78,92,74,88]

plt.plot(subjects,marks)

plt.title('Student Marks')

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

plt.boxplot(marks)
plt.show()



data={
    "Months":['Jan','Feb','Mar','Apr','May','June','Jul'],
    "Sales":[100,150,110,75,120,160,175]
}

df = pd.DataFrame(data)

plt.plot(df['Months'],df['Sales'])

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()