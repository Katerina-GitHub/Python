n = int(input('Введите число N: '))
factor = 1
for i in range(1, n+1):
    factor *= i
    print(factor, end=' ')
