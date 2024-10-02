import os

class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(24)

    #database configuration
    DATABASE_USER = 'inventory_manager_admin'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'localhost'
    DATABASE_NAME = 'inventory_management_db'
    DATABASE_PORT = 5432
    
    #SQLALCHEMY configuration
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'filename': 'flask_app.log',
                'formatter': 'default'
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file']
        }
    }