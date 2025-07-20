# import math
from doctest import OutputChecker
from os import remove

import numpy as np
#
#
# full_patient_name = 'John Smith'
# age = 20
# is_new = True
#
#
# name = input('What is your name: ')
# favourite_color = input('What is your favourite color: ')
# print(name,'likes',favourite_color)
#
# birth_year = int(input('Birth year: '))
# age = 2025 - birth_year
# print(age)
#
#
# weight_lb = int(input('what is your weight(lb): '))
# weight_kg = weight_lb * 0.453592
# print(weight_kg,'kg')
#
#
# message = 'deployed successfully'
# alert = message
# print(alert[0:5])
#
#
# name = 'Jennifer'
# print(name[1:-1])
#
#
# course = 'learning mathematics'
# print(len(course), course.upper())
# print(course.find('tics'))         # 7
# print(course.replace('atics','atata')) #replaces characters
#
# print('learning' in course) # returns bool value
#
#
# print(10 // 3)   #return integer i.e 3 without floating points
# print(10 % 4)    #returns remainder
# print(3 ** 3)    #raise to power
#
# x = 10
# x = x + 4
# x += 4            #augmented assignment operator--- for shorter code
# print(x)
#
#
# x = 10 + 6 * 3 ** 2
# print(x)            #return 64---following Expo>division>multi>add>sub
# y = (5 + 3) * 6 ** 2 / 2
# print(y)            #return 144.o following BEDMAS
#
#
# y = 78.56
# print(round(y))
# print(abs(-988.00))         #gives absolute (+ive) value
# print(math.factorial(5))
#
#
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("It's a hot day. drink plenty of water")
# elif is_cold:
#     print("It's a cold day. Wear warm clothes")
#
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")
#
# house_price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = house_price * 0.1
# else:
#     down_payment = house_price * 0.2
# print(f"down_payment: ${down_payment}")
#
#
# has_property = input("Do you own property?(yes/no):").lower() == 'yes'
# has_car = input("Do you have a car?(yes/no):").lower() == 'yes'
#
# if has_property and has_car:
#      print("Has to pay tax annually ")
# elif has_car or has_property:
#     print("Might pay some tax")
# else:
#     print("No tax applied")
#
# course ='python course'
# print(course.upper())
#
# marks = [12, 13,45,33,33]
# print(len(marks))
#
# def cal_sum(value1, value2):
#     sum_is =value1 +value2
#     print(sum_is)
#     return sum_is
#
# cal_sum(3,9)
#
#
# name = input("Enter your name: ")
#
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")
#
# def weight_converter():
#     weight = int(input("weight: "))
#     weight_unit = input("(L)bs or (K)g: ").lower()
#
#     if weight_unit == 'l':
#         weight_in_kg = weight * 0.453592
#         print(f"You are {round(weight_in_kg, 2)} kilos. ")
#     elif weight_unit == 'k':
#         weight_in_lbs = weight / 0.453592
#         print(f"You are {round(weight_in_lbs, 2)} pounds. ")
#     else:
#         print("Please enter a valid weight.")
#
# weight_converter()
#
#
# i = 8
#
# while i >= 1:
#     print("$" * i)
#     i -= 1
# print("Finished")
#
# i = 1
#
# while i <=8:
#     print("@" * i)
#     i += 1
# print("Done")
#
#
# number_to_guess = 8
# for attempt in range(3):
#     user_guessed_number = int(input("guess the secret number: "))
#     if user_guessed_number == number_to_guess:
#         print("You guessed correct number")
#         break
# else:
#     print("Sorry, you failed")
#
# car_started = False
# while  True:
#     user_command = input(">").lower()
#     if user_command == 'help':
#        print("""
# start- to start the car
# stop- to stop the car
# quit- to exit
#         """)
#     elif user_command == 'start':
#         if car_started:
#             print("Car is already started")
#         else:
#             car_started = True
#             print("Car started...Ready to go!")
#     elif user_command == 'stop':
#         if not car_started:
#             print("Car has already stopped")
#         else:
#             car_started = False
#             print("Car has stopped")
#     elif user_command == 'quit':
#         break
#     else:
#         print("Please enter a valid command")
#
# def prime_number(number):
#     if number <= 1:
#         print(f"{number} is not a prime number")
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(f"{number} is not a prime number")
#                 break
#         else:
#             print(f"{number} is a prime number")
#
#
# prime_number(7)
#
# prices = [78, 98, 345,786]
# total = 0
# for price in prices:
#     total += price
# print(total)
#
#
#
# for x in range(3):
#     for y in range(2):
#         print(f"{x,y}")
#
#
# symbols_number =[5,2,5,2,2]
# for number in symbols_number:
#     print("X" * number)
#
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ''
#     for y in range(x):
#             output += 'x'
#     print(output)
#
#
#
# names = ['Ali', 'khalid', 'sami', 'samuel']
#
# names[1] = 'waleed'
#
# print(names)
#
#
# numbers = [45, 7, 8, 23, 55]
# maximum = numbers[0]
#
# for number in numbers:
#     if number > maximum:
#         maximum = number
# print(f"{maximum} is the largest number")
from os.path import split

# numbers = [45, 664, 2 ,4, 6,554]
#
# minimum = numbers[0]
#
# for number in numbers:
#     if number < minimum:
#         minimum = number
# print(f"{minimum} is the smallest number")


# matrix = [
#     [7, 9, 4],
#     [9, 9, 4],
#     [4, 2, 9]
# ]
#
# print

# matrix = [
#      [7, 9, 4],
#      [9, 9, 4],
#      [4, 2, 9]
# ]
#
# for row in matrix:
#     for value in row:
#         print(value)


# marks_list = [43, 44, 53, 77, 32]
# (marks_list.insert(2, 63))       #insert value at give index
# print(marks_list)
# marks_list.remove(44)                   #remove specific value from list
# print(marks_list)
# marks_list.append(90)                   #add value to end of list
# print(marks_list)
# print(marks_list.index(53))             #return index
# marks_list.pop()                        #remove last value
# print(marks_list)
# print(marks_list.count(44))             #checks occurrence of a value
# marks_list.sort()                       #sort in ascending order
# print(marks_list)
# marks_list.reverse()                    #return descending order of values in list
# print(marks_list)
# print(40 in marks_list)          #check existence of value in list
# marks_list2 = marks_list.copy()     #makes independent copy of list
# print(marks_list2)
# marks_list.clear()               #clear entire list
# print(marks_list)
#
#
# marks_list2.append(909)
# print(marks_list)



# numbers = [3, 4, 6, 8, 8, 2]
# unique_list = []
# for number in numbers:
#     if number not in unique_list:
#         unique_list.append(number)
# print(unique_list)



# values = (5, 5,3,98,33)
# coordinates = (3, 5, 9)
# x, y,z =     coordinates      #unpacking
# print(z)

# phone_number =input('phone: ')
# key_in_phone = phone_number.split()
# keys_in_words = 'One Two Three'
# for key_in_phone in phone_number:
#     (keys_in_words.split())
# print(keys_in_words.split())

# phone_number =input('phone: ')
#
# keys_in_words_mapping ={
#     "1": 'One',
#     "2": 'Two',
#     "3": 'Three',
#     "4": 'Four'
#
# }
# output_message = ' '
# for key in phone_number:
#     output_message += keys_in_words_mapping.get(key, 'unknown' ) + ' '
# print(output_message)



# def emojis_mapping(message):
#     words_in_message = message.split()
#
#     emojis = {
#         ":)": '😀',
#         ":(": '😔'
#     }
#     output = ''
#     for word in words_in_message:
#        output +=  emojis.get(word, word) + ' '
#     print(output)
#
#
# user_message = input("> ")
# emojis_mapping(user_message)


# try:
#     print("This program divides two numbers")
#     first_number = int(input("Enter first number: "))
#     Second_number = int(input("Enter second number: "))
#     result = first_number / Second_number
#     print(f"result is {result}")
# except ZeroDivisionError:
#     print("Cannot be divide by zero")


# class Animals:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def sleep(self):
#         pass
#     def cow(self, name):
#         self.name = name
#         print(f"i ma {name}. i eat grass")
#     def cat(self, name):
#         self.name = name
#         print(f"i am {name}  and i like love cuddling")
#
# a1 =Animals('Cowy', 'herbivorous')
# a2 = Animals('catty', 'pet')
# print(f"Name is {a1.name} and specie is {a1.species}")
# print(f"Name is {a2.name} and specie is {a2.species}")
#
# print(a1.cow(a1.name))
#
#
# class Birds(Animals):
#     def parror(self):
#         print("I am parrot and i can fly")
# b1 = Birds()
# b1.sleep()


# library = ["english", "maths", "operating system", "data structures", "machine learning", "programming fundamentals", "programming in cpp","calculus"]
# lend_books_data ={}
#
# def display_books():
#     print("\nAvailable books")
#     for book in library:
#         print(f" --> {book}")
# def add_book():
#     book = input("Enter book name: ")
#     user = input("Enter your name: ")
#     library.append(book)
#     print(f" {book} is added by {user}")
# def lend_book():
#     global lend_books_data
#     book =input("Enter book name: ")
#     user =input("Enter your name")
#     if book in library:
#         if book not in lend_books_data:
#             lend_books_data[book] = user
#             print(f"Book {book} has been lend to {user}")
#         else:
#             print(f"Sorry the {book} has already lent to {lend_books_data[book]}")
#     else:
#         print(f"{book} is not available in library")
#
#
# def return_book():
#     book = input("Enter the book name: ")
#     if book in lend_books_data:
#         del lend_books_data[book]
#         print("Thanks for returning the book")
#     else:
#         print(f"{book} book was not lent out")
#
# while True:
#     print("\n LIBRARY BOOKS MENU")
#     print("1. Display books")
#     print("2. Add  book")
#     print("3.Lend  book")
#     print("4.Return book ")
#
#     choice = input("Enter your choice(1-5): ")
#
#     match choice:
#         case '1':
#             display_books()
#         case '2':
#             add_book()
#         case '3':
#             lend_book()
#         case '4':
#             return_book()
#             break
#         case _:
#             print("Invalid option")

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} can talk")
        pass

p1 = Person('zia')
p1.talk()
p2 =Person("Ahmad")
p2.talk()









