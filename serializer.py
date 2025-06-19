import json
filename = 'library.json'
class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        return f'{self.name}, {self.author}, {self.year}'
        
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])

class library:
    def __init__(self):
        self.books = []
        self.load()
        
    def add_book(self, book):
        self.books.append(book)
        self.save()
        
    def delete_book(self, name):
        found = False
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                print(f"Книга с именем '{name}' удалена.")
                found = True
                break
        if not found:
            print(f"Книга '{name}' не найдена.")
        self.save()
        
    def show_books(self):
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books:
                print(book.get_info())
                print()
    def save(self):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
    
    def load(self):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data_list = json.load(f)
                self.books = [Book.from_dict(data) for data in data_list]
        except FileNotFoundError:
            self.books = []
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            self.books = []
            
lib = library()

lib.show_books()

while True:
    print("Выберите действие:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Вывести список книг")
    print("0. Выйти")
    choice = input("Введите номер действия: ")

    if choice == '1':
        name = input("Введите название книги: ")
        author = input("Введите автора: ")
        year_input = input("Введите год издания: ")
        try:
            year = int(year_input)
            new_book = Book(name, author, year)
            lib.add_book(new_book)
            print(f"Книга '{name}' добавлена.")
        except ValueError:
            print("Некорректный год. Попробуйте снова.")
    elif choice == '2':
        name = input("Введите название книги для удаления: ")
        lib.delete_book(name)
    elif choice == '3':
        lib.show_books()
    elif choice == '0':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
