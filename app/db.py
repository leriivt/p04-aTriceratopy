#functions regarding the database

import sqlite3
DB_FILE = "airplane.db"


def reset_database():
    db = sqlite3.connect(DB_FILE) #open if file exists, if not it will create a new db
    c = db.cursor() #creates db cursor to execute and fetch           

    c.execute("DROP TABLE IF EXISTS crashes;")
    c.execute("DROP TABLE IF EXISTS coordinates;")

    #users table stores the username and password
    c.execute("CREATE TABLE IF NOT EXISTS crashes(id INTEGER, date STRING, time STRING, location STRING, operator STRING, takeoff STRING, destination STRING, model STRING, crew INTEGER, passengers INTEGER, fatalities INTEGER, ground INTEGER, summary STRING);")
    c.execute("CREATE TABLE IF NOT EXISTS coordinates(id INTEGER, longitude FLOAT, latitude FLOAT);")

    db.commit()
    db.close()
