import math
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' автор {self.author}, год издания: {self.year}"
class BankAccount:
    def __init__(self, number, balance=0):
        self.__number = number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма для пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снятие {amount}. Остаток на счёте: {self.__balance}")
            else:
                print("Недостаточно средств.")
        else:
            print("Сумма для снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

    def get_number(self):
        return self.__number
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} издает звук.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def print_area(shape):
    print(f"Площадь: {shape.area()}")

book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book3 = Book("Мастер и Маргарита","Михаил Булгаков", 1967)

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())

account = BankAccount("1234567890", 1000)

try:
    print(f"Номер счёта: {account.__number}")
except AttributeError:
    pass

try:
    print(f"Баланс: {account.__balance}")
except AttributeError:
    pass

print(f"Номер счёта: {account.get_number()}")
print(f"Баланс: {account.get_balance()}")

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

animals = [
    Dog("Бобик"),
    Cat("Мурка"),
    Animal("Животное")
]

for animal in animals:
    animal.make_sound()

rect = Rectangle(4, 5)
circle = Circle(3)

print("Прямоугольник:")
print_area(rect)

print("Круг:")
print_area(circle)
