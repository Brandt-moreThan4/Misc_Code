"""creates a pretty cool world map with earthquakes marked off"""

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = r'data\eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['title'])

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
        },
    }]


my_layout = Layout(title='Global Quakers')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')

#readable_file = r'data\readable_eq_data.json'
#with open(readable_file,'w') as f:
#    json.dump(all_eq_data,f, indent = 4)
