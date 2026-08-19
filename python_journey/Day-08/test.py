class Book :
    def __init__(self,title):
        self.title = title

class Library :
    def __init__(self):
        self.books = []
    def add_books(self,book):
        self.books.append(book)
book_1 = Book("Atomic Habits")
library = Library()
library.add_books(book_1)
print(library.books[0].title)