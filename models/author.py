# models/author.py

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    @staticmethod
    def create_author(conn, name):
        """Create an author in the database."""
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all_authors(conn):
        """Get all authors from the database."""
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        return [Author(author['id'], author['name']) for author in authors]
