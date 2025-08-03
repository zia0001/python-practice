#----- Age group categorization-----
while True:
      try:
            age =int(input("Enter your age: "))

            if age <= 0:
              print("Enter valid age")
            elif age > 0 and age < 13:
              print("Child")
              break
            elif age >= 13 and age <= 19:
              print("Teenager")
              break
            elif age >= 20 and age <= 59:
              print("Adult")
              break
            else:
              print("Senior")
              break
      except ValueError:
        print("invalid value")


#-----Movie ticket pricing------
from datetime import datetime


CHILD_PRICE = 10
ADULT_PRICE = 12
DISCOUNT = 2
DISCOUNT_DAY = "Saturday"
while True:
    try:
        age = int(input("Enter your age: "))

        if age <= 0:
          print("Age must be greater than 0.")
          continue
          
        day =  datetime.now().strftime("%A")
        discount_applies = (day == DISCOUNT_DAY)

        if age > 18:
           price = ADULT_PRICE
        else:
           price = CHILD_PRICE
        if discount_applies:
           price = price - DISCOUNT
        print(f"Ticket price is ${price:.2f}")
        break
    except ValueError:
      print("Invalid value")


#-------------- Grade Calculator--------------
grade = ''
while True:
    try:
        score = int(input("Enter your score: "))
        if score < 0:
          print("Score must be positive.")
          continue
        if score > 100:
          print("Please enter valid score")
          continue
        if score >= 90 and score <= 100:
          grade = 'A'
        elif score >= 80 and score <= 89:
          grade = 'B'
        elif score >= 70 and score <= 79:
          grade = 'C'
        elif score >= 60 and score <=69:
          grade = 'D'
        elif score >= +0 and score < 60:
            grade = 'F'
        print(grade)
        break
    except Exception as error:
        print(error)


#---------------Fruit Ripness Checker------------


fruit_name = input("Enter fruit name: ").upper()
fruit_color = input("Enter fruit color: ").upper()

if fruit_name == "BANANA":
    if fruit_color == 'GREEN':
      print("Fruit is unripe")
    elif fruit_color == 'YELLOW':
      print("Fruit is ripe")
    elif fruit_color == 'BROWN':
      print("Fruit is Overipe")

if fruit_name == "APPLE":
    if fruit_color == 'GREEN':
      print("Fruit is unripe")
    elif fruit_color == 'YELLOW' or 'RED':
      print("Fruit is ripe")
    elif fruit_color == 'BROWN':
      print("Fruit is Overipe")


#---------------Weather Activity Suggestion---------------


while True:
      weather_condition = input("What is weather condition: ").lower()
      if weather_condition.isalpha():
          break
      else:
          print("Please enter letters only.")
if weather_condition == 'sunny':
          activity = "Enjoy! Go for a walk"
elif weather_condition == 'rainy':
          activity = "Stay at home and read a book"
elif weather_condition == 'snowy':
          activity = "Build a snowman"
else:
        activity = "condition not recognized"

print(activity)
    


#------------------Transportation mode selection-----------


try:
  while True:
      distance = int(input('Enter distance: '))
      transport_mode = ''

      if distance < 0 :
        print("Distance must be positive")
        continue
      if distance < 3:
        transport_mode = 'Walk'
      elif distance >= 3 and distance <= 15:
        transport_mode = 'Bike'
      else:
        transport_mode = 'Car'
      print(transport_mode)
      break

except Exception as error:
  print(error)



#-------------Coffee Customization-----------
while True:
    customer_name = input("Enter your name: ").lower()
    if customer_name.isalpha():
      break
    else:
       print("Please enter only letters")
while True:
    order_size =input("Enter coffee size: ").lower()
    if order_size.isalpha():
      break
    else:
      print("Please enter only letters")
while True:
    extra_input_shot = input("Want extra shot? (yes/no): ").lower()
    if extra_input_shot in ['yes', 'no']:
      extra_shot = (extra_input_shot == 'yes')
      break
    else:
        print("Please enter yes or no")
   
    
   
if order_size in ['small']:
  order = 'small'
elif order_size in ['medium', 'med']:
  order = 'medium'
elif order_size in ['large', 'lg']:
  order = 'large'
else:
  order = 'size not recognized'

if extra_shot:
   order = order + " coffee with extra shot"
print(f"{customer_name} ordered {order}")


#-----------------password strength checker-------
def password_checker(password):
    try:
    
      password_char = ''

      if len(password) < 6:
        password_char = len(password)
        print(f"{password} has {password_char} charactes. Password must have more the 6 chars")
      elif len(password) >= 6 and len(password) <= 10:
        password_char = len(password)
        print(f"{password} has {password_char} characters. Password is medium")

      elif len(password) >= 11 and len(password) <= 50:
        password_char = len(password)
        print(f"{password} has {password_char} characters. Password is stronge")

    except Exception as error:
      print(error)

user_password = input("Enter password: ")
password_checker(user_password)


#----------Leap Year checker----------------
year = int(input("Enter year: "))    

def leap_year(year):
    if (year % 4 == 0 and year % 100  != 0) or (year % 400 == 0) :
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year") 


leap_year(year)



#--------pet food recommendation-------
while True:
    pet_specie = input("Enter pet specice type: ").lower()
    if pet_specie.isalpha():
      break
    else:
       print("Enter only letters")

while True:
    try:
       pet_age = int(input("Enter pet age: "))
       if pet_age <= 0: 
          print("Age must be greater than 0.")
          continue
    except Exception as error:
       print(error)
       continue
    break
food = ''
if pet_age <= 0:
  print("Age must be greater than 0.")

if pet_specie =='dog' and pet_age < 2:
  food = 'Puppy food'
elif pet_specie == 'cat' and pet_age > 5:
  food = 'Senior cat food'
else:
   food = ' Regular pet food'

print(food)