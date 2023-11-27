#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:02:34 2023

@author: saikiranakula
"""

import matplotlib.pyplot as plt
import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = '/Users/saikiranakula/Downloads/pie1.xlsx'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file)
print(df)

# Create a Pandas DataFrame from the data
df = pd.DataFrame({'Shares in 2019': [27.7,23.4,19.6,17.2,12.1],
                   'Shares in 2022': [30.2,25.7,17.1,12.4,14.6]},
                  index=['Tesco', 'Sainsbury\'s', 'Asda', 'Morrisons','Aldi'])
# Create a pie chart
plot = df.plot.pie(y='Shares in 2019', figsize=(4,4))
plot = df.plot.pie(subplots=True, figsize=(15,15))
# Display the pie chart
plt.show()