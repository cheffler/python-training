
while True:
    try:
        age = int(input('what is you age? '))
        10/age
        print(age)

    except ValueError as err:
        print(f'please enter a number {err}')

    except ZeroDivisionError:
        print('please enter age higher than zero')

    else:
        print('thank you')
        break

