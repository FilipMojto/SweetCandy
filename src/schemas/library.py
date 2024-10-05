import sqlite3

SCHEMA = """
	-- Create the 'authors' table
	CREATE TABLE IF NOT EXISTS authors (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username VARCHAR(255) UNIQUE NOT NULL
	);

	-- Create the 'genres' table
	CREATE TABLE IF NOT EXISTS genres (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(255) UNIQUE NOT NULL
	);

	-- Create the 'books' table
	CREATE TABLE IF NOT EXISTS books (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title VARCHAR(255) NOT NULL,
		ISBN VARCHAR(13) UNIQUE NOT NULL,
		publication_date DATE NOT NULL,  -- DATE type for year, month, and day
		page_count INTEGER NOT NULL,
		author_id INTEGER,
		FOREIGN KEY (author_id) REFERENCES authors(id)
	);

	-- Create the 'books_genres' table (many-to-many relationship between Book and Genre)
	CREATE TABLE IF NOT EXISTS books_genres (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		book_id INTEGER NOT NULL,
		genre_id INTEGER NOT NULL,
		FOREIGN KEY (book_id) REFERENCES Book(id),
		FOREIGN KEY (genre_id) REFERENCES Genre(id),
		UNIQUE (book_id, genre_id)  -- Ensure a book cannot be assigned the same genre more than once
	);
"""

def import_db_schema(conn: sqlite3.Connection):
	cur = conn.cursor()
	cur.execute(SCHEMA)
	


