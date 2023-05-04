import requests
import json

def forward_geocode(address){
    return requests.get(f"https://api.positionstack.com/v1/forward
    ? access_key = YOUR_ACCESS_KEY
    & query = {address}")
}

def reverse_geocode(latitude, longitude){
    return requests.get(f"https://api.positionstack.com/v1/reverse
    ? access_key = YOUR_ACCESS_KEY
    & query = {latitude},{longitude}")
}