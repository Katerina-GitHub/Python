fibonacci = int(input('Задайте количество чисел в списке '))

list = []
for i in range(fibonacci+1):
    if i == 0:
        list.append(i)
    elif i == 1:
        list.append(i)
        list.insert(0, i)
    else:
        list.append(list[len(list)-1]+list[len(list)-2])
        list.insert(0, (-1)**(i-1)*list[len(list)-1])
print(list)
