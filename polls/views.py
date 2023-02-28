from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from zeep import Client

import folium
import polyline
from folium.plugins import MarkerCluster
import pandas as pd
import json

# client = Client('http://192.168.167.21:8000/?wsdl')
# result1 = client.service.say_hello(
#     'Hi', 3)

# result2 = client.service.add(10, 20)

# result = str(result1) + str(result2)

import requests

body = {"coordinates":[[5.873988614136497, 45.64809643726083],[5.908335008392307, 45.67265149150438]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248ae8b2b8cd4f943509643db9544603784',
    'Content-Type': 'application/json; charset=utf-8'
}

{
    "bbox":[[8.8034,53.0756],[8.7834,53.0456]],
    "geojson":
        {"type":"Point","coordinates":[8.8034,53.0756]},
    "buffer":200
}

{"request":"pois","geometry":{"bbox":[[8.8034,53.0756],[8.7834,53.0456]],"geojson":{"type":"Point","coordinates":[8.8034,53.0756]},"buffer":200}}

# /route/v1/car/[{45.64054},{5.8712};{45.67452},{5.91606}]?steps=true&geometries=geojson

# /route/v1/car/{coordinates}?alternatives={true|false}&steps={true|false}&geometries={polyline|polyline6|geojson}&overview={full|simplified|false}&annotations={true|false}
# url = 'https://router.project-osrm.org/route/v1/driving/45.64065156855971,5.871094977724547;46.08548300818923,6.549487628404506;46.19339490626042,6.203223970603168'

# call = requests.post("https://api.openrouteservice.org/v2/directions/driving-car/geojson", headers=headers, json=body)
# call = requests.get(url)

def index(request):
    #Call API to find the city
    # call = requests.get("https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf6248ae8b2b8cd4f943509643db9544603784&text=Chambery&boundary.country=FR")

    
    #Call API to get the travel
    call = requests.post("https://api.openrouteservice.org/v2/directions/driving-car/geojson", headers=headers, json=body)

    print(call.status_code, call.reason)
    print(json.dumps(call.json(), indent=1))
    
    #Define coordinates of where we want to center our map
    boulder_coords = [45.64919040418908, 5.86433719433594]

    #Create the map
    my_map = folium.Map(location = boulder_coords, zoom_start = 13, tiles="cartodbpositron")

    folium.GeoJson(call.json(), name="geojson").add_to(my_map)
    
    folium.LayerControl().add_to(my_map)
    
    my_map.fit_bounds(my_map.get_bounds())
    
    #Display the map
    return HttpResponse(my_map._repr_html_())