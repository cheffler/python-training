# Generator

# list -> iterable -> __iter__
# range is a generator, but list is not it is a iterable
# a generator is iterable, an interable is not always generator

def generator_function(num):
    for i in range(num):
        yield i*2


# Not making the whole thing in memory/waiting for the list to be created
# for item in generator_function(1000):
#     print(item)

g = generator_function(10)
print(next(g))
next(g)
print(next(g))
