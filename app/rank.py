from db import *
from array import array

def search(key, min, max):
    while (min <= max):
        if key < max:
            return min
        else:
            return search(key, max, max + 10) 

# this function returns a 2D array 
# 2 columns and 11 rows for each decade (1910s-2010s). Will be passed into google line chart
def crashes_by_decade():
    data_array = [ [0] * 2 for i in range(12) ]
    data_array[0][0] = "Decade"
    data_array[0][1] = "Crashes"
    for i in range(1,12):
        data_array[i][0] = 1910 + ((i-1)*10)

    dates = get_all("date")
    # print(dates)
    row = 0
    for i in dates:
        # cuts the date to just the year
        year = int(i[0][-4:])
        # matches the year with the decade it falls in
        decade = search(year, 1910, 1920)
        # increments the decade's plane crash count by 1 in the array
        for i in range(1,12):
            if data_array[i][0] == decade:
                data_array[i][1] += 1
    # print(type(data_array)) 
    return data_array

# print(crashes_by_decade())
# [['Decade', 'Crashes'], [1910, 33], [1920, 182], [1930, 357], [1940, 578], [1950, 649], [1960, 636], [1970, 612], [1980, 552], [1990, 631], [2000, 506], [2010, 231]]

def most_fatalities():
    ids = get_all("id")
    dates = get_all("date")
    fatalities = get_all("fatalities")

    length = len(ids)
    data_array = [ [0] * 3 for i in range(length) ]

    i = 0
    while i < length:
        data_array[i][0] = ids[i][0]
        data_array[i][1] = int(dates[i][0][-4:])
        data_array[i][2] = fatalities[i][0]
        i += 1
    
    # print(data_array)
    return data_array

most_fatalities()

