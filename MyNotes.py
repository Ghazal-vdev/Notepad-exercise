# A minimal notepad with SQLite (OOP)

import sqlite3


class NoteManager():
    def __init__(self, db_path='notes.db'):
        self.db_path = db_path
        self._setup_database()

    def _get_connection(self): # a helpfunc which connects us to database in moment
        return sqlite3.connect(self.db_path)

    def _setup_database(self):
        with self._get_connection() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS notes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT NOT NULL,
                        created_at TEXT DEFAULT (datetime('now'))
                        )
                        """)
    

    def add_note(self, content):
        content = content.strip()
        if not content:
            return False, "Cannot save an empty note."
        try:
            with self._get_connection() as conn:
                conn.execute("INSERT INTO notes (text) VALUES(?)", (content,))
            return True, "Saved.✅"
        except Exception as e:
            return False, f"Error: {e}"
    

    def delete_note(self, note_id):
        try:
            with self._get_connection() as conn:
                cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            if cursor.rowcount == 0:
              return False, "No note found with this id."
            return True, f"Note {note_id} deleted successfully.✅"
        except Exception as e:
            return False, f"Error: {e}"

    def edit_note(self, note_id, new_text):
        new_text = new_text.strip()
        if not new_text:
            return False, "Note can not be empty."
        
        try:
            with self._get_connection() as conn:
                cursor = conn.execute("UPDATE notes SET text = ? WHERE id = ?",(new_text, note_id))
            if cursor.rowcount == 0:
                return False, "No note found with this id."
            return True, "Edited.✅"
        except Exception as e:
            return False, f"Error: {e}"


    def show_notes(self):
        with self._get_connection() as conn:
            return conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
        
    def search_note(self, search_term):
        term = search_term.strip().lower()
        if not term:
            return self.show_notes()
        try:
            with self._get_connection() as conn:
                return conn.execute("SELECT id, text, created_at FROM notes WHERE text LIKE ?",\
                                    (f"%{term}%",)).fetchall()
        except Exception:
            return []

