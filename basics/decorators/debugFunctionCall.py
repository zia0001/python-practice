def func_debug(func):
  def wrapper(*args, **kwargs):
    args_values = ', '.join(str(arg)for arg in args)
    print(f"Calling: {func.__name__}() with args {args_values}")
    return func(*args, **kwargs)
  return wrapper


@func_debug
def greet(name, greeting = 'Hello'):
  print(f"{greeting}, {name}")

greet('zia', "welcome")