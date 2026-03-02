import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.f2py.crackfortran import kindselector

x = np.array([1,2,3,4,5])

y = x*2

plt.plot(x,y)
plt.show()

x = np.arange(1,100,1)
y = x**2

plt.title("Square plot")
plt.xlabel("nums")
plt.ylabel("Squares")

plt.plot(x,y)
plt.show()

data = {
    "Day":['Mon','Tue','Wed','Thu','Fri','Sat',"Sun"],
    "Steps":[4000,5000,7000,6500,8000,5000,3500]
}

df = pd.DataFrame(data)

df.plot(x='Day',y="Steps",kind='pie')
plt.title("Daily Setps Count")
plt.xlabel('Day')
plt.ylabel("Steps")
plt.show()


# Pie
plt.pie(df['Steps'], labels=df['Day'], autopct='%1.1f%%')
plt.title("Steps Contribution by Day")
plt.show()