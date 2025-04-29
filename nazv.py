def sozd(ima):
    with open(ima, 'w') as new:
        new.write('Это первая строка этого файла')

sozd('new.txt')
