def processing(text: str, flag: bool, number: float):
    if not text:
        raise ValueError("Поле 'text' нельзя оставить пустым")

    squares_dict = []

    for i in range(int(number) + 1):
        if i == 4:
            continue
        if i == 9:
            break

        square = i ** 2
        squares_dict[i] = square
        print(square)

        if square > 50:
            print(f"Квадрат числа {i} больше 50")
        elif 20 <= square <= 50:
            print(f"Квадрат числа {i} больше или равен 20 и меньше или равен 50")
        else:  
            print(f"Квадрат числа {i} меньше 20")

    return squares_dict

konec = processing("Пока", False, 321123)
propusk = {}
for key, value in konec.items():
    if key % 2 == 0:
        propusk[key] = value
print(propusk)
