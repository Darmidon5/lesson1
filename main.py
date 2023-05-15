def is_100(x):
    if x != 100:
        raise ValueError('not 100')


print(is_100(50))