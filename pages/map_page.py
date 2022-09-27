import os

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html

from functions.widgets.navbar import Navbar
from functions.widgets.sidebar import Sidebar

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
us_cities = us_cities.query("State in ['New York', 'Ohio']")

fig = px.line_mapbox(us_cities, lat="lat", lon="lon", color="State",
                     # width=3200,
                     # height=1024,
                     )

fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4, mapbox_center_lat=41,
                  margin={"r": 0, "t": 0, "l": 0, "b": 0},
                  showlegend=False
                  )

sidebar_ = Sidebar()
navbar_ = Navbar()

layout = html.Div(children=[
    # html.Div(
    #     children=dbc.Input(type='text', #className='input_search',
    #                        placeholder='Search...', required=True),
    #     className='searsh'
    # ),
    sidebar_.layout,
    dbc.Row(navbar_.layout, ),
    dcc.Graph(id="mapa",
              figure=fig,
              className='box'
              ),
    # html.Div(className='box stack-top',
    #          style={'background': 'blue'})
],
    # style={'overflow': 'hidden',
    #        },
    # className="container"
)

dash.register_page(os.path.basename(__file__),
                   name=os.path.basename(__file__).strip('.py'),
                   path='/',
                   layout=layout)

dash.register_page(os.path.basename(__file__),
                   name=os.path.basename(__file__).strip('.py'),
                   path='/configuration',
                   layout=layout)
