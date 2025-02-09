import os

class Config:
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf'}
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_clé_secrète_tres_secrete'

    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///documents.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


