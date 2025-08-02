# if __name__ == "__main__":
#     print("hello poor developer")

# def poor_developer(n):
#   print(n)

# poor_developer("poor people") 

# poor_dev = 'zia'

name = ["zia", "waqas", "asim"]
colors = name
# name.pop()
# print(name)
# print(colors)

fruits = {
  "Dry_fruits": {"Almond": "brown", "Peanuts":"brown", "Cashews": "white"},
  "Green_fruits": {"Banana": "yellow", "orange": "orange", "peach": "red"}
}

#print(fruits["Dry_fruits"]["Almond"])
# print(fruits["Green_fruits"]["Banana"])
# print(fruits.get("Dry_fruits", "Green_fruits"))

students = ['Asim', 'Aleena', 'Mehreena','Ayoub']
default_status = 'pass'

new_record = dict.fromkeys(students, default_status)
print(new_record)


fruits = ["Apple", "Grapes", "Berry"]
taste = "Tasty"

fruits_dic = dict.fromkeys(fruits, taste)

print(fruits_dic)
