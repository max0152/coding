def procht():
    f = open('file.txt', 'r')
    try:
        with open('file.txt', 'r') as f:
            print('Файл открыт!')
    except FileNotFoundError:
        print('Файл не найден')
