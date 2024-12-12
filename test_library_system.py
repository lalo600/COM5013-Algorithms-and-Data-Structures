from library_system import BookCatalog, LoanRecords

def test_book_catalog():
    catalog = BookCatalog()
    catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    assert catalog.find_book(1)["title"] == "1984"
    catalog.delete_book(1)
    assert catalog.find_book(1) == "Book not available"
