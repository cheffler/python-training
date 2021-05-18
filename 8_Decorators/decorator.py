# Decorator Pattern
def my_dec(func):
    def wrap_func(*args, **kwargs):
        print('***')
        func(*args, **kwargs)
        print('***')
    return wrap_func


@my_dec
def hello(greet):
    print(greet)


hello('dsfasd')
