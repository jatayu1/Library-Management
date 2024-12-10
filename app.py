from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

books = {}
members = {}

@app.route('/books', methods=['GET'])
def fetch_books():
    title = request.args.get('title')
    author_name = request.args.get('author')

    filtered_books = []
    for book in books.values():
        author_id = book['author']
        author = members.get(author_id)
        if author:
            if (not title or title.lower() in book['title'].lower()) and (not author_name or author_name.lower() in author['name'].lower()):
                enhanced_book = {
                    "id": book["id"],
                    "title": book["title"],
                    "content": book["content"],
                    "author": {
                        "id": author_id,
                        "name": author['name'],
                        "email": author['email']
                    }
                }
                filtered_books.append(enhanced_book)

    return jsonify(filtered_books), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('author') or not data.get('content'):
        return jsonify({"error": "title or author id or content not provided"}), 400
    
    flag = False
    for member in members.values():
        if (member["id"] == data['author']):
            flag = True
            break
    
    if flag :
        book_id = len(books) + 1
        book = {
            "id" : book_id,
            "title" : data['title'],
            "author" : data['author'],
            "content" : data['content'],
        }
        books[book_id] = book
        return jsonify(book), 201
    else:
        return jsonify({"error": "Author doesn't exist"}), 400

@app.route('/members', methods=['get'])
def fetch_member():    
    name = request.args.get('name')
    email = request.args.get('email')

    filtered_members = [
        member for member in members.values() if (not name or name.lower() in member['name'].lower()) and (not email or email.lower() in member['email'].lower())
    ]

    return jsonify(filtered_members), 201

@app.route('/members', methods=['POST'])
def add_member():    
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Name or email not provided"}), 400

    member_id = len(members) + 1
    member = {
        "id" : member_id,
        "name" : data['name'],
        "email" : data['email'],
    }
    members[member_id] = member
    return jsonify(member), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)