import pandas as pd
import folium as fl

vol_data = pd.read_csv("Volcanoes_USA.txt")

def colorPicker(elev):
    if elev >= 3200:
        return "red"
    elif elev >= 2500 and elev < 3200:
        return "lightred"
    elif elev >= 1800 and elev < 2500:
        return "blue"
    else:
        return "lightgreen"

map = fl.Map(location = [37.0902, -95.7129], tiles = "OpenStreetMap", zoom_start = 6)
fgv = fl.FeatureGroup(name = "Volcanoes")

for num in range(len(vol_data)):
    popup_data =  vol_data.iloc[num]["NAME"] + "\n" +  str(vol_data.iloc[num]["ELEV"])  + " m"
    fgv.add_child(fl.Marker(location = [vol_data.iloc[num]['LAT'], vol_data.iloc[num]['LON']], popup = popup_data, icon = fl.Icon(colorPicker(vol_data.iloc[num]["ELEV"]))))

fgp = fl.FeatureGroup(name = "Population")
fgp.add_child(fl.GeoJson(data = (open('world.json', 'r', encoding='utf-8-sig').read()), style_function = lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fl.LayerControl())
map.save("Map.html")
