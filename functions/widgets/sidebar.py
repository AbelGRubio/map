import configparser
import datetime

import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

from configuration import LOGGER
from functions.functions import define_id


class Sidebar:
    def __init__(self, path: str = None):
        self._path = None
        if path is None:
            self._path = r'assets\parser_widgets\sidebar.ini'
        else:
            self._path = path
        self._sidebar_dict = None
        self.layout = None
        self._version = 'v1.0.0'
        self.id_version_timestamp = define_id('menu', 'sidebar')
        self.id_interval = define_id('menu', 'interval')

        if self._read_sidebar_ini():
            self._create_sidebar()

    def _read_sidebar_ini(self):
        """
        read the .ini file in the path indicate
        :return:
        """
        try:
            sidebar_config = configparser.ConfigParser()
            sidebar_config.read(self._path)
        except Exception as e:
            LOGGER.debug('Could not find one of the config files! Mssg: {}'.format(e))
            return False

        sidebar_ = dict(sidebar_config)
        self._sidebar_dict = {}
        for page in sidebar_.keys():
            if page != 'DEFAULT':
                self._sidebar_dict[page] = (dict(sidebar_[page]))

        return True

    def _datetime_now(self) -> str:
        return datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    def _add_callback(self):
        @callback(Output(self.id_version_timestamp, 'children'),
                  Input(self.id_interval, 'n_intervals'))
        def update_timestamp(n):
            print('Entra aqui la {} vez'.format(n))
            layout = [self._version,
                      html.Br(),
                      self._datetime_now()]
            return layout

    def _create_sidebar(self):
        self.layout = html.Div(
            [
                html.Div(
                    [
                        html.Img(src=r'assets/imgs/maps_app.png', style={"width": "3rem"}),
                        html.H5("Maps app", className='sidebar_title'),
                    ],
                    className="sidebar-header",
                ),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            [html.I(className=self._sidebar_dict[i]['icon']),
                             html.Span(self._sidebar_dict[i]['name'])],
                            href=self._sidebar_dict[i]['ref'],
                            active=self._sidebar_dict[i]['active'],
                        ) for i in self._sidebar_dict
                    ],
                    vertical=True,
                    pills=True,
                ),
                html.Div(children=self._version,
                         className='text_sidebar_footer1',
                         id=self.id_version_timestamp),
                dcc.Interval(
                    id=self.id_interval,
                    interval=1000,
                    n_intervals=0
                )
            ],
            className="sidebar",
        )

        self._add_callback()

        return self.layout
