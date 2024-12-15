# models/article.py

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @staticmethod
    def create_article(conn, title, content, author_id, magazine_id):
        """Create an article in the database."""
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (title, content, author_id, magazine_id))
        conn.commit()
        return cursor.lastrowid

    @staticmethod
    def get_all_articles(conn):
        """Get all articles from the database."""
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]
