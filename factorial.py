def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
f = open('file.txt', 'a')
f.write(str(factorial(11)))
