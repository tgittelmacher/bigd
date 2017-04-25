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
outfile = open('../output/homicides.txt', 'w')
sys.stdout = outfile

#Pulling data
crimes = read_csv('../data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')
crimes2 = read_csv('../data/Chicago_Crimes_2001_to_2004.csv', index_col='Date', error_bad_lines=False)
crimes3 = read_csv('../data/Chicago_Crimes_2005_to_2007.csv', index_col='Date', error_bad_lines=False)
crimes4 = read_csv('../data/Chicago_Crimes_2008_to_2011.csv', index_col='Date', error_bad_lines=False)

crimes2 = crimes2.append(crimes3)
crimes2 = crimes2.append(crimes4)
crimes = crimes2.append(crimes)

crimes = crimes.iloc[:, 3: ]

crimes.index = pd.to_datetime(crimes.index)
crimes.sort_index(inplace=True)
print(crimes.shape)
print(crimes.head())
types = crimes[['Primary Type']]
print(types.head())
