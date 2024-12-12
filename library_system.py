class LibraryCatalog:
    def __init__(self):
        # Initialize an empty dictionary to store book details
        self.books = {}

    def add_book(self, book_id, book_details):
        # Add or update a book's information in the catalog
        self.books[book_id] = book_details

    def remove_book(self, book_id):
        # Remove a book from the catalog if it exists
        self.books.pop(book_id, None)

    def search_book(self, book_id):
        # Retrieve book details by ID, or return a default message if not found
        return self.books.get(book_id, "Book not found")


class BorrowingRecords:
    def __init__(self):
        # Initialize an empty list to store borrowing records
        self.borrow_records = []

    def add_record(self, user_id, book_id):
        # Add a new borrowing record
        self.borrow_records.append({"user_id": user_id, "book_id": book_id})

    def remove_record(self, user_id, book_id):
        # Remove a specific borrowing record by matching user ID and book ID
        self.borrow_records = [
            record for record in self.borrow_records
            if not (record["user_id"] == user_id and record["book_id"] == book_id)
        ]

    def get_user_records(self, user_id):
        # Get all borrowing records for a specific user
        return [record for record in self.borrow_records if record["user_id"] == user_id]
