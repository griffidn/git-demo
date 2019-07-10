x = 10
if x == 5:
    print(x)
    raise Exception('x should not be 5. The value of x was {}'.format(x))

try:
    print(0 / 0)
except ZeroDivisionError:
    print('Divide by zero exception happened')
