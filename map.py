import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv("data/Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elev = data['ELEV']

#print(elev)

def color_change(elev):
    if(elev<1000):
        return 'green'
    elif(1000<=elev<3000):
        return 'orange'
    else:
        return 'red'

m = folium.Map(location=[37.296933,-121.9574983],zoom_start = 8,tiles = "CartoDB dark_matter")
folium.CircleMarker(location = [37.4074687,-122.086669],popup = "Google HQ",radius=9,fill_color = "tomato",color="gray",fill_opacity=0.9).add_to(m)

for lat,lon,elev in zip(lat,lon,elev):
    folium.Marker(location=[lat,lon],popup=str(elev)+"m",icon = folium.Icon(color = color_change(elev))).add_to(m)

m.save("map.html")
