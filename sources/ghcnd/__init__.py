from requests import get

token = 'kRLKxqYZQangpfoIdxleMkHfINRvCXdC'
url = r"http://www.ncdc.noaa.gov/cdo-web/api/v2/stations"

class Data:
    ''' creates new instance of the data class '''
    
    def __init__(self):
        pass

class Stations:
    ''' creates new instance of the stations class '''
    
    def __init__(self, base_url, user_token):
        self.token = user_token
        self.url = base_url
    
def download_stations(bbox='17.5000,-65.1000,18.5000,-64.1000', datasetid='GHCND', limit=1000):
    ''' downloads stations from the specified dataset withint he bounding box '''
    
    #
    MyUtility = Stations(url, token)
    header = { 'token': MyUtility.token }
    payload = { 'extent' : bbox, 'limit': limit, 'datasetid': datasetid }
    
    #
    r = get(url, headers=header, params=payload)
    return r.text
