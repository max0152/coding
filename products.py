products = ("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)
def product80(products):
    print("Список продуктов с ценой меньше 80:")
    for product in products:
        ima, cena = product
        if cena < 80:
            print(f"Товар: {ima}, Цена: {cena}")
for product in products:
    ima, cena = product
    print(f"Товар: {ima}, Цена: {cena}")
product80(products)
