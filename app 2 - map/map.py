import folium
import pandas
map = folium.Map(location=[49.201316, -116.601570], zoom_start=6, tiles="Stamen Terrain")

data=pandas.read_csv("volcanoes.txt ")
lat_list=list(data['LAT'])
lon_list=list(data['LON'])
elev_list=list(data['ELEV'])


fgv=folium.FeatureGroup(name='Volcanoes')

def color(height):
    if height < 1000:
        return 'green'
    elif height >= 1000 and height < 3000 :
        return 'orange'
    else:
        return 'red'


for lat,lon,elev in zip(lat_list,lon_list,elev_list):
    fgv.add_child(folium.CircleMarker(location=[lat,lon], radius=6, popup=str(elev) + 'm', fill_color=color(elev), color='grey', fill_opacity=0.7))

fgp=folium.FeatureGroup(name='Population')


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
print(type(map))
