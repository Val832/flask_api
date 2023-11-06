from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'objet SQLAlchemy qui sera utilisé comme ORM pour interagir avec la base de données.
db = SQLAlchemy()

# Fonction pour créer et configurer l'application Flask.
def create_app():
    
    # Création d'une instance de l'application Flask.
    app = Flask(__name__)
    
    # Chemin d'accès au fichier de configuration. 
    # On utilise les chemins relatifs pour trouver le fichier 'config.py'.
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.py')

    # Application de la configuration à l'application Flask à partir du fichier 'config.py'.
    app.config.from_pyfile(config_path)

    # Affichage de la sortie de la méthode 'app.config.from_pyfile', 
    # qui devrait être 'None' car la méthode ne retourne pas de valeur.
    print(app.config.from_pyfile(config_path))
    
    # Initialisation de l'extension SQLAlchemy avec l'application Flask.
    db.init_app(app)

    # Création d'un contexte d'application qui permet d'utiliser 'current_app' 
    # et 'g' sans avoir à passer par un endpoint.
    with app.app_context():
        
        # Importation des routes et modèles de l'application.
        from .routes import main_routes  # Importation du module des routes principales.
        from app.models import models     # Importation du module des modèles de la base de données.

        # Enregistrement du Blueprint 'main_bp' qui contient les routes principales de l'application.
        app.register_blueprint(main_routes.main_bp)

    # Retourne l'instance de l'application Flask configurée.
    return app




