import os
import sys
import requests

token = 'kRLKxqYZQangpfoIdxleMkHfINRvCXdC'
url = r"http://www.ncdc.noaa.gov/cdo-web/api/v2/stations"

class G:
    
    def __init__(self, base_url, user_token):
        self.token = user_token
        self.url = base_url
    
def make_request():
    
    #
    MyUtility = G(url, token)
    
    #
    header = { 'token': MyUtility.token }
    payload = { 'extent' : '17.5000,-65.1000,18.5000,-64.1000', 'limit': 100, 'datasetid': 'GHCND'}
    
    #
    r = requests.get(url, headers=header, params=payload)
    return r.text
