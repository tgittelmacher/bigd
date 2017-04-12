#!/usr/bin/env

import csv
import mysql.connector
import config
from config import db, table_name

mydb = mysql.connector.connect(user=db['user'],
    password=db['password'],
    host=db['host'],
    db=db['db'])
cursor = mydb.cursor()

print('BEGINNING DATA IMPORT')

print('Reading data...')
csv_data = csv.reader(file('../data/Chicago_Crimes_2001_to_2004.csv'))

print('Dumping old data if exists...')
cursor.execute("DROP TABLE IF EXISTS " + table_name)

print('Creating new table...')
cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(caseNum NUMERIC, ID NUMERIC, Case_Number VARCHAR(20), Crime_Date VARCHAR(40), Block VARCHAR(40), IUCR VARCHAR(20), Primary_Type VARCHAR(40), Description VARCHAR(200), Location_Description VARCHAR(50), Arrest VARCHAR(10), Domestic VARCHAR(10), Beat NUMERIC, District NUMERIC, Ward NUMERIC, Community_Area NUMERIC, FBI_Code VARCHAR(10), X_Coordinate DOUBLE, Y_Coordinate DOUBLE, Year INT, Updated_On VARCHAR(40), Latitude DOUBLE, Longitude DOUBLE, Location VARCHAR(50))" )

print('Migrating data to database...')

isFirstLine = True;
for row in csv_data:
    if isFirstLine:
        isFirstLine = False
        continue
    sql = "INSERT into " + table_name + "(caseNum, ID, Case_Number, Crime_Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate, Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = [row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]]
    for i in range(22):
        if not vals[i]:
            vals[i] = '0'
    cursor.execute(sql, tuple(vals))
#close the connection to the database.
mydb.commit()

print('Data migration successful!')
cursor.close()
