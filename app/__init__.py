from flask import Flask, render_template
from db import *
import api

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('map.html')

@app.route('/trends')
def trends():
  return render_template("trends.html")

@app.route('/summary')
def summary():
  return "nop"

@app.route('/coordinates_data')
def data():
  store_coordinate(1,1,1)
  return get_all_coordinates()
  #return "nop"

@app.route('/mapboxapikey')
def mapbox():
    return api.get_key_mp();

@app.route('/csv_test')
def csv():
  return "Country,Value\nUnited States,12394\nRussia,6148"

#@app.route('/crashes_data')



if __name__ == '__main__':
  app.debug = True
  app.run()
  reset_database()
  populate_crashes()
  populate_all_coordinates()
  route_to_stops()
