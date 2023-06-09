from app import create_app
from config import app_config, app_activate


config = app_config[app_activate]
config.APP = create_app()

app = config.APP

if __name__ == "__main__":
    app.run(host=config.IP_HOST, port=config.PORT_HOST, debug=config.DEBUG)