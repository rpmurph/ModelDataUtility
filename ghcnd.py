import os
import sys
import urllib2

token = 'kRLKxqYZQangpfoIdxleMkHfINRvCXdC'
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
#url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/stations/COOP:010008"

class GHCND:
    
    def __init__(self, base_url, user_token):
        self.token = user_token
        self.url = base_url
    
def make_request():
    
    #
    MyUtility = GHCND(url, token)
    
    #
    request_headers = { 'token': MyUtility.token }
    
    #
    request = urllib2.Request(MyUtility.url, headers=request_headers)
    contents = urllib2.urlopen(request).read()
    
    return contents
