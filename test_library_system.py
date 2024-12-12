from library_system import BookCatalog, LoanRecords

def test_book_catalog():
    catalog = BookCatalog()
    catalog.add_book(1, {"title": "1984", "author": "George Orwell"})
    assert catalog.find_book(1)["title"] == "1984"
    catalog.delete_book(1)
    assert catalog.find_book(1) == "Book not available"

def test_loan_records():
    loans = LoanRecords()
    loans.add_loan(101, 1)
    assert len(loans.list_user_loans(101)) == 1
    loans.remove_loan(101, 1)
    assert len(loans.list_user_loans(101)) == 0

if __name__ == "__main__":
    test_book_catalog()
    test_loan_records()
    print("All tests passed!")
