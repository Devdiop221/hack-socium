import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from fastapi import UploadFile

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

async def save_file(file: UploadFile):
    filename = secure_filename(file.filename)
    filepath = os.path.join('../../uploads', filename)

    # Lire le contenu du fichier téléchargé
    with open(filepath, "wb") as f:
        content = await file.read()  # Lire le contenu du fichier
        f.write(content)  # Sauvegarder le contenu dans le fichier

    return filepath




def extract_text_from_pdf(filepath: str) -> str:
    text = ""
    with open(filepath, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()  # Extraire le texte de chaque page
    return text


def extract_text_from_txt(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
