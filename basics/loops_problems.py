#-------count positive numbers----------


numbers = [1, -2, 3, -4, 5, -6, -7, -9, 8, 10]
positive_numbers = []

# for number  in  numbers:
#   if number > 0:
#     positive_numbers.append(number)
# print(positive_numbers)


#----------Sum of even numbers-------

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
