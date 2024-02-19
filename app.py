from flask import Flask, redirect, request, jsonify, render_template
import datetime

app = Flask(__name__)

class Book:
    def __init__(self, title, author, isbn, publication_year):
        # Initialize Book attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = 'Available'
        self.due_date = None

class Library:
    def __init__(self):
        # Initialize Library with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a new book to the library
        self.books.append(book)

    def search_books(self, query):
        # Search for books based on title, author, or publication year
        results = []
        for book in self.books:
            if (query.lower() in book.title.lower()) or (query.lower() in book.author.lower()) or (query.lower() in str(book.publication_year)):
                results.append({
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'publication_year': book.publication_year,
                    'status': book.status
                })
        return results

    def borrow_book(self, isbn):
        # Borrow a book if it is available
        for book in self.books:
            if book.isbn == isbn and book.status == 'Available':
                book.status = 'Borrowed'
                book.due_date = datetime.datetime.now() + datetime.timedelta(days=14)  # Due date set to 14 days from now
                return True
        return False

    def return_book(self, isbn):
        # Return a borrowed book
        for book in self.books:
            if book.isbn == isbn and book.status == 'Borrowed':
                book.status = 'Available'
                book.due_date = None  # Reset due date when returned
                return True
        return False

    def get_overdue_books(self):
        # Get a list of overdue books
        overdue_books = []
        today = datetime.datetime.now()
        for book in self.books:
            if book.status == 'Borrowed' and book.due_date and book.due_date < today:
                overdue_books.append({
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'due_date': book.due_date.strftime('%Y-%m-%d')
                })
        return overdue_books

# Create a Library instance
library = Library()

# Add sample books to the library
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 1960))
library.add_book(Book("1984", "George Orwell", "9780451524935", 1949))

@app.route('/')
def homepage():
    # Display all books on the homepage
    all_books = []
    for book in library.books:
        all_books.append({
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'status': book.status
        })
    return render_template('index.html', books=all_books)

@app.route('/add_book_form', methods=['GET'])
def add_book_form():
    # Render the form to add a new book
    return render_template('add_book_form.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    # Add a new book to the library based on user input
    if request.content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form

    new_book = Book(data['title'], data['author'], data['isbn'], int(data['publication_year']))
    library.add_book(new_book)

    if request.content_type == 'application/json':
        return jsonify({"message": "Book added successfully"})
    else:
        return redirect('/')

@app.route('/search_books', methods=['GET'])
def search_books():
    # Search for books based on user input
    query = request.args.get('query')
    results = library.search_books(query)
    return jsonify(results)

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    # Borrow a book based on ISBN
    data = request.get_json()
    isbn = data['isbn']
    success = library.borrow_book(isbn)
    if success:
        return jsonify({"message": "Book borrowed successfully"})
    else:
        return jsonify({"message": "Book not available for borrowing"})

@app.route('/return_book', methods=['POST'])
def return_book():
    # Return a borrowed book based on ISBN
    data = request.get_json()
    isbn = data['isbn']
    success = library.return_book(isbn)
    if success:
        return jsonify({"message": "Book returned successfully"})
    else:
        return jsonify({"message": "Book not available for returning"})

@app.route('/overdue_books', methods=['GET'])
def overdue_books():
    # Get a list of overdue books
    overdue_books = library.get_overdue_books()
    return jsonify(overdue_books)

if __name__ == '__main__':
    # Run the Flask application on port 8000
    app.run(debug=False, port=8000)
