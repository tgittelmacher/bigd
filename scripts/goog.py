import gmplot
import pandas as pd
from pandas import read_csv
import csv
import math

#Pulling data
crimes = read_csv('../data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')
crimes2 = read_csv('../data/Chicago_Crimes_2001_to_2004.csv', index_col='Date', error_bad_lines=False)
crimes3 = read_csv('../data/Chicago_Crimes_2005_to_2007.csv', index_col='Date', error_bad_lines=False)
crimes4 = read_csv('../data/Chicago_Crimes_2008_to_2011.csv', index_col='Date', error_bad_lines=False)

crimes2 = crimes2.append(crimes3)
crimes2 = crimes2.append(crimes4)
crimes = crimes2.append(crimes)

#crimes = crimes.iloc[:, 3: ]
crimes = crimes.loc[(crimes['Primary Type'] == 'HOMICIDE') & (crimes['Latitude'] != '0') & (crimes['Latitude'] != 0)]

latitudes = [float(i) for i in crimes['Latitude'].tolist()]
latitudes = [x for x in latitudes if x > 0 or x < 0]
longitudes = [float(i) for i in crimes['Longitude'].tolist()]
longitudes = [x for x in longitudes if x > 0 or x < 0]
print(len(latitudes))

for i in range(2001, 2017) :
    year_homicides = crimes.loc[(crimes['Year'] == i)]
    print(len(year_homicides))
    lats = [float(x) for x in year_homicides['Latitude'].tolist()]
    lats = [x for x in lats if x > 0 or x < 0]
    longs = [float(x) for x in year_homicides['Longitude'].tolist()]
    longs = [x for x in longs if x > 0 or x < 0]
    gmap = gmplot.GoogleMapPlotter(41.8339037, -87.8722363, 11)
    gmap.heatmap(lats, longs)
    gmap.draw("../heatmaps/heatmap" + str(i) + ".html")

gmap = gmplot.GoogleMapPlotter(41.8339037, -87.8722363, 11)
gmap.heatmap(latitudes, longitudes)
gmap.draw("../heatmaps/heatmap2001-2017.html")
print('finished!')
