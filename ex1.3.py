cache = {}

def func(n):
    if n in cache:
        return cache[n]
    elif n == 0 or n == 1:
        result = n
    else:
        result = func(n-1) + func(n-2)
    cache[n] = result
    return result


print(func(35))