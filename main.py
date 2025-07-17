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