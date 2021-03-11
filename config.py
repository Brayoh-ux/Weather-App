import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'fhvnbmgmgkh9ttolslso'
    WEATHER_API_KEY=os.environ.get('WEATHER_API_KEY') or 'a778d9642410a11ed2cbd17c20c246bc'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///weather.db'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG=True


config_options={
    'development': DevConfig,
    'production': ProdConfig
}