class Books():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def book_details(self):
        return print(f"{self.name} and the price is {self.price}")


class Author(Books):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def full_details(self):
        return print(f"{self.name} written by {self.author} and the price is {self.price} ")


class Admin(Books):
    def __init__(self, name, books=None):
        super().__init__(name, price)
        if self.books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)


if __name__ == '__main__':
    one = Author("Scilent patient", 3434, "pavan pattinson")
    one.book_details()
    one.full_details()
