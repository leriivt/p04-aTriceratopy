import requests
import json

def get_key_bing():
    with open('./keys/key_bingMaps.txt', 'r') as file:
        key = file.read()
    return key

def get_key_mp():
    with open('../app/keys/key_mapbox.txt', 'r') as file:
        key = file.read()
    return key

    
#returns longitude and latitude in a string
def forward_geocode(location):
    res = requests.get(f"http://dev.virtualearth.net/REST/v1/Locations?query={location}&key={get_key_bing()}")
    json = res.json()
    #print(json)
    try:
        return json["resourceSets"][0]["resources"][0]["point"]["coordinates"]
    except:
        return [None, None]

print(forward_geocode("New York, New York"))
'''
def reverse_geocode(latitude, longitude):
    return requests.get(f"http://api.positionstack.com/v1/reverse?access_key={get_key()}&query={latitude},{longitude}")
'''
# print( forward_geocode("1600 Pennsylvania Ave NW, Washington DC"))    
