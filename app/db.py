#functions regarding the database

import sqlite3
import csv
#from api import *

DB_FILE = "airplane.db"
CSV_FILE = "Airplane_Crashes_and_Fatalities_Since_1908_20190820105639.csv"


def reset_database():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db
    c = db.cursor() #creates db cursor to execute and fetch           

    c.execute("DROP TABLE IF EXISTS crashes;")
    c.execute("DROP TABLE IF EXISTS coordinates;")
    c.execute("DROP TABLE IF EXISTS rankings;")

    #crashes table stores crash info (has 13 cols)
    c.execute("CREATE TABLE IF NOT EXISTS crashes(id INTEGER, date STRING, time STRING, location STRING, operator STRING, route STRING, model STRING, crew INTEGER, passengers INTEGER, fatalities INTEGER, ground INTEGER, summary STRING);")
    c.execute("CREATE TABLE IF NOT EXISTS coordinates(id INTEGER, longitude FLOAT, latitude FLOAT);")
    c.execute("CREATE TABLE IF NOT EXISTS rankings(item STRING, category STRING, rank INTEGER, number_of INTEGER);")

    db.commit()
    db.close()

#populates the crashes table
def populate_crashes():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch      

    with open(CSV_FILE, "r") as crashes_csv:
        reader = csv.DictReader(crashes_csv)
        id = 0
        for row in reader:
            c.execute("INSERT INTO crashes VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, row['Date'], row['Time'],row['Location'], row['Operator'], row['Route'], row['AC Type'], row['Aboard Crew'], row['Aboard Passangers'], row['Fatalities'], row['Ground'], row['Summary']))
            id += 1
    
    db.commit()
    db.close()

def populate_all_coordinates():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch   

    c.execute("SELECT location FROM crashes")
    locations = c.fetchall()
    #print(locations)
    id = 0
    latitude = 0
    longitude = 0

    for row in locations:
        #store_coordinate(id, latitude, longitude)
        data = (id, latitude, longitude)
        c.execute("INSERT INTO coordinates VALUES(?, ?, ?)", data)
        id += 1
        latitude += 1
        longitude += 1
    
    db.commit()
    db.close()

#takes in all routes and returns a dictionary of id keys with values of a list of stops, null if no stops or unknown
def route_to_stops():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT route FROM crashes")
    routes = c.fetchall()
    all_routes = {}
    id = 0

    for row in routes:
        route = row[0]
        #print(route)
        if route == null or route.count(' - ') == 0:
            all_routes[id] = null
        else:
            stops = route.split(' - ')
            all_routes[id] = stops
        id += 1
    
    return all_routes
        
        

    


def get_all_coordinates():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch  

    c.execute("SELECT * FROM coordinates")
    everything = c.fetchall()

    return everything

def get_all_crashes():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch  

    c.execute("SELECT * FROM crashes")
    everything = c.fetchall()

    return everything


#get functions for crashes table start vvv
def get_date(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT date FROM crashes WHERE id=?", (plane_id,))
    date = c.fetchone()

    db.close()

    return date

def get_time(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT time FROM crashes WHERE id=?", (plane_id,))
    time = c.fetchone()

    db.close()

    return time

def get_location(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT location FROM crashes WHERE id=?", (plane_id,))
    location = c.fetchone()

    db.close()

    return location

def get_operator(plate_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT operator FROM crashes WHERE id=?", (plane_id,))
    operator = c.fetchone()

    db.close()

    return operator

def get_model(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT model FROM crashes WHERE id=?", (plane_id,))
    model = c.fetchone()

    db.close()

    return model

def get_crew(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT crew FROM crashes WHERE id=?", (plane_id,))
    crew = c.fetchone()

    db.close()

    return crew

def get_passengers(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT passengers FROM crashes WHERE id=?", (plane_id,))
    passengers = c.fetchone()

    db.close()

    return passengers

def get_fatalities(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT fatalities FROM crashes WHERE id=?", (plane_id,))
    fatalities = c.fetchone()

    db.close()

    return fatalities

def get_ground(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT ground FROM crashes WHERE id=?", (plane_id,))
    ground = c.fetchone()

    db.close()

    return ground
#get functions for crashes table end ^^^

def store_coordinate(plane_id, longitude, latitude):
    data = (plane_id, longitude, latitude)
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("INSERT INTO coordinates VALUES(?, ?, ?)", data)
    db.commit()
    db.close()

def store_ranking(item, category, rank, number_of):
    data = (item, category, rank, number_of)
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("INSERT INTO coordinates VALUES(?, ?, ?, ?)", data)
    db.commit()
    db.close()

