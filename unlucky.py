for n in range(1, 21):
    if n == 4 or n == 13:
        if n % 2 != 1:
            print(f'{n} is unlucky and even')
        else:
            print(f'{n} is unlucky and odd')
    elif n % 2 == 1:
        print(f'{n} is odd')
    else:
        print(f'{n} is even')

print('\n')
# diferente versión

for n in range(1, 21):
    if n == 4 or n == 13:
        if n % 2 != 1:
            state = 'unlucky and even'
        else:
            state = 'unlucky and odd'
    elif n % 2 == 1:
        state = 'odd'
    else:
        state = 'even'
    print(f'{n} is {state}')
