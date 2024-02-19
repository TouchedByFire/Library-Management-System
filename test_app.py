import pytest
import json
import datetime
from flask import Flask
from app import app, library, Book

# Fixture to set up a test client with the Flask app in testing mode
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Reset the library before each test and add a test book
    library.books = []
    library.add_book(Book("Test Book", "Test Author", "1234567890", 2022))

    yield client

# Test case for adding a book through the '/add_book' endpoint
def test_add_book(client):
    response = client.post('/add_book', data={'title': 'New Book', 'author': 'New Author', 'isbn': '0987654321', 'publication_year': '2023'})
    assert response.status_code == 302  # Expecting a redirect after adding a book
    assert len(library.books) == 2  # Ensure there are two books in the library now

# Test case for searching books through the '/search_books' endpoint
def test_search_books(client):
    response = client.get('/search_books?query=Test')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1  # Expecting only one book in the library with 'Test' in title/author

# Test case for borrowing a book through the '/borrow_book' endpoint
def test_borrow_book(client):
    response = client.post('/borrow_book', json={'isbn': '1234567890'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Book borrowed successfully"

# Test case for returning a book through the '/return_book' endpoint
def test_return_book(client):
    # Add a book and try to return it without borrowing
    test_book = {
        'title': 'Test Book',
        'author': 'Test Author',
        'isbn': '1234567890',
        'publication_year': 2022
    }

    client.post('/add_book', json=test_book)

    # Try to return the book without borrowing it
    response = client.post('/return_book', json={'isbn': '1234567890'})
    result = json.loads(response.get_data(as_text=True))

    # Verify that the result indicates the book is not available for returning
    assert result['message'] == 'Book not available for returning'

# Test case for retrieving overdue books through the '/overdue_books' endpoint
def test_overdue_books(client):
    # Add a book, borrow it to make it overdue, and call the 'overdue_books' endpoint
    test_book = {
        'title': 'Test Book',
        'author': 'Test Author',
        'isbn': '1234567890',
        'publication_year': 2022
    }

    client.post('/add_book', json=test_book)
    client.post('/borrow_book', json={'isbn': '1234567890'})

    # Make sure there is at least one second difference to ensure it's overdue
    library.books[0].due_date = datetime.datetime.now() - datetime.timedelta(seconds=1)

    # Call the 'overdue_books' endpoint
    response = client.get('/overdue_books')
    result = json.loads(response.get_data(as_text=True))

    # Verify that the result contains the overdue book
    assert len(result) == 1
    assert result[0]['title'] == 'Test Book'
    assert result[0]['author'] == 'Test Author'
    assert result[0]['isbn'] == '1234567890'
    assert 'due_date' in result[0]
