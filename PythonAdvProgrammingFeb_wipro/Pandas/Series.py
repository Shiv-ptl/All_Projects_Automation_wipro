# Pandas - high perfomance data manipulation and data analysis tool
# 2008 Mckinnley
# data frame object
# list , csv , josn , pdf

# series - A one-dimensional labeled homogeneous array, sizeimmutable.
# DataFrames    2  A two-dimensional labeled, size-mutable tabular structure with potentially heterogeneously typed columns.


import pandas as pd
import numpy as np

# -----------------------------
# Create Series from List
# -----------------------------
data = ['Steve', 35, 'Male', 3.5]

series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Rating'])
print("Series from List:")
print(series)

# -----------------------------
# Create Series with Custom Index
# -----------------------------
data = [100, 200, 300]

s = pd.Series(data, index=['a', 'b', 'c'])
print("\nSeries with Custom Index:")
print(s)

# -----------------------------
# Create Series from Dictionary
# -----------------------------
data = {'a': 1, 'b': 2, 'c': 3}

s = pd.Series(data)
print("\nSeries from Dictionary:")
print(s)

# -----------------------------
# Create Series from NumPy Array
# -----------------------------
data = np.array([10, 20, 30, 40])

s = pd.Series(data)
print("\nSeries from NumPy Array:")
print(s)