class Book:
    def __init__(self, name, author, year , genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

    def book_info(self):
        print(self.name, ",", self.author, "(", self.year, ")", ",", self.genre)


Book = Book("Норвежский лес", "Харуки Мураками", 1987, "роман")
Book.book_info()

