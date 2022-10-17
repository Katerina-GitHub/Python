n = int(input('Введите число N: '))
i = 2
while i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1
