#lst = [9, 22, 34, -88, 52, -2, -7, -11]
# print(*filter(lambda x:
#              9 < abs(x) < 100, lst))
print(*filter(lambda x:
              10 <= abs(x) <= 99, map(int, input().split())))
