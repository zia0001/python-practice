# -------count positive numbers----------


numbers = [1, -2, 3, -4, 5, -6, -7, -9, 8, 10]
positive_numbers = []

for number  in  numbers:
  if number > 0:
    positive_numbers.append(number)
print(positive_numbers)


# ----------Sum of even numbers-------

numbers = [2,5,1,7,41,62,88,73,54]
even_numbers = []

for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print(even_numbers)

sum_of_even = 0

for number in even_numbers:
  sum_of_even += number
print(f"sum of even numbers = {sum_of_even}")


input_numbers = input("Enter numbers: ")
list_of_strings = input_numbers.split()
list_of_integers = list(map(int, list_of_strings))
even_numbers = []

for number in list_of_integers:
  if number % 2 == 0:
    even_numbers.append(number)
print(even_numbers)

sum_of_even = 0

for number in even_numbers:
  sum_of_even += number
print(f"sum of even numbers = {sum_of_even}")



#-------------multiplication printer table-----------------

number = int(input("Enter the number: "))

# for n in range(1, 11):
#   print(f"{number} X {n} = {n * number}")



#-----------Reverse a sring-----------


original_string = input("Enter the string: ")
reversed_string = original_string[::-1]


# print(reversed_string)



#----------Find repeated character in string------------


input_string = input("Enter anything: ")
string_list = list(input_string)

unique_char = []
repeated_char = []
for s in string_list:
  if s not in unique_char:
    unique_char.append(s)
  else:
    repeated_char.append(s)
print(f"{repeated_char} is/are repeated character(s)")


#----------Find first Non repeated character in string------------

input_string = input("Enter anything: ")
string_list = list(input_string)

unique_char = []
repeated_char = []
for s in string_list:
  if s not in unique_char:
    unique_char.append(s)
  else:
    repeated_char.append(s)

for n in string_list:
  if n not in repeated_char:
    print(f"{n} is first Non repeated character")





  