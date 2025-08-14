import time


def cache(func):
    cache_value = {}
    print (cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(x, y):
    time.sleep(5)
    return x + y

print(long_running_function(4,5))
print(long_running_function(4,5))