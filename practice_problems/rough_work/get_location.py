# import requests
# import json
lat_1 = '19.218330'
lon_1 = '72.978088'
lat_2 = '19.075983'
lon_2 = '72.877655'
# # call the OSMR API
# r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")
# # then you load the response using the json libray
# # by default you get only one alternative so you access 0-th element of the `routes`
# routes = json.loads(r.content)
# route_1 = routes.get("routes")[0]
# print(route_1)


import geopy.distance

start_coordinates = (lat_1, lon_1)
end_coordinates = (lat_2, lon_2)

distance_travelled = geopy.distance.geodesic(start_coordinates, end_coordinates).km

print(round(distance_travelled, 2))

