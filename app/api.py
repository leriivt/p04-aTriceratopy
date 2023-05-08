import requests
import json

def get_key():
    with open('../key_positionstack.txt', 'r') as file:
        key = file.read()
    return key

def initialize():
    return requests.get(f"http://api.positionstack.com/v1/forward?access_key={get_key()}")

def forward_geocode(address):
    return requests.get(f"http://api.positionstack.com/v1/forward?access_key={get_key()}&query={address}")


def reverse_geocode(latitude, longitude):
    return requests.get(f"http://api.positionstack.com/v1/reverse?access_key={get_key()}&query={latitude},{longitude}")

# 
# print( forward_geocode("1600 Pennsylvania Ave NW, Washington DC"))    