def fib(num):
    # return all number until fib index num
    a = 0
    b = 1

    for i in range(num+1):
        yield a
        tmp = a
        a = b
        b = tmp+b


for x in fib(20):
    print(x)
