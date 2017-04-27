# coding: utf-8
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
crimes = read_csv('../data/Chicago_Crimes_2001_to_2004.csv', index_col='Date', error_bad_lines=False)
crimes = crimes.append(read_csv('../data/Chicago_Crimes_2005_to_2007.csv', index_col='Date', error_bad_lines=False))
crimes = crimes.append(read_csv('../data/Chicago_Crimes_2008_to_2011.csv', index_col='Date', error_bad_lines=False))
crimes = crimes.append(read_csv('../data/Chicago_Crimes_2012_to_2017.csv', index_col='Date', error_bad_lines=False))
crimes = crimes.iloc[:, 3: ]
crimes.head()
crimes.index = pd.to_datetime(crimes.index)
crimes.sort_index(inplace=True)
crimes.shape
crimes.head()
types = crimes[['Primary Type']]
types.head()
crime_count = pd.DataFrame(types.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
crime_count.head()
sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(12,15))
sns.set_color_codes("pastel")
sns.barplot(x="count", y="Primary Type", data = crime_count.iloc[:10, :], label="Total", color="b")
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="Type", xlabel="Crimes")
sns.despine(left=True, bottom=True)
plt.show()
arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']
plt.subplot()
arrest_yearly.resample('A').sum().plot()
plt.title('Yearly arrests')
plt.show()
arrest_yearly.resample('M').sum().plot()
plt.title('Monthly arrests')
plt.show()
arrest_yearly.resample('W').sum().plot()
plt.title('Weekly arrests')
plt.show()
top_crimes = pd.DataFrame(crimes[crimes['Primary Type'].isin(['THEFT', 'BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
grouper = top_crimes.groupby([pd.TimeGrouper('M'), 'Primary Type'])
data_top_crimes = grouper['Primary Type'].count().unstack()
data_top_crimes.plot()
plt.title("Top 5 monthly crimes")
plt.show()
