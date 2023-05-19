from db import *

#these functions return strings in csv layout for graphs in d3.js
def blank_by_date(category):
    csv_string = ""
    # x-axis
    dates = get_all("date")
    # y-axis
    categories = get_all(category)
    

    

#create a dict with all operators
def blank_by_operator(category):
    return null
