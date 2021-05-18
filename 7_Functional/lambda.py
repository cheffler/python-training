from functools import reduce

# lambda means use once and forget

# lambda param: action(param)

arr = [1, 2, 3]
print(arr)
print(list(map(lambda item: item*2, arr)))

print(reduce(lambda acc, item: acc+item, arr))

print(list(map(lambda item: item ^ 2, arr)))

# using lambda in sorting for key definition
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda item: item[1])
print(a)
