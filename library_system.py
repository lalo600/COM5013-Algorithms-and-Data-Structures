class BookCatalog:
  def _init_(self):
    self.books = {}

def add_book(self, book_id, book_info):
        self.catalog[book_id] = book_info

    def remove_book(self, book_id):
        self.catalog.pop(book_id, None)

    def search_book(self, book_id):
        return self.catalog.get(book_id, "Book not found")
