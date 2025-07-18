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
    print("name must be least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")















































