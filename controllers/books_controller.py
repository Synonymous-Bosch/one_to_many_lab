from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repo, author_repo   
from models.book import Book    
from models.author import Author

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET 'books'
@books_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("books/index.html", all_books=books)

# # DELETE
# # DELETE '/tasks/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_task(id):
    book_repo.delete(id)
    return redirect('/books')


# NEW
# GET '/books/new'
# Return an HTML form to the browser
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    return render_template("books/new.html")

# # CREATE
# # POST '/tasks'
# # Receive data from the form to insert into the database
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form['title']
    author_name = request.form['author']
    genre = request.form['genre']

    author = author_repo.find_by_name(author_name)
    if author == None:
        author = Author(author_name)
        author = author_repo.save(author)


    book = Book(title, author, genre)
    book_repo.save(book)
    return redirect('/books')
    

# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>", methods=["GET"])
def show_task(id):
    book=book_repo.select(id)
    return render_template('books/show.html', book=book)

# # EDIT
# # GET '/tasks/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template('books/edit.html', book=book, all_authors=authors)

# # UPDATE
# # PUT '/tasks/<id>'
@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']

    author = author_repo.select(author_id)
    book = Book(title, author, genre, id)

    book_repo.update(book)
    return redirect('/books')


