def some_function():
    print("print in the function")


def some_function2(username):
    print(f"Welcome, {username}")


def times_function(num_1, num_2):
    return num_1 * num_2


def some_function3(user, first_name, *other_info):
    print(user)
    print(first_name)
    for info in other_info:
        print(info)


def tax_calc(rate, amount):
    return (rate/100) * amount


some_function()
some_function2("me")
print(times_function(11, 12))
some_function3('dgriffith', 'Drew', 'other info', 'info2', 'info3')

print('Tax Rate:', tax_calc(5, 150))


