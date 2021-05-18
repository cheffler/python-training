def hello():
    print('hellooooo')


def greet():
    print('still here')


def something(func):
    func()


a = something(greet)
