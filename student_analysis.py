import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [80, 90, 70, 85, 95]
}

df = pd.DataFrame(data)

df['Average'] = np.mean(df['Marks'])

print(df)
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())

plt.bar(df['Name'], df['Marks'])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
