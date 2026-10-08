# 📝 My Notepad

A simple notepad web app built with Python, Streamlit, and SQLite.

## Features
- Add new notes
- Edit existing notes
- Delete notes
- View all notes with creation time
- Search notes by keyword

## Tech Stack
- Python
- Streamlit (user interface)
- SQLite (database)
- Object-Oriented Programming (`NoteManager` class)

## Project Structure
```
app.py       # Streamlit user interface
MyNotes.py   # NoteManager class: all database operations
notes.db     # SQLite database (created automatically on first run)
```

## How to Run
1. Clone the repository:
```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
```
2. Install the requirements:
```

   pip install -r requirements.txt
```
3. Start the app:
```
   streamlit run app.py
```

## Screenshot
![App screenshot](screenshot.png)

## What I Practiced
- Separating the interface (`app.py`) from the logic (`MyNotes.py`)
- Basic CRUD operations with SQLite
- Using parameterized queries (`?`) instead of string formatting
- Building a simple interface with Streamlit
