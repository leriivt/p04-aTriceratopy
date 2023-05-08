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

def populate_crashes():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db 
    c = db.cursor() #creates db cursor to execute and fetch      

    with open(CSV_FILE, "r") as crashes_csv:
        reader = csv.DictReader(crashes_csv)
        id = 0
        for row in reader:
            c.execute("INSERT INTO crashes VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, row['Date'], row['Location'], row['Operator'], row['Route'], row['AC Type'], row['Aboard Crew'], row['Aboard Passangers'], row['Fatalities'], row['Ground'], row['Summary']))
    
    db.commit()
    db.close()
