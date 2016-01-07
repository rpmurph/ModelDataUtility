#!c:/Users/RYAN/Anaconda/python.exe
import sys
from json import loads
from shapely.geometry import Point, mapping
from fiona import collection
from fiona.crs import from_epsg

def write_shapefile(the_points):
    
    #
    the_points_parsed = json.loads(the_points)
    the_points_parsed = the_points_parsed['results']
    
    #
    station_schema = { 'geometry': 'Point', 
    
                        'properties': { 
                        
                            'ELEV': 'str',
                            'MINDATE': 'str', 
                            'MAXDATE': 'str', 
                            'LAT': 'str', 
                            'STANAME': 'str', 
                            'PCTCOV': 'str',
                            'STAID': 'str',
                            'ELEVUNIT': 'str',
                            'LNG': 'str',
                        } 
                        
                    }
    
    #
    with collection('some.shp', 'w', driver='ESRI Shapefile', schema=station_schema, crs=from_epsg(4326)) as output:
        for record in the_points_parsed:
            
            #
            point = Point(float(record['longitude']), float(record['latitude']))
            output.write({
                
                'properties': {
                    'ELEV':  record['elevation'], 
                    'MINDATE': record['mindate'], 
                    'MAXDATE': record['maxdate'], 
                    'LAT': record['latitude'], 
                    'STANAME': record['name'], 
                    'PCTCOV': record['datacoverage'], 
                    'STAID': record['id'], 
                    'ELEVUNIT': record['elevationUnit'], 
                    'LNG': record['longitude']
                },
            
                'geometry': mapping(point)
            
            })
            
if __name__ == '__main__':
    write_shapefile()