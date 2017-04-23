#!/usr/bin/env

import pandas as pd
from pandas import read_csv
import csv
import mysql.connector
import config
from config import db, table_name


mydb = mysql.connector.connect(user=db['user'],
    password=db['password'],
    host=db['host'],
    db=db['db'])
cursor = mydb.cursor()


sql = "select * from " + table_name

crimes = pd.read_sql(sql, mydb)
crimes = crimes.iloc[:, 3: ]
print(crimes.head())





mydb.close()
