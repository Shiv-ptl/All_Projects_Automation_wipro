import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.array([1,2,3,4,5])

y = x*2
plt.hist(x, bins=5)
plt.show()
plt.hist(y,bins=5)
plt.show()
data = {
    "Day":['Mon','Tue','Wed','Thu','Fri','Sat',"Sun"],
    "Steps":[4000,5000,7000,6500,8000,5000,3500]
}

df = pd.DataFrame(data)

df.plot(y="Steps",kind='hist')
plt.title("Daily Setps Count")
plt.xlabel('Day')
plt.ylabel("Steps")
plt.show()


# plt.bar(df['Day'],df["Steps"])
# plt.title("Daily Setps Count")
# plt.xlabel('Day')
# plt.ylabel("Steps")
# plt.show()