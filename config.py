class Config:
    SECRET_KEY = 'AHA'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'web'
    MYSQL_DATABASE_HOST = 'localhost'

  

config = {"development": DevelopmentConfig}
