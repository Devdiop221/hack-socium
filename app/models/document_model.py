from app.database import get_db

class Document:
    def __init__(self, id, filename, anonymized_text, label, summary, description, created_at):
        self.id = id
        self.filename = filename
        self.anonymized_text = anonymized_text
        self.label = label
        self.summary = summary
        self.description = description
        self.created_at = created_at

    def __repr__(self):
        return f"<Document {self.filename}>"

    @staticmethod
    def get_all():
        conn = get_db()
        documents = conn.execute("SELECT * FROM documents").fetchall()
        return [Document(**doc) for doc in documents]

    @staticmethod
    def get_by_id(doc_id):
        conn = get_db()
        doc = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
        return Document(**doc) if doc else None

    @staticmethod
    def create(filename, anonymized_text, label, summary, description):
        conn = get_db()
        conn.execute("""
            INSERT INTO documents (filename, anonymized_text, label, summary, description)
            VALUES (?, ?, ?, ?, ?)
        """, (filename, anonymized_text, label, summary, description))
        conn.commit()

    @staticmethod
    def delete(doc_id):
        conn = get_db()
        conn.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
        conn.commit()