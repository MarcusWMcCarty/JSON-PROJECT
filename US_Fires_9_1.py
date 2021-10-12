import json

infile = open('US_fires_9_1.json', 'r')
outfile = open('Readable_Fire_Data_9_1', 'w')

fire_data = json.load(infile)

json.dump(fire_data,outfile, indent=4)


lats = []
lons = []
brightness = []


for fire in fire_data:
    lat = fire["latitude"]
    lon = fire["longitude"]
    bright = fire["brightness"]
    if bright > 450:
        brightness.append(bright)
        lats.append(lat)
        lons.append(lon)


print(lats)
print()
print(lons)
print()
print(brightness)

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker': {
        'size':[.05*b for b in brightness],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='UsFires_9_1.html')



