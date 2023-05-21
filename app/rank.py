from db import *

def search(key, min, max):
    while (min <= max):
        if key < max:
            return min
        else:
            return search(key, max, max + 10) 

# this function returns a 2D array 
# 2 columns and 11 rows for each decade (1910s-2010s). Will be passed into google line chart
def crashes_by_decade():
    data_array = [ [0] * 2 for i in range(11) ]
    for i in range(11):
        data_array[i][0] = 1910 + (i*10)

    dates = get_all("date")
    # print(dates)
    row = 0
    for i in dates:
        # cuts the date to just the year
        year = int(i[-4:])
        # matches the year with the decade it falls in
        decade = search(year, 1910, 1920)
        # increments the decade's plane crash count by 1 in the array
        for i in range(11):
            if data_array[i][0] == decade:
                data_array[i][1] += 1

    return data_array 
    

# print(crashes_by_decade())


#create a dict with all operators
def blank_by_operator(category):
    return null

