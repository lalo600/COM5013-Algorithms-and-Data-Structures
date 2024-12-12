class BookCatalog:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, details):
        self.books[book_id] = details

    def delete_book(self, book_id):
        self.books.pop(book_id, "Book not found")

    def find_book(self, book_id):
        return self.books.get(book_id, "Book not available")


class LoanRecords:
    def __init__(self):
        self.loans = []

    def add_loan(self, user_id, book_id):
        self.loans.append({"user_id": user_id, "book_id": book_id})

    def remove_loan(self, user_id, book_id):
        self.loans = [loan for loan in self.loans if not (loan["user_id"] == user_id and loan["book_id"] == book_id)]

    def list_user_loans(self, user_id):
        return [loan for loan in self.loans if loan["user_id"] == user_id]


