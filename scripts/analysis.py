#!/usr/bin/env
import sys

import pandas as pd
from pandas import read_csv
import csv
import mysql.connector
import config
from config import db, table_name
import seaborn as sns
import matplotlib.pyplot as plt

#configure stdout to file
orig_stdout = sys.stdout
outfile = open('../output/output.txt', 'w')
sys.stdout = outfile

#Connect DB and import data
mydb = mysql.connector.connect(user=db['user'],
    password=db['password'],
    host=db['host'],
    db=db['db'])
cursor = mydb.cursor()

sql = "select * from " + table_name

#Pulling data
#crimes = pd.read_sql(sql, mydb)
crimes = read_csv('../data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')
crimes2 = read_csv('../data/Chicago_Crimes_2001_to_2004.csv', index_col='Date', error_bad_lines=False)
crimes3 = read_csv('../data/Chicago_Crimes_2005_to_2007.csv', index_col='Date', error_bad_lines=False)
crimes4 = read_csv('../data/Chicago_Crimes_2008_to_2011.csv', index_col='Date', error_bad_lines=False)

crimes2 = crimes2.append(crimes3)
crimes2 = crimes2.append(crimes4)
crimes = crimes2.append(crimes)

#Truncate needless first 3 columns
crimes = crimes.iloc[:, 3: ]
print(crimes.head())

#Index by Date
#crimes = crimes.set_index('Date')
crimes.index = pd.to_datetime(crimes.index)
crimes.sort_index(inplace=True)
print(crimes.shape)
print(crimes.head())
types = crimes[['Primary Type']]
print(types.head())

#Output sorted most occurrent crime types
crime_count = pd.DataFrame(types.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
print(crime_count.head())

#seaborn - a better visualization for crime amounts
sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(6,15))

sns.set_color_codes("pastel")
sns.barplot(x="count", y="Primary Type", data = crime_count.iloc[:10, :], label="Total", color="b")
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="Type", xlabel="Crimes")
sns.despine(left=True, bottom=True)
plt.show()


#Yearly crimes
arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']

plt.subplot()
#Yearly
arrest_yearly.resample('A').sum().plot()
plt.title('Yearly Arrests')
plt.show()
#Monthly
arrest_yearly.resample('M').sum().plot()
plt.title('Monthly Arrests')
plt.show()
#Weekly
arrest_yearly.resample('W').sum().plot()
plt.title('Weekly Arrests')
plt.show()


#handle closings
sys.stdout = orig_stdout
outfile.close()
mydb.close()
