import json
import redis

from client.redis import CacheClient

cache = CacheClient()

with open("static/books.json", "r") as f:
    books_data = json.load(f)

for book in books_data:
    book_id = book.get("id")
    book_title = book.get("title")
    book_author = book.get("author")
    book_rating = book.get("rating")

    book_data = {"title": book_title, "author": book_author, "rating": book_rating}

    cache.set(f"book:{book_id}", book_data)
