#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:01:27 2023

@author: saikiranakula
"""


import matplotlib.pyplot as plt
import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = '/Users/saikiranakula/Downloads/line.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file)
print(df)

#crease the dataframe
df = pd.DataFrame({
    'Trains': [12.10,9.85,8.40,10.20],
    'Food': [12.10,16.40,14.40,14.09],
    'Bus': [9.8,8.6,7.4,9.2],
    'Metro':[6.2,6.7,8.9,12.4]}
, index=['week1','week2','week3','week4'])

# Create a line plot for the DataFrame
ax = df.plot( marker='o', figsize=(8, 5))

# Set labels and title
plt.xlabel('Weeks')
plt.ylabel('charges in £')
plt.title('Transportation Charges')

# Display the plot
plt.grid(True)
plt.legend()

#show the plot
plt.show()