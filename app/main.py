from fastapi import FastAPI
from app.config import Config
from app.routes.document_routes import init_routes
from app.database import init_db
import os

def create_app():
    app = FastAPI()

    # Initialiser la base de données
    init_db(app)

    # Créer le dossier d'upload s'il n'existe pas
    upload_folder = Config.UPLOAD_FOLDER
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Initialiser les routes
    init_routes(app)

    return app

app = create_app()

# Pour lancer l'application avec Uvicorn :
# uvicorn main:app --reload