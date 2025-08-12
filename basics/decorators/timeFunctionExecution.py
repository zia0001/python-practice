import time

def timer(func):
  def wrapper(*args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__} ran in {end - start} time")
    return result
  return wrapper

@timer
def example(n):
  time.sleep(n)

example(6)