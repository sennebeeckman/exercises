class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string):
        search_string = search_string.lower()
        result = []
        for book in self.books:
            print(book.title, book.author)
            if  search_string in book.title.lower() or search_string in book.author.lower():
                result.append(book)
        return result
    
