# app.py

from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()

    # Create an author and get their id
    author_id = Author.create_author(conn, author_name)

    # Create a magazine and get its id
    magazine_id = Magazine.create_magazine(conn, magazine_name, magazine_category)

    # Create an article
    Article.create_article(conn, article_title, article_content, author_id, magazine_id)

    conn.commit()

    # Query the database for inserted records.
    authors = Author.get_all_authors(conn)
    magazines = Magazine.get_all_magazines(conn)
    articles = Article.get_all_articles(conn)

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(magazine)

    print("\nAuthors:")
    for author in authors:
        print(author)

    print("\nArticles:")
    for article in articles:
        print(article)

if __name__ == "__main__":
    main()
