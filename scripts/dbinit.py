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
cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(caseNum NUMERIC, ID NUMERIC, Case_Number VARCHAR(200), Crime_Date VARCHAR(200), Block VARCHAR(200), IUCR VARCHAR(200), Primary_Type VARCHAR(200), Description VARCHAR(200), Location_Description VARCHAR(200), Arrest VARCHAR(200), Domestic VARCHAR(200), Beat VARCHAR(200), District VARCHAR(200), Ward VARCHAR(200), Community_Area VARCHAR(200), FBI_Code VARCHAR(200), X_Coordinate VARCHAR(200), Y_Coordinate VARCHAR(200), Year VARCHAR(200), Updated_On VARCHAR(200), Latitude VARCHAR(200), Longitude VARCHAR(200), Location VARCHAR(200))" )

print('Migrating 2001-2017 data to database...')

missedRows = 0

#2001 to 2004
isFirstLine = True;
for row in csv_data:
    if isFirstLine:
        isFirstLine = False
        continue
    try:
        sql = "INSERT into " + table_name + "(caseNum, ID, Case_Number, Crime_Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate, Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = [row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]]
        for i in range(22):
            if not vals[i]:
                vals[i] = '0'
        cursor.execute(sql, tuple(vals))
    except:
        missedRows += 1
print("2001-2004 data completed...")
print("Missed " + str(missedRows) + " rows.")
missedRows = 0

#2005-2007
csv_data = csv.reader(file('../data/Chicago_Crimes_2005_to_2007.csv'))
isFirstLine = True;
for row in csv_data:
    if isFirstLine:
        isFirstLine = False
        continue
    try :
        sql = "INSERT into " + table_name + "(caseNum, ID, Case_Number, Crime_Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate, Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = [row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]]
        for i in range(22):
            if not vals[i]:
                vals[i] = '0'
        cursor.execute(sql, tuple(vals))
    except:
        missedRows += 1
print("2005-2007 data completed...")
print("Missed " + str(missedRows) + " rows.")
missedRows = 0

#2008-2011
csv_data = csv.reader(file('../data/Chicago_Crimes_2008_to_2011.csv'))
isFirstLine = True;
for row in csv_data:
    if isFirstLine:
        isFirstLine = False
        continue
    try:
        sql = "INSERT into " + table_name + "(caseNum, ID, Case_Number, Crime_Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate, Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = [row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]]
        for i in range(22):
            if not vals[i]:
                vals[i] = '0'
        cursor.execute(sql, tuple(vals))
    except:
        missedRows += 1
print("2008-20011 data completed...")
print("Missed " + str(missedRows) + " rows.")
missedRows = 0

#2012-2017
csv_data = csv.reader(file('../data/Chicago_Crimes_2012_to_2017.csv'))
isFirstLine = True;
for row in csv_data:
    if isFirstLine:
        isFirstLine = False
        continue
    try:
        sql = "INSERT into " + table_name + "(caseNum, ID, Case_Number, Crime_Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate, Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        vals = [row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]]
        for i in range(22):
            if not vals[i]:
                vals[i] = '0'
        cursor.execute(sql, tuple(vals))
    except:
        missedRows += 1
print("20012-2017 data completed...")
print("Missed " + str(missedRows) + " rows.")


#close the connection to the database.
mydb.commit()

print('Data migration successful!')
cursor.close()
