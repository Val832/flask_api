from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')
    app.config.from_pyfile(config_path)
    print(app.config.from_pyfile(config_path))
    db.init_app(app)
    with app.app_context():
        
        from .routes import main_routes
        from app.models import models

        #Enregistrer les Blueprints
        app.register_blueprint(main_routes.main_bp)

    return app

