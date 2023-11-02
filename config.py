import os
from dotenv import load_dotenv

# Chargement des vars d'environnement hors du code source 
load_dotenv()

# Configuration de l'API avec les variables d'environnement
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
