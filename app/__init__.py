from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/summary')
def summary():
  return "nop"

@app.route('/data')
def data():
  return "this is data"


if __name__ == '__main__':
  app.debug = True
  app.run()
