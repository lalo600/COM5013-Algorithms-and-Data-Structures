class BookCatalog:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, details):
        self.books[book_id] = details

    def delete_book(self, book_id):
        self.books.pop(book_id, "Book not found")

    def find_book(self, book_id):
        return self.books.get(book_id, "Book not available")
