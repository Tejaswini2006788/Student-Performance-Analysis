import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV dataset
df = pd.read_csv("student_marks.csv")

# Calculate average marks
subjects = ['Python', 'Pandas', 'NumPy']
df['Average'] = np.mean(df[subjects], axis=1)

# Display student data
print("STUDENT PERFORMANCE ANALYSIS")
print(df)

# Highest and lowest average
print("Highest Average:", df['Average'].max())
print("Lowest Average:", df['Average'].min())

# Subject-wise average
print("Subject Average:")
print(df[subjects].mean())

# Create bar chart
plt.bar(df['Name'], df['Average'])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()
