from math import sqrt

print('Введите координаты точки А:')
x_A = float(input('ось X: '))
y_A = float(input('ось Y: '))
print("Введите координаты точки B:")
x_B = float(input('ось X: '))
y_B = float(input('ось Y: '))

print('Дистанция между точками A и B: ', round(
      sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))
