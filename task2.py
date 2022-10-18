from random import uniform

num = int(input('Сколько элементов будет в списке? '))
list = []
for i in range(num):
    f = uniform(0, 9)
    list.append(round(f, 2))
min = list[0]
max = 0
for i in range(len(list)):

    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
differ = (max - int(max)) - (min - int(min))

print(list)
print(max, min)
print(round(differ, 2))
