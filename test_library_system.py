# Testing Functions
def test_library_catalog():
    # Create a LibraryCatalog instance and test its functionality
    catalog = LibraryCatalog()
    catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    assert catalog.search_book(1)["title"] == "1984"
    catalog.remove_book(1)
    assert catalog.search_book(1) == "Book not found"

def test_borrowing_records():
    # Create a BorrowingRecords instance and test its functionality
    records = BorrowingRecords()
    records.add_record(101, 1)
    assert len(records.get_user_records(101)) == 1
    records.remove_record(101, 1)
    assert len(records.get_user_records(101)) == 0


# Example Usage
if __name__ == "__main__":
    # Run tests
    test_library_catalog()
    test_borrowing_records()
    print("All tests passed!")

    # Create and use the library catalog
    catalog = LibraryCatalog()
    catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    print(catalog.search_book(1))

    # Create and manage borrowing records
    records = BorrowingRecords()
    records.add_record(101, 1)
    print(records.get_user_records(101))
