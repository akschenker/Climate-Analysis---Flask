# climate-analysis

In this assignment, we were tasked with analyzing Hawaii climate data from a local SQL database. This included precipitation and temperature data from several weather stations in the area.

These results were then added to a local Flask app with several API endpoints. These endpoints include:

* /api/v1.0/precipitation
* /api/v1.0/stations
* /api/v1.0/tobs
* /api/v1.0/&lt;start&gt; where start is a date in YYYY-MM-DD format
* /api/v1.0/&lt;start&gt;/&lt;end&gt; where start and end are dates in YYYY-MM-DD format

## Prerequisites

Climate data was obtained from `Resources/hawaii.sqlite`, which is required for the `climate_analysis.ipynb` notebook to run. The notebook must be run in Jupyter Notebook within an Anaconda3 virtual environment.

For `climate_app.py` to run, the Python Flask library must be installed. The app can be run through Terminal.

## Built With

* Jupyter Notebook
* SQLAlchemy
* Flask
* Python

## Authors

* Arley Schenker
