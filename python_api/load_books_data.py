import json
import redis

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)

with open("python_api/books.json", "r") as f:
    books_data = json.load(f)

for book in books_data:
    book_id = book.get("id")
    book_title = book.get("title")
    book_author = book.get("author")
    book_rating = book.get("rating")

    book_data = {"title": book_title, "author": book_author, "rating": book_rating}

    redis_client.hmset(f"book:{book_id}", book_data)
