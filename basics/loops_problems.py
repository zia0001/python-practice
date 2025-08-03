#-------count positive numbers----------


numbers = [1, -2, 3, -4, 5, -6, -7, -9, 8, 10]
positive_numbers = []

for number  in  numbers:
  if number > 0:
    positive_numbers.append(number)
print(positive_numbers)