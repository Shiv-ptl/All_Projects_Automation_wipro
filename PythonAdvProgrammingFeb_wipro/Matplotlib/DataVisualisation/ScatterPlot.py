import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2

# Histogram
plt.hist(x, bins=5)
plt.title("Histogram of x")
plt.show()

plt.hist(y, bins=5)
plt.title("Histogram of y")
plt.show()

# Data
data = {
    "Day":['Mon','Tue','Wed','Thu','Fri','Sat',"Sun"],
    "Steps":[4000,5000,7000,6500,8000,5000,3500]
}

df = pd.DataFrame(data)


# Scatter
plt.scatter(x, y)
plt.title("Scatter Plot of x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

df.plot(x='Day',y='Steps',kind="scatter")
plt.title("Steps by day")
plt.show()

