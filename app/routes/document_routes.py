from app.services.document_service import process_document
from fastapi import APIRouter, HTTPException, FastAPI,UploadFile
from app.models.document_model import Document

router = APIRouter()

@router.get("/documents/")
def read_documents():
    documents = Document.get_all()
    return documents

@router.get("/documents/{doc_id}")
def read_document(doc_id: int):
    document = Document.get_by_id(doc_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.post("/documents/")
def create_document(filename: str, anonymized_text: str, label: str, summary: str, description: str):
    Document.create(filename, anonymized_text, label, summary, description)
    return {"message": "Document created successfully"}

@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int):
    Document.delete(doc_id)
    return {"message": "Document deleted successfully"}

""" @router.post("/processes/")
def process_file(file: UploadFile):
    return process_document(file) """

def init_routes(app: FastAPI):
    app.include_router(router)