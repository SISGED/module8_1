def add_everything_up(a, b):

    try:
        return a + b

    except TypeError:
        return str(a) + str(b)

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('яблоко', 'банан'))
print(add_everything_up(10, 20))