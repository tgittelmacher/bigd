~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Welcome to a little Python big data experimentation!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The dataset contains about 2GB of crime data collected between 2001 and 2017. The .CSV files would normally be directly loaded via python, but migration into an MySQL database was done
for experimental/learning/masochistic purposes. Some data analysis using pandas is done and the results are collected for analysis and visualization.

Enjoy!

To run:
1) Ensure you have python 2.X, pandas, and mysql-connector installed
2) Change scripts/config.py file to point your database
3) Download https://www.kaggle.com/currie32/crimes-in-chicago/downloads/crimes-in-chicago.zip, extract the 4 .csv files inside to a new folder called /data/ on the project root
4) Run dbinit.py (may take a while)
5) Run analysis.py
