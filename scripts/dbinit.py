#!/home/goku/anaconda3/bin/python

import csv
import config
import mysql.connector

mydb = mysql.connector.connect(user=config[db].user,
    password=config[db].password,
    host=config[db].host,
    db=config[db].db)
cursor = mydb.cursor()

print('BEGINNING DATA IMPORT')

print('Reading data...')
csv_data = csv.reader(file('../data/chicago/Chicago_Crimes_2001_to_2004.csv'))

print('Dumping old data if exists...')
cursor.execute("DROP TABLE IF EXISTS " +config[table_name])

print('Creating new table...')
cursor.execute("CREATE TABLE IF NOT EXISTS " + config[table_name] + "(col1 type, col2 type)" )

print('Migrating data to database...')
for row in csv_data:

    sql = "INSERT into " + config[table_name] + "('col1', 'col2') VALUES(?, ?)"
    cursor.execute(sql, (row[0], row[1]))
#close the connection to the database.
mydb.commit()

print('Data migration successful!')
cursor.close()
