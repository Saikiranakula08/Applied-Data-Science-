#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:03:12 2023

@author: saikiranakula
"""

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = '/Users/saikiranakula/Downloads/samp4 (1)-2.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file)

# Now you can work with the data in the DataFrame (e.g., display the first few rows)
print(df.head())
# Set the 'Category' column as the index
df.set_index('Year', inplace=True)

# Create a 2D bar graph for Fruits Sales In India
df.plot(kind='bar', figsize=(10,7))
plt.title('Fruits Sales In India')
plt.xlabel('Year')
plt.ylabel('Tonnes')
plt.xticks(rotation=0)  # Rotate x-axis labels (0 degrees)

# Display the 2D bar graph
plt.show()