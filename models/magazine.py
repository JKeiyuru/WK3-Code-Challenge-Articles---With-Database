# models/magazine.py

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @staticmethod
    def create_magazine(conn, name, category):
        """Create a magazine in the database."""
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all_magazines(conn):
        """Get all magazines from the database."""
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines]
