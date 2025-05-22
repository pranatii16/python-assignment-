class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"You returned '{book.title}'")
                return
        print("Book not found in library.")

lib = Library()
lib.add_book(Book("Python 101", "John Doe"))
lib.add_book(Book("Data Science", "Jane Smith"))
lib.borrow_book("Python 101")
lib.return_book("Python 101")