x = int(input('Введите координаты точки x: '))
y = int(input('Введите координаты точки y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')
