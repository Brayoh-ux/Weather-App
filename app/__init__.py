from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options,Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
bootstrap=Bootstrap()
migrate = Migrate()

def create_app(config_name):

    app=Flask(__name__)


    app.config.from_object(Config)
    # app.config.from_object(config_options[config_name])
    # app.config[Config]
   

    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .requests import configure_request
    configure_request(app)

    return app