        ...data types / object types...

--> Number: 123, 3.14, 3+5j etc,
--> String: 'things', 'jack's' etc,
--> List: [1,2,4,9,[10, 'jack']]
--> Tuple: (1, 'zia', 'x', 8)
--> Dictionary: {"id": 1, "name": "zia", "age": 23}
--> Set: set(j,l,c), {3,5,j,9}
--> File: open(xyz.txt), open(r'C:\ham.bin, 'wb')
--> Boolean: True, False
--> None: None
--> Functions
--> modules  
--> classes
--> Advance: Decorators, Generators, Iterators
--> MetaProgramming



          ----------- Numbers-------------

--> operator overloading: means the + operator automatically decide the data on its left and right whether it is number or string and add them on the base of their datatype.
in simple terms the same + operator behaves differently for different types.
      example:
           print('zia' + 'uddin')  .....Concatenation (str + str)

   print(3 + 5)     ..... Addition (int + int)

--> chain comparison:

      2 == 2 < 3
      True

      because:>
      2 == 2 and 2 < 3
      
      left side: 2 == 2  --> return True
      right side: 2 < 3  --> return True

      both conditions are True so 'and' operator returns True

--> imaginary numbers: 
     (4 + 3j) * 2
      result: (8+6j)

--> random():  random.random()
              result: 0.5980655923501288

              it returns s random floating point  number between 0.0  and 1.0
--> randint(): 

            random.randint(3,12)
            result: 3

            it returns a random integer within a specified given range

--> shuffle(): 

            list = [2,3,4,67]
            random.shuffle(list)
            result: [4,67,2,3]

            The shuffle() function or method is used to randomly reorder the elements within a sequence, such as a list or array

--> sets: 

      ** & is used for intersection(common) between sets

       set_one = {4,6,7}
       set_one & {1,2,4}
       result: {4}

       

       ** | is used for union of sets
        set_one | {7,9,22}
        result: {4, 6, 7, 22, 9}


      ** - is used subtraction 
        set_one - {6}
        result: {4, 7}


            -----------strings----------

--> string slicing: 
                  poor_developer = 'zia'
first_char = poor_developer[0]
first_char
'z' 
print(first_char)
z   
full_name = 'zia'
get_full_name = full_name[0:3]
print(get_full_name)
zia 
get_full_name = full_name[0:2]
print(get_full_name)
zi  
number_list = "0123456789"
 number_list[:]
'0123456789'
 number_list[0:]
'0123456789'
 number_list[0:5]
'01234'
 number_list[:5]
'01234'
 number_list[-2]
'8' 
 number_list[-2:3]
''  
number_list[0:8:3]
'036'

--> split():
            names ="Ahmed, khalid, saeed, kamran"
            names.split()
           result: ['Ahmed,', 'khalid,', 'saeed,', 'kamran']  

           names.split(",")                                                 # will remove ',' from the string
           result : ['Ahmed', ' khalid', ' saeed', ' kamran']

           ** converts string into a list


--> placeholders:
                
total_marks = 100
obtained_marks = 75
result = "I obtained {} marks out of {}"
            
result.format(obtained_marks, total_marks)
output: 'I obtained 75 marks out of 100'

print(result.format(obtained_marks, total_marks))
I obtained 75 marks out of 100
 

--> List to string:

                  members = ['member1', 'member2', 'member3']
                  print(" ".join(members))                        # " "is used for space after each value
                  result: member1 member2 member3

--> raw string:

      full_path = r"E:\Python-Workspace\practice"
      print(full_path)
      E:\Python-Workspace\practice

      ** r is used to make a string raw(as it is) to avoid escape sequence problems during path setting...

             -----Lists------


vegs = ['onion', 'tomato', 'mint']
 vegs[0:3] = ['cucumber', 'bindi', 'chilli']
 vegs
['cucumber', 'bindi', 'chilli']
 vegs[2] =[]
 vegs
['cucumber', 'bindi', []]
 vegs[2] =''
 vegs
['cucumber', 'bindi', '']
 vegs[2] =None
 vegs
['cucumber', 'bindi', None]
 vegs[2:3] = []
 vegs
['cucumber', 'bindi']


--> List comprehension:

    cube_nums = [x**3 for x in range(5)]
    print(cube_nums)
    [0, 1, 8, 27, 64]



    ---------dictionaries---------

users = {
"name": "zia",      
"age": 24,
 "is_married": False,
 "is_student": True  
  }

 for attribute in users:
     print(attribute)
     
name      
age       
is_married
is_student


fruits = {
  "Dry_fruits": {"Almond": "brown", "Peanuts":"brown", "Cashews": "white"},
  "Green_fruits": {"Banana": "yellow", "orange": "orange", "peach": "red"}
}
print(fruits["Green_fruits"]["Banana"])
output: yellow

print(fruits.get("Dry_fruits", "Green_fruits"))
output: {'Almond': 'brown', 'Peanuts': 'brown', 'Cashews': 'white'}


students = ['Asim', 'Aleena', 'Mehreena','Ayoub']
default_status = 'pass'

new_record = dict.fromkeys(students, default_status)
print(new_record)
output: {'Asim': 'pass', 'Aleena': 'pass', 'Mehreena': 'pass', 'Ayoub': 'pass'}



       --------------Tuples--------------

tuple unwraping : 

persons = ("boy", "girl", "trans")
(boy, girl, trans) = persons

boy
output: 'boy'
trans
'output: trans'