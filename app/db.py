#functions regarding the database

import sqlite3
import csv

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
    c.execute("CREATE TABLE IF NOT EXISTS rankings(id INTEGER, date STRING, time STRING, location STRING, operator STRING, takeoff STRING, destination STRING, model STRING, crew INTEGER, passengers INTEGER, fatalities INTEGER, ground INTEGER, summary STRING);")

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
            c.execute("INSERT INTO crashes VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, row['Date'], row['Location'], row['Operator'], row['Route'], row['AC Type'], row['Aboard Crew'], row['Aboard Passangers'], row['Fatalities'], row['Ground'], row['Summary']))
            id += 1
    
    db.commit()
    db.close()

#get date of plane crash based on id
def getDate(plane_id):
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor()

    c.execute("SELECT date FROM crashes WHERE id=?", (plane_id,))
    date = c.fetchone()

    db.close()

    return date

def getTime(plane_id):
    return null

def getLocation(plane_id):
    return null

#How get database data to javascript?
# - javascript can talk to html
# - html can talk to python
# - python can talk to database