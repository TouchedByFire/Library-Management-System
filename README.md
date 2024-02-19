Library Management System - README

This is a simple Flask-based Library Management System. It allows users to add books, search for books, borrow and return books, and view overdue books.
Getting Started

To run this application locally, follow these steps:
Prerequisites

Make sure you have Python installed on your system. You can download it from Python's official website.
Installation

    Clone the repository to your local machine.

    bash

git clone https://github.com/your-username/library-management-system.git

Navigate to the project directory.

bash

cd library-management-system

Create a virtual environment to isolate dependencies.

bash

python -m venv venv

Activate the virtual environment.

    On Windows:

    bash

.\venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the required dependencies.

bash

    pip install -r requirements.txt

Running the Application

    Ensure you are in the project directory and the virtual environment is activated.

    Run the Flask application.

    bash

    python app.py

    Open your web browser and go to http://localhost:8000.

Usage

    Access the home page to view all available books.

    Use the "Add Book" page to add new books to the library.

    Use the "Search Books" page to search for books by title, author, or publication year.

    Borrow and return books using the respective endpoints.

    View overdue books on the "Overdue Books" page.

Endpoints

    Home Page: http://localhost:8000/
    Add Book Form: http://localhost:8000/add_book_form
    Search Books: http://localhost:8000/search_books?query={your_query}
    Borrow Book: http://localhost:8000/borrow_book
    Return Book: http://localhost:8000/return_book
    Overdue Books: http://localhost:8000/overdue_books

Testing

This application includes a set of pytest tests. Run the tests with the following command:

bash

pytest

Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Commit your changes.
    Push the branch to your fork.
    Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize and enhance the application based on your needs!
