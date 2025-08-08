def outer():
  msg = 'Hello from outer function'

  def inner():
    print(msg)
  
  return inner     #return function, not the result


greet = outer()
greet()



def multiplier(x):
  def multiply(y):
    return x * y
  
  return multiply

result = multiplier(3)
print(result(6))