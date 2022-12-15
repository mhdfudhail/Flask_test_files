from flask import Flask, render_template
import folium
import os
import json
import pathlib as pl

app = Flask(__name__)

###########--Get-Data--#############
def get_data():
    pass


###########-------------############

start_coords = (10.1, 76.9)

@app.route('/')
def index():

    # path = os.path.join(pl.Path.cwd(),'./map/', 'sampleMap.geojson') 
    pathjson = r"C:\Users\mhmdf\Documents\C-Watch\myApp\map\sampleMap.geojson"
    map = folium.Map(location=start_coords)

    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )

    folium.GeoJson(pathjson, name="geojson").add_to(map)
    folium.GeoJsonTooltip(fields=["name"]).add_to(folium_map)
    # folium.LayerControl().add_to(folium_map)
    folium_map.save('templates/map.html')
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':

    app.run(debug=True)

