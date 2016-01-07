import os
import sys
import requests

token = 'kRLKxqYZQangpfoIdxleMkHfINRvCXdC'
url = r"http://www.ncdc.noaa.gov/cdo-web/api/v2/stations"

class GHCND:
    
    def __init__(self, base_url, user_token):
        self.token = user_token
        self.url = base_url
    
def make_request():
    
    #
    MyUtility = GHCND(url, token)
    
    #
    header = { 'token': MyUtility.token }
    payload = { 'extent' : '17.5000,-65.1000,18.5000,-64.1000', 'limit': 100 }
    #payload = { 'extent' : '47.5204,-122.2047,47.6139,-122.1065', 'limit': 100 }
    #'-64.7259063198959979,18.3433448527116809,-64.7138323663953088,18.3574645858839034'
    
    

    #
    r = requests.get(url, headers=header, params=payload)
    return r.text
