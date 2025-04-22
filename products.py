products = ("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)
def product80(products):
    print("Список продуктов с ценой меньше 80:")
    for product in products:
        ima, cena, kolvo = product
        if cena < 80:
            print(f"Товар: {ima}, Цена: {cena}, Количество:{kolvo}")
def globalcena(products):
    for product in products:
        ima, cena, kolvo = product
        totalcena = cena * kolvo
        if kolvo * cena != 0:
            print(f"Общая стоимость товара:{totalcena}")
for product in products:
    ima, cena, kolvo = product
    print(f"Товар: {ima}, Цена: {cena}, Количество:{kolvo}")
product80(products)
globalcena(products)
