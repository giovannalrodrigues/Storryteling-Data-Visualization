# -*- coding: utf-8 -*-
"""
storytelling_data_visualization.ipynb
"""
import matplotlib.pyplot as plt
import pandas as pd

exchange_rates2 = pd.read_csv('euro-daily-hist_1999_2022.csv')

# Data Cleaning


exchange_rates2.rename(columns={'[US dollar ]': 'US_dollar',
                                'Period\\Unit:': 'Time'},
                       inplace=True)
exchange_rates2['Time'] = pd.to_datetime(exchange_rates2['Time'])
exchange_rates2.sort_values('Time', inplace=True)


def new_func(exchange_rates):
    """Função exchange"""
    euro_to_dollar = exchange_rates[['Time', 'US_dollar']].copy()
    return euro_to_dollar


euro_to_dollar2 = new_func(exchange_rates2)

euro_to_dollar2['US_dollar'].value_counts()  # 62 '-' characters

euro_to_dollar2 = euro_to_dollar2[euro_to_dollar2['US_dollar'] != '-']
euro_to_dollar2['US_dollar'] = euro_to_dollar2['US_dollar'].astype(float)
euro_to_dollar2.info()

# """# Rolling Mean"""

# Commented out IPython magic to ensure Python compatibility.

# %matplotlib inline

plt.plot(euro_to_dollar2['Time'], euro_to_dollar2['US_dollar'])
plt.show()

plt.figure(figsize=(9, 6))

plt.subplot(3, 2, 1)
plt.plot(euro_to_dollar2['Time'], euro_to_dollar2['US_dollar'])
plt.title('Original values', weight='bold')

for i, rolling_mean in zip([2, 3, 4, 5, 6],
                           [7, 30, 50, 100, 365]):
    plt.subplot(3, 2, i)
    plt.plot(euro_to_dollar2['Time'],
             euro_to_dollar2['US_dollar'].rolling(rolling_mean).mean())
    plt.title('Rolling Window:' + str(rolling_mean), weight='bold')

plt.tight_layout()  # Auto-adjusts the padding between subplots
plt.show()

euro_to_dollar2['rolling_mean'] = euro_to_dollar2['US_dollar'].rolling(
    30).mean()
# euro_to_dollar
