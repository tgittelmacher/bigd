~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Welcome to a little Python big data experimentation!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The dataset contains about 2GB of crime data collected between 2001 and 2017. The .CSV files would normally be directly loaded via python, but migration into an MySQL database was done
for experimental/learning/masochistic purposes. Some data analysis using pandas, seaborn, gmaps, and matplotlib is done and the results are collected for analysis and visualization.

Enjoy!

To run:
1) Ensure you have python 2.X, pandas, seaborn, matplotlib, gmaps, and mysql-connector installed
2) Change scripts/config.py file to point your database **ENSURE YOU DO NOT HAVE AN EXISTING TABLE WITH THE NAME LISTED IN config.py FILE, IT WILL BE DROPPED!**
3) Download <a href="https://www.kaggle.com/currie32/crimes-in-chicago/downloads/crimes-in-chicago.zip">this zip file</a>, and extract 4 .csv files inside to a new folder called /data/ on the project root (provided empty for reference)
4) Run scripts/dbinit.py (may take a while, this is normal)
5) Run scripts/analysis.py
