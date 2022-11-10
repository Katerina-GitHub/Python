my_list = [12, 'sadf', 5643, 'eva', 'many other things', 8, 9, 'ноль']
result = filter(lambda x: type(x) is int, my_list)
print(*result, sep=",")
result1 = filter(lambda x: type(x) is str, my_list)
print(*result1, sep=",")
