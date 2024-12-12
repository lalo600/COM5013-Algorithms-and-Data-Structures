from library_system import LibraryCatalog, BorrowingRecords

def test_library_catalog():
   catalog = LibraryCatalog()
   catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    assert catalog.search_book(1)["title"] == "1984"
    catalog.remove_book(1)
    assert catalog.search_book(1) == "Book not found"

