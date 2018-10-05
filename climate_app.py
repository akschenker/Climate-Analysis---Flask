from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import numpy as np

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# Flask
app = Flask(__name__)

# Create routes
@app.route("/")
def welcome():
    return """
    Welcome to the Hawaii Climate API!
    Available endpoints:
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    """

@app.route("/api/v1.0/precipitation")
def precip():
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= "2016-08-23").\
    filter(Measurement.date <= "2017-08-23").all()

    results_dict = []
    for row in results:
        date_dict = {}
        date_dict[row.date] = row.prcp
        results_dict.append(date_dict)

    return jsonify(results_dict)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    results_list = list(np.ravel(results))

    return jsonify(results_list)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.tobs).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date <= "2017-08-23").all()

    results_list = list(np.ravel(results))

    return jsonify(results_list)



@app.route("/api/v1.0/<start>")
def start_date(start):
    end_date = session.query(func.max(Measurement.date)).all()[0][0]
    temps = calc_temps(start, end_date)
    temps_list = list(np.ravel(temps))
    return jsonify(temps_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    temps = calc_temps(start, end)
    temps_list = list(np.ravel(temps))
    return jsonify(temps_list)

if __name__ == '__main__':
    app.run(debug=True)