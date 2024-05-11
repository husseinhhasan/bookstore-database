from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Cosmos DB configuration
cosmosdb_username = username here
cosmosdb_password = yourpassword here
cosmosdb_database = "BOOKSTORE"
cosmosdb_collection = "mycollection"

# Azure Cosmos DB MongoDB instance connection details
cosmosdb_uri = "mongodb://ain3003project:" + cosmosdb_password + "@ain3003project.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retryWrites=false"

# Create MongoDB client
client = MongoClient(cosmosdb_uri)

# Access the specific database
db = client[cosmosdb_database]

# Access the specific collection within the database
collection = db[cosmosdb_collection]

# Main page route - List all books
@app.route('/', methods=['GET'])
@app.route('/books', methods=['GET'])
def get_books():
    books = list(collection.find({}, {'title': 1, 'author': 1, 'coverPhoto': 1}))
    return render_template('index.html', books=books)

# Book detail page route
@app.route('/book/<book_id>', methods=['GET'])
def book_detail(book_id):
    book = collection.find_one({'_id': ObjectId(book_id)})
    return render_template('book_detail.html', book=book)

# Add a new document form
@app.route('/books/add', methods=['GET'])
def add_book_form():
    return render_template('add_book.html')

# POST - Add a new document
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.form.to_dict()  # Get data from the form
    # Construct the author dictionary
    author = {
        'firstName': new_book.pop('authorFirstName', ''),
        'lastName': new_book.pop('authorLastName', '')
    }
    new_book['author'] = author  # Add the author dictionary to the new_book

    # Construct the publisher dictionary
    publisher = {
        'name': new_book.pop('publisherName', '')
    }
    new_book['publisher'] = publisher  # Add the publisher dictionary to the new_book

    new_book['mykey'] = "mykey"  # Set the 'mykey' field to "mykey"
    collection.insert_one(new_book)  # Insert the new document
    return redirect(url_for('get_books'))  # Redirect back to the book list


# GET - Update a document form by ID
@app.route('/books/edit/<string:id>', methods=['GET'])
def update_book_form(id):
    book = collection.find_one({'_id': ObjectId(id)})
    return render_template('edit_book.html', book=book)

# POST - Update a document by ID
@app.route('/books/edit/<string:id>', methods=['POST'])
def update_book(id):
    book_data = request.form.to_dict()  # Get updated data from the form
    # Update the author dictionary
    author = {
        'firstName': book_data.pop('authorFirstName', ''),
        'lastName': book_data.pop('authorLastName', '')
    }
    book_data['author'] = author  # Update the author dictionary in book_data

    # Update the publisher dictionary
    publisher = {
        'name': book_data.pop('publisherName', '')
    }
    book_data['publisher'] = publisher  # Update the publisher dictionary in book_data

    book_data['mykey'] = "mykey"  # Ensure the 'mykey' field is set to "mykey"
    _id = ObjectId(id)  # Convert received id into ObjectId
    collection.update_one({'_id': _id}, {'$set': book_data})  # Update the document
    return redirect(url_for('get_books'))  # Redirect back to the book list


# GET - Delete confirmation for a document by ID
@app.route('/books/delete/<string:id>', methods=['GET'])
def delete_book_confirm(id):
    book = collection.find_one({'_id': ObjectId(id)})
    return render_template('delete_confirm.html', book=book)

# POST - Delete a document by ID
@app.route('/books/delete/<string:id>', methods=['POST'])
def delete_book(id):
    _id = ObjectId(id)  # Convert received id into ObjectId
    collection.delete_one({'_id': _id})  # Delete the document
    return redirect(url_for('get_books'))

if __name__ == '__main__':
    app.run(debug=True)
