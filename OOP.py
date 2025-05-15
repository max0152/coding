class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' автор {self.author}, год издания: {self.year}"

book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
