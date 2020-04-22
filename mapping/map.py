import folium
map = folium.Map([7.5629, 4.5200], title = "Osun State")

coordinates = {"Ile-Ife":[[7.4905, 4.5521], 'green'], "Ilesa":[[7.6396, 4.7588], 'blue'], "Osogbo":[[7.7827, 4.5418], 'red'], "Iwo": [[7.6292, 4.1872], 'gray']}

fg = folium.FeatureGroup(name="My Map")
for cities in coordinates:
    fg.add_child(folium.Marker(location = coordinates[cities][0], popup = cities, icon = folium.Icon(coordinates[cities][1])))

map.add_child(fg)
#map.add_child(folium.Marker(location = [7.4905, 4.5521], popup = "Ile-Ife", icon = folium.Icon("green")))

#folium.Marker([7.4905, 4.5521], popup = "IleIfe").add_to(map)
map.save("Map1.html")
