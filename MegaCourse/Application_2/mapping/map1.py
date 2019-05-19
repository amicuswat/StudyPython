import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(el):
    color=" "
    if el <= 2000:
        color = "green"
    elif el <= 3000:
        color = "orange"
    else :
        color = "red"
    return color

map = folium.Map(location = [38.5, -109], zoom_start = 6)
fg = folium.FeatureGroup(name = "My map")

for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(str(el) +" m", parse_html = True, max_width =  "90px"), icon = folium.Icon(color="green")))
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
#    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))
    fg.add_child(folium.CircleMarker(location=[lt, ln], fill = True, fill_color = color_producer(el), radius = 5, popup=folium.Popup(iframe), fill_opacity = 0.7, color = color_producer(el)))

map.add_child(fg)

map.save("Map1.html")
