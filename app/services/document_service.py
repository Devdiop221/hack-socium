from fastapi import APIRouter, UploadFile, HTTPException
from app.utils import file_utils, text_utils
from app.models.document_model import Document
from app.database import db
def process_document(file: UploadFile):
    # Sauvegarder le fichier
    filepath = file_utils.save_file(file)

    # Extraire le texte en fonction du type de fichier
    if file.filename.endswith('.pdf'):
        text = file_utils.extract_text_from_pdf(filepath)
    elif file.filename.endswith('.txt'):
        text = file_utils.extract_text_from_txt(filepath)
    else:
        raise ValueError("Format de fichier non supporté")

    # Traiter le texte
    anonymized_text = text_utils.anonymize(text)
    label_doc = text_utils.label(anonymized_text)
    summary_doc = text_utils.summarize(anonymized_text)
    description_doc = text_utils.describe(anonymized_text)

    # Enregistrer les résultats dans la base de données
    document = Document(
        filename=file.filename,
        anonymized_text=anonymized_text,
        label=label_doc,
        summary=summary_doc,
        description=description_doc
    )


    # Supprimer le fichier après traitement
    file_utils.delete_file(filepath)

    return {
        "id": document.id,
        "filename": document.filename,
        "anonymized_text": document.anonymized_text,
        "label": document.label,
        "summary": document.summary,
        "description": document.description,
        "created_at": document.created_at
    }

## Comment transformer process_document en un endpoint qui recupere un fichier et le renvoie au fonction qui extrait le text(spacy,tesseract...) et
##

