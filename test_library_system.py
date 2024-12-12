from library_system import LibraryCatalog, BorrowingRecords

def test_library_catalog():
   catalog = LibraryCatalog()
   catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    assert catalog.search_book(1)["title"] == "1984"
    catalog.remove_book(1)
    assert catalog.search_book(1) == "Book not found"

def test_borrowing_records():
    records = BorrowingRecords()
    records.add_record(101, 1)
    assert len(records.get_user_records(101)) == 1
    records.remove_record(101, 1)
    assert len(records.get_user_records(101)) == 0

if __name__ == "__main__":
    test_library_catalog()
    test_borrowing_records()
    print("All tests passed!")
