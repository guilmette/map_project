import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def colors(i):
        if i < 1000:
            return "green"
        elif i >= 1000 and i < 3000:
            return "orange"
        else:
            return "red"

map = folium.Map(location=[46.16,-84.36], zoom_start=6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="volcanoes")



for lt,ln,n,el in zip(lat, lon, name,elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+"m.  " + n,fill_color=colors(el), color = "grey",fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map2.html")
