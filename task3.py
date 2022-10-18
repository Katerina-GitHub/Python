a = int(input('Какое число нужно преобразовать? '))
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2
print(b)
