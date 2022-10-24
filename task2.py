num = int(input('Введите значение N '))
multi = []
i = 2

while i <= num:
    if num % i == 0:
        multi.append(i)
        num //= i
    else:
        i += 1

print(multi)
