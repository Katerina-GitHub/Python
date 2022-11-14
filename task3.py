num = (input('number: '))
print(sum(map(int, num.replace('.', '').replace('-', ''))))
