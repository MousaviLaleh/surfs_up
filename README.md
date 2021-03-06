# Surf's Up
Advanced Data Storage and Retrieval

## Project Overview
Analyze the temperature trends for the months of June and December in Oahu, in order to evaluate the year-round sustainability of a surf and ice cream shop business, using Python, Pandas, SQLite and SQLAlchemy for this analysis.

### Resources
- Softwares : [Python](https://www.python.org/downloads/windows/),&nbsp; [Pandas](https://www.anaconda.com/products/distribution),&nbsp; [SQLite](https://docs.python.org/3/library/sqlite3.html),&nbsp; [SQLAlchemy](https://docs.sqlalchemy.org/en/14/intro.html),&nbsp; [Flask](https://flask.palletsprojects.com/en/2.1.x/tutorial/database/)
- Data : [hawaii.sqlite](hawaii.sqlite)
- Analysis : [SurfsUp_Challenge.ipynb](SurfsUp_Challenge.ipynb)


## Results
This project was consist of two technical analysis:

**- The Summary Statistics for June**<br/>
Using Python, Pandas functions and methods, and SQLAlchemy, we did filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. We then converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics.
<br/>

![june.png](images/june.png)
<br/>
<br/>

**- The Summary Statistics for December** <br/>
Taking the same steps for month of December, we did use Python, Pandas functions and methods, and SQLAlchemy, filtered the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December, then converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics.
<br/>

![december.png](images/december.png)


## Summary
The temperatures in December are slightly lower than June but suitable for a surf and ice cream shop business, and the most active station for June and December can be find by following analysis: <br/>
- session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()
- session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 12).all()

<br/>
 

