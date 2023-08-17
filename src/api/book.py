from flask import Flask, request, jsonify

from client.redis import CacheClient

app = Flask(__name__)

# Connect to Redis
cache = CacheClient()

@app.route('/book/<int:id>', methods=['GET'])
def get(id):
    # Check if the book already exists
    book = cache.get(f'book:{id}')
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book_info = {key.decode('utf-8'): value.decode('utf-8') for key, value in book.items()}
    return jsonify(book_info)

@app.route('/book/<int:id>', methods=['POST'])
def create(id):
    # Check if the book already exists
    if cache.exists(f'book:{id}'):
        return jsonify({'error': 'Book already exists'}), 409

    book = request.json

    # Store the product data
    cache.set(f'book:{id}', book)

    return jsonify({'message': 'Book created successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
