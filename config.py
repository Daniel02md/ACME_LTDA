import os

class __Config(object):
    SECRET = "df353b383b79b16beb71dd3d6585243f9e78892ad0fd8ed5e45ec3f0c58b761d"
    TEMPLATE_FOLDER =  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None


class Development(__Config):
    TESTING = False
    DEBUG = True
    IP_HOST = "0.0.0.0"
    PORT_HOST = "5000"
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URI")
    
class Testing(__Config):
    pass

class Production(__Config):
    TESTING = False
    DEBUG = False
    IP_HOST = "localhost"
    PORT_HOST = "5000"
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URI")
    pass


app_config = {
    "development": Development(),
    "testing": Testing(),
    "production": Production()
}


app_activate = os.getenv("FLASK_ENV")
if not app_activate:
    app_activate = "development"




