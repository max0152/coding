products = ("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)
def product80(products):
    print("Список продуктов с ценой меньше 80:")
    for product in products:
        ima, cena, kolvo = product
        if cena < 80:
            print(f"Товар: {ima}, Цена: {cena}, Количество:{kolvo}")
for product in products:
    ima, cena, kolvo = product
    print(f"Товар: {ima}, Цена: {cena}, Количество:{kolvo}")
product80(products)
