# list, set, dictionary
# faster and easier way to loop
# param for param in interable <conditional>

char_list = [char + '-' for char in 'hello']

print(char_list)

num_list_1 = [num for num in range(0, 100)]
num_list_2 = [num**2 for num in range(0, 100)]
num_list_3 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(num_list_3)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set(x for x in some_list if some_list.count(x) > 1))
print(duplicates)
