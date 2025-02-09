import sqlite3
from datetime import datetime
from fastapi import FastAPI

# Database file path (change it to your desired location)
db = "test.db"

# Function to get a database connection
def get_db():
    """Get a connection to the SQLite database."""
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row  # This allows access to columns by name
    return conn

# Function to initialize the database (create tables)
def init_db(app: FastAPI):
    """Initialize the database (create tables if they don't exist)."""
    @app.on_event("startup")
    def startup():
        with get_db() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    anonymized_text TEXT NOT NULL,
                    label TEXT NOT NULL,
                    summary TEXT NOT NULL,
                    description TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()