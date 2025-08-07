#------------Square of a number---------

def square(number):
  try:
      number = int(number)
      result = number * number
      print(result)
      return result
  except Exception as error:
   print(error)


square(4)


#-----------multiple parameters in function--------

def sum(num1, num2):
   return num1 + num2

# print(sum(2,3))


#-------------------multiply two number and also accept string---------

def multiply(value1, value2):
  return value1 * value2


# print(multiply('h',7))


#----------function returning multiple values area and circumference of a circle-----------
import math

def area_stats(radius):
  area = math.pi * radius **2
  circumference = 2 * math.pi * radius

  return {
    'area':round(area, 3),
    'circumference': round(circumference, 3)}

result = area_stats(7)
print(result['area'])


#---------------------------function greet user if user not found greet with default name----------

def greet(user ='zia'):
  return user

# print(greet())


#-----------lambda function--------------

cube = lambda x: x**3
print(cube(3))



#---------*args a variable(multiple)args function accept multiple arguments----------

def add(*args):
  return sum(args)


# print(add(1,2,3))
# print(add(3,4,5,6,7,7))



#-------------------**kwargs-------

def result_card(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")


result_card(name = 'zia', marks = 89 )