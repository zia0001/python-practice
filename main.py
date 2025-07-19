import math


full_patient_name = 'John Smith'
age = 20
is_new = True


name = input('What is your name: ')
favourite_color = input('What is your favourite color: ')
print(name,'likes',favourite_color)

birth_year = int(input('Birth year: '))
age = 2025 - birth_year
print(age)


weight_lb = int(input('what is your weight(lb): '))
weight_kg = weight_lb * 0.453592
print(weight_kg,'kg')


message = 'deployed successfully'
alert = message
print(alert[0:5])


name = 'Jennifer'
print(name[1:-1])


course = 'learning mathematics'
print(len(course), course.upper())
print(course.find('tics'))         # 7
print(course.replace('atics','atata')) #replaces characters

print('learning' in course) # returns bool value


print(10 // 3)   #return integer i.e 3 without floating points
print(10 % 4)    #returns remainder
print(3 ** 3)    #raise to power

x = 10
x = x + 4
x += 4            #augmented assignment operator--- for shorter code
print(x)


x = 10 + 6 * 3 ** 2
print(x)            #return 64---following Expo>division>multi>add>sub
y = (5 + 3) * 6 ** 2 / 2
print(y)            #return 144.o following BEDMAS


y = 78.56
print(round(y))
print(abs(-988.00))         #gives absolute (+ive) value
print(math.factorial(5))


is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day. drink plenty of water")
elif is_cold:
    print("It's a cold day. Wear warm clothes")

else:
    print("It's a lovely day")

print("Enjoy your day")

house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f"down_payment: ${down_payment}")


has_property = input("Do you own property?(yes/no):").lower() == 'yes'
has_car = input("Do you have a car?(yes/no):").lower() == 'yes'

if has_property and has_car:
     print("Has to pay tax annually ")
elif has_car or has_property:
    print("Might pay some tax")
else:
    print("No tax applied")

course ='python course'
print(course.upper())

marks = [12, 13,45,33,33]
print(len(marks))

def cal_sum(value1, value2):
    sum_is =value1 +value2
    print(sum_is)
    return sum_is

cal_sum(3,9)


name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")

def weight_converter():
    weight = int(input("weight: "))
    weight_unit = input("(L)bs or (K)g: ").lower()

    if weight_unit == 'l':
        weight_in_kg = weight * 0.453592
        print(f"You are {round(weight_in_kg, 2)} kilos. ")
    elif weight_unit == 'k':
        weight_in_lbs = weight / 0.453592
        print(f"You are {round(weight_in_lbs, 2)} pounds. ")
    else:
        print("Please enter a valid weight.")

weight_converter()


i = 8

while i >= 1:
    print("$" * i)
    i -= 1
print("Finished")

i = 1

while i <=8:
    print("@" * i)
    i += 1
print("Done")


number_to_guess = 8
for attempt in range(3):
    user_guessed_number = int(input("guess the secret number: "))
    if user_guessed_number == number_to_guess:
        print("You guessed correct number")
        break
else:
    print("Sorry, you failed")

car_started = False
while  True:
    user_command = input(">").lower()
    if user_command == 'help':
       print("""
start- to start the car
stop- to stop the car
quit- to exit
        """)
    elif user_command == 'start':
        if car_started:
            print("Car is already started")
        else:
            car_started = True
            print("Car started...Ready to go!")
    elif user_command == 'stop':
        if not car_started:
            print("Car has already stopped")
        else:
            car_started = False
            print("Car has stopped")
    elif user_command == 'quit':
        break
    else:
        print("Please enter a valid command")

def prime_number(number):
    if number <= 1:
        print(f"{number} is not a prime number")
    else:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")


prime_number(7)

prices = [78, 98, 345,786]
total = 0
for price in prices:
    total += price
print(total)



for x in range(3):
    for y in range(2):
        print(f"{x,y}")


symbols_number =[5,2,5,2,2]
for number in symbols_number:
    print("X" * number)

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
            output += 'x'
    print(output)


