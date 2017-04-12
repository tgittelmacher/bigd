#!/usr/bin/env

import pandas as pd
from pandas import read_csv

crimes = read_csv('../data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')

print(type(crimes))
crimes = crimes.iloc[:, 3: ]
print(crimes.head())
