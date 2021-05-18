from functools import reduce

# Pure Functions
# 1. Always produce the same result given the same inputs
# 2. No side effects (e.g. print to screen)

# map, filter, zip and reduce


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc+item


arr = [1, 2, 3]

# map
list_mapped_arr = list(map(multiply_by2, arr))
print(list_mapped_arr)

# filter
print(list(filter(only_odd, arr)))

# zip
arr2 = [10, 20, 30]
print(list(zip(arr, arr2)))

#  reduce
print(reduce(accumulator, arr, 10))
