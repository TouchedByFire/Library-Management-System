# Library Management System - README

This is a simple Flask-based Library Management System. It allows users to add books, search for books, borrow and return books, and view overdue books.

## Getting Started

To run this application locally, follow these steps:

### Prerequisites

Make sure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   ```

2. Navigate to the project directory.

   ```bash
   cd library-management-system
   ```

3. Create a virtual environment to isolate dependencies.

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Ensure you are in the project directory and the virtual environment is activated.

2. Run the Flask application.

   ```bash
   python app.py
   ```

3. Open your web browser and go to [http://localhost:8000](http://localhost:8000).

## Usage

1. Access the home page to view all available books.

2. Use the "Add Book" page to add new books to the library.

3. Use the "Search Books" page to search for books by title, author, or publication year.

4. Borrow and return books using the respective endpoints.

5. View overdue books on the "Overdue Books" page.

## Endpoints

- Home Page: [http://localhost:8000/](http://localhost:8000/)
- Add Book Form: [http://localhost:8000/add_book_form](http://localhost:8000/add_book_form)
- Search Books: [http://localhost:8000/search_books?query={your_query}](http://localhost:8000/search_books?query={your_query})
- Borrow Book: [http://localhost:8000/borrow_book](http://localhost:8000/borrow_book)
- Return Book: [http://localhost:8000/return_book](http://localhost:8000/return_book)
- Overdue Books: [http://localhost:8000/overdue_books](http://localhost:8000/overdue_books)

## Testing

This application includes a set of pytest tests. Run the tests with the following command:

```bash
pytest
```

## Using POSTMAN

You can interact with the API endpoints using [Postman](https://www.postman.com/).

### Adding a Book

- **Method**: POST
- **URL**: [http://localhost:8000/add_book](http://localhost:8000/add_book)
- **Body (form-data or JSON)**:
  - title: New Book
  - author: New Author
  - isbn: 0987654321
  - publication_year: 2023

### Searching for Books

- **Method**: GET
- **URL**: [http://localhost:8000/search_books?query={your_query}](http://localhost:8000/search_books?query={your_query})

### Borrowing a Book

- **Method**: POST
- **URL**: [http://localhost:8000/borrow_book](http://localhost:8000/borrow_book)
- **Body (JSON)**:
  - isbn: 1234567890

### Returning a Book

- **Method**: POST
- **URL**: [http://localhost:8000/return_book](http://localhost:8000/return_book)
- **Body (JSON)**:
  - isbn: 1234567890

### Viewing Overdue Books

- **Method**: GET
- **URL**: [http://localhost:8000/overdue_books](http://localhost:8000/overdue_books)

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push the branch to your fork.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize and enhance the application based on your needs!
