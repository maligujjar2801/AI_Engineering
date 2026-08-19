class Book :
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __str__(self):
        return f"{self.title} has {self.pages} pages."
    def __len__(self):
        return self.pages
book = Book("Holy Quran", 604)
print(book)
print(len(book))