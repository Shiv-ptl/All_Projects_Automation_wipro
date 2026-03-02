import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "Day":['Mon','Tue','Wed','Thu','Fri','Sat',"Sun"],
    "Steps":[4000,5000,7000,6500,8000,5000,3500]
}

df = pd.DataFrame(data)

df.plot(x='Day',y="Steps",kind='bar')
plt.title("Daily Setps Count")
plt.xlabel('Day')
plt.ylabel("Steps")
#plt.show()

#Save As Image -jpg
plt.savefig("BarChart.jpg")

#save as pdf
plt.savefig("BarChart.pdf",format="pdf")