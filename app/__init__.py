from flask import Flask, render_template
from db import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/summary')
def summary():
  return "nop"

@app.route('/coordinates_data')
def data():
  store_coordinate(1,1,1)
  return get_all_coordinates()

#@app.route('/crashes_data')



if __name__ == '__main__':
  app.debug = True
  app.run()
  reset_database()
  populate_crashes()
  populate_all_coordinates()
  route_to_stops()
