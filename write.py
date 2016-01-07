#!c:/Users/RYAN/Anaconda/python.exe
import sys
import json
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
                        
                            'elevation': 'str',
                            'mindate': 'str', 
                            'maxdate': 'str', 
                            'latitude': 'str', 
                            'name': 'str', 
                            'datacoverage': 'str',
                            'id': 'str',
                            'elevationUnit': 'str',
                            'longitude': 'str',
                        } 
                            
                    }

    #
    with collection('some.shp', 'w', driver='ESRI Shapefile', schema=station_schema, crs=from_epsg(3857)) as output:
        for record in the_points_parsed:
            
            #
            point = Point(float(record['longitude']), float(record['latitude']))
            output.write({
                
                'properties': {
                    'elevation':  record['elevation'], 
                    'mindate': record['mindate'], 
                    'maxdate': record['maxdate'], 
                    'latitude': record['latitude'], 
                    'name': record['name'], 
                    'datacoverage': record['datacoverage'], 
                    'id': record['id'], 
                    'elevationUnit': record['elevationUnit'], 
                    'longitude': record['longitude']
                },
            
                'geometry': mapping(point)
            
            })
            
if __name__ == '__main__':
    write_shapefile()