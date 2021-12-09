from re import search
import flask
from flask import request, jsonify
import json
import books

books = books.booksList #List de livres importés de la variable bookList du fichier books.py
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books/name', methods=['GET'])
def api_bookName():       
    results = []
    for book in books:
        results.append(book["Title"])   
    return jsonify(results)

@app.route('/api/books/author', methods=['GET'])
def api_bookAuthor():       
    results = []
    for book in books:
        results.append(book["Author"])   
    return jsonify(results)

@app.route('/api/book/genre', methods=['GET'])
def api_bookGenre():       
    results = {"fiction,mathematics"}
    for book in books:
        results.add(book["Genre"])   
    return jsonify(list(results))


app.run()