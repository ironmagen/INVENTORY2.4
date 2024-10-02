from flask_sqlalchemy import SQLAlchemy
import logging
from app.config import Config


db = SQLAlchemy()


def init_db(app):
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{Config.DATABASE_USER}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_HOST}:{Config.DATABASE_PORT}/{Config.DATABASE_NAME}"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        
        # Create tables
        with app.app_context():
            db.create_all()
        
        logging.info("Database initialized successfully.")
    
    except Exception as e:
        logging.error(f"Database initialization failed: {str(e)}")


def get_db():
    """
    Return the initialized database instance.
    """
    return db