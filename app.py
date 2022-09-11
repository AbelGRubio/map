import dash
import dash_bootstrap_components as dbc
from flask import Flask

import configuration.reader_configuration_system as SysConfig

if __name__ == '__main__':
    # Setup the Flask server
    SysConfig.SERVER = Flask(__name__)

    SysConfig.SERVER.config.update(
        SECRET_KEY=SysConfig.SECRET,
    )

    SysConfig.APP = dash.Dash(
        name=__name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME],
        meta_tags=[{"name": "viewport", "content": "width=device-width"}, ],
        server=SysConfig.SERVER)

    SysConfig.APP.config['suppress_callback_exceptions'] = True
    SysConfig.APP.title = SysConfig.NAME_SERVER

    SysConfig.LOGIN_MANAGER.init_app(SysConfig.SERVER)

    from pages.map_page import layout

    SysConfig.APP.layout = layout

    SysConfig.APP.run_server(debug=False,
                             host=SysConfig.IP_HOST,
                             port=SysConfig.PORT_HOST)
