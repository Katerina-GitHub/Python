nums = [3, 5, 1, 2, 3, 5]
result = []
for i in nums:
    if nums.count(i) < 2:
        result.append(i)

print(result)
