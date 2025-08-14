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


-----------Exponential Backoff---------

Exponential Backoff is a retry strategy used when a request (like to a server or API) fails.
Instead of retrying immediately or at a fixed delay, it waits longer and longer between retries.

🔍 How it works
First retry: wait a short time (e.g., 1 second)

Second retry: wait more (e.g., 2 seconds)

Third retry: wait even more (e.g., 4 seconds)

Delay grows exponentially (1, 2, 4, 8, 16 … seconds) until success or max retries.

🛠 Why use it?
Prevents overloading the server when there’s an error or high traffic.

Gives the system time to recover.

Common in APIs, network requests, cloud services, etc.


#--------------iteration_tools---------------

>>> mylist = [1,2,3,4,5]
>>> I = iter(mylist)
>>> I
<list_iterator object at 0x0000024636D693F0>    
>>> I.__next__()
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
5
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>  
    I.__next__()
StopIteration



#---------------------------function greet user if user not found greet with default name----------

# def greet(user ='zia'):
#   return user

# print(greet())


#-----------lambda function--------------

cube = lambda x: x**3
print(cube(3))

#---------**kwargs------

The special syntax **kwargs in function definitions is used to pass a variable length argument list. We use the name kwargs with the double star **.

A keyword argument is where you provide a name to the variable as you pass it into the function.
It collects all the additional keyword arguments passed to the function and stores them in a dictionary.

  Example:
          def result_card(**kwargs):
              for key, value in kwargs.items():
              print(f"{key} : {value}")


result_card(name = 'zia', marks = 89 )

output: name : zia
marks : 89


#--------------Recursion----------
        def factorial(num):
          if num == 0 or num == 1:
            return 1
          else:
            return num * factorial((num - 1))

        num = 5
        print(f"factorial of {num} is {factorial(num)}")

        Step-by-step breakdown:
                  factorial(5)

                → 5 * factorial(4)
                    → 4 * factorial(3)
                        → 3 * factorial(2)
                            → 2 * factorial(1)
                                → 1  → Base case reached

        Now we return step by step
                factorial(1) → returns 1
                factorial(2) → 2 * 1 = 2
                factorial(3) → 3 * 2 = 6
                factorial(4) → 4 * 6 = 24
                factorial(5) → 5 * 24 = 120




#---------ENCLOSURE---------

What is Enclosure in Python?
An enclosure happens when a function is defined inside another function, and the inner function remembers the variables from the outer function even after the outer function has finished running.

This is part of Python’s LEGB rule:

Local

Enclosing

Global

Built-in

✅ Example of Enclosure
def outer():
    msg = "Hello from outer!"

    def inner():
        print(msg)  # ← accesses 'msg' from outer scope (enclosure)

    return inner
Now when you call:

greet = outer()
greet()  # prints: Hello from outer!
Even though outer() has finished running, inner() still remembers the value of msg — this is because of enclosure.

the reason we store the outer() function's return value in a variable (like greet) is:

 So we can keep and use the inner() function later, even after outer() has finished running.


#--------CLASS AND OBJECT WITH CONSTRUCTOR----------


class Car:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    

c1= Car('pijaro', 2021)
print( c1.brand,':' ,c1.model)



#--------------------- ENCAPSULATION------------

keeping things private means only accessabale inside class...


getter:
A getter is simply a method that returns the value of a (usually private) attribute.
    EXAMPLE:
    def get_brand(self):
    return self.__brand    #__ makes attribute private



#----------POLYMORPHISM-----------

Polymorphism in simple terms
"One interface, multiple forms."
Same method name, but it behaves differently depending on which object is calling it.
    EXAMPLE:
  class Car:
    def fuel_type(self):
        return "Petrol or Diesel or CNG"

  class ElectricCar(Car):
    def fuel_type(self):
        return "Electric charge"

#----------STATIC METHOD---------

 a static method is a method that belongs to a class but does not operate on an instance of that class or the class itself. Unlike instance methods, static methods do not receive an implicit self (instance) or cls (class) argument. 
    EXAMPLE:

          class MyClass:
            @staticmethod
            def my_static_method(arg1, arg2):
                # This method does not access instance or class attributes
                return arg1 + arg2


#------------------DECORATORS---------

def func_debug(func):
  def wrapper(*args, **kwargs):
    args_values = ', '.join(str(arg)for arg in args)
    print(f"Calling: {func.__name__}() with args {args_values}")
    return func(*args, **kwargs)
  return wrapper


@func_debug
def greet(name, greeting = 'Hello'):
  print(f"{greeting}, {name}")

greet('zia', "welcome")

:..HERE
    func_debug(greet) returns wrapper

    wrapper remembers func (the original greet) because of closure

    greet now points to wrapper

:-  Key connection:

  Both closures and decorators depend on an inner function remembering variables from the outer function.

  The main difference:

  A closure is about returning a function that keeps state.

  A decorator is about replacing a function with a wrapped version that adds behavior.



