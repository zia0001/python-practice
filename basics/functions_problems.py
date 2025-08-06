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

print(sum(2,3))