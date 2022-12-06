import pandas as pd
import folium

world = folium.Map(
    zoom_start=2,
    location=[13.133932434766733, 16.103938729508073])
world

world.save('/Users/albamolina/files/python_final/first_world_map.html')
