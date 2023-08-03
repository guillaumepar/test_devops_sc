from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    # Check if the book already exists
    book_data = redis_client.hgetall(f'book:{id}')
    if not book_data:
        return jsonify({'error': 'Book not found'}), 404

    book_info = {key.decode('utf-8'): value.decode('utf-8') for key, value in book_data.items()}
    return jsonify(book_info)

@app.route('/book/<int:id>', methods=['POST'])
def create_book(id):
    # Check if the book already exists
    if redis_client.exists(f'book:{id}'):
        return jsonify({'error': 'Book already exists'}), 409

    book_data = request.json

    # Store the product data
    redis_client.hmset(f'book:{id}', book_data)

    return jsonify({'message': 'Book created successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
