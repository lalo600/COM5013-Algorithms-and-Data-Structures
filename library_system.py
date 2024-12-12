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


# Example Usage
if __name__ == "__main__":
    # Create and use the library catalog
    catalog = LibraryCatalog()
    catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    print(catalog.search_book(1))

    # Create and manage borrowing records
    records = BorrowingRecords()
    records.add_record(101, 1)
    print(records.get_user_records(101))


