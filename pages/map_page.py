import os

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html


us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
us_cities = us_cities.query("State in ['New York', 'Ohio']")

fig = px.line_mapbox(us_cities, lat="lat", lon="lon", color="State",
                     width=1600,
                     height=1600)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat=41,
                  margin={"r": 0, "t": 0, "l": 0, "b": 0})

layout = dcc.Graph(id="mapa",
              figure=fig,
              # config={
              #     'displaylogo': False,
                  # 'modeBarButtonsToRemove': ['select2d', 'lasso2d']
              # }
              )


dash.register_page(os.path.basename(__file__),
                   name=os.path.basename(__file__).strip('.py'),
                   path='/',
                   layout=layout)
