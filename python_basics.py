# to print hello world in python
print("Hello World")
# 

# Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.


# PYTHON DATATYPES

# a type is how python represents different types of data
# python has the following data types
# 1. int - integer number (whole number)
type(1) # int
# 2. float - floating point number. a float can be a whole number or a decimal number.
# type casting in python means converting a variable from one data type to another data type.
type(1.0) # float
# 3. str - string
type("hello") # string
# 4. bool - boolean.
# type casting in python means converting a variable from one data type to another data type.
type(True) # bool
# 5. list - list
type([1,2,3]) # list
# 6. tuple - tuple
type((1,2,3)) # tuple
# 7. dict - dictionary
type({"name": "John", "age": 30}) # dict
# 8. set - set  
type({1,2,3}) # set
# 9. complex - complex number
type(1+2j) # complex
# 10. bytes - bytes
type(b"hello") # bytes
# 11. bytearray - bytearray
type(bytearray(5)) # bytearray
# 12. memoryview - memoryview
type(memoryview(bytearray(5))) # memoryview
# 13. None - None
type(None) # None
# 14. range - range
type(range(5)) # range
# 15. frozenset - frozenset
type(frozenset({1,2,3})) # frozenset
# 16. Ellipsis - Ellipsis
type(Ellipsis) # Ellipsis
# 17. NotImplemented - NotImplemented
type(NotImplemented) # NotImplemented
# 18. Generator - Generator
type((i for i in range(5))) # Generator
# 19. Coroutine - Coroutine
def my_coroutine():
    yield from range(5)
type(my_coroutine()) # Coroutine
# 20. AsyncGenerator - AsyncGenerator
type((await i for i in range(5))) # AsyncGenerator
# 21. Module - Module
type(__import__("math")) # Module
# 22. Class - Class
class MyClass:
    pass
# 23. Function - Function
def my_function():
    pass
# 24. Method - Method
class MyClass:
    def my_method(self):
        pass
# 25. Code - Code
type((lambda x: x)) # Code
# 26. MethodDescriptor - MethodDescriptor
class MyClass:
    def my_method(self):
        pass
# 27. MemberDescriptor - MemberDescriptor
class MyClass:
    my_attribute = 1
# 28. GetSetDescriptor - GetSetDescriptor
class MyClass:
    @property
    def my_property(self):
        return 1
# 29. WrapperDescriptor - WrapperDescriptor
class MyClass:
    def __call__(self):
        pass

# 31. Frame - Frame
import inspect
frame = inspect.currentframe()
type(frame) # Frame
# 32. Traceback - Traceback
try:
    raise Exception("An error occurred")
except Exception as e:
    tb = e.__traceback__
    type(tb) # Traceback
# 33. Code - Code
type((lambda x: x).__code__) # Code 

# PYTHON EXPRESSIONS
# expressions are representations of value. 
# they are different from statements in the fact that statements do something while expressions are representation of value. 
# they are the operations that python performes
# 1. Expression - Expression
1 + 1 # 2
# 2. Expression - Expression
1 - 1 # 0
# 3. Expression - Expression
1 * 1 # 1
# 4. Expression - Expression
1 / 1 # 1.0
# 5. Expression - Expression
1 // 1 # 1 in this kind of division, the result is the integer part of the result of the division. it is usually rounded down.
# 6. Expression - Expression
1 % 1 # 0
# 7. Expression - Expression
1 ** 1 # 1
# 8. Expression - Expression
1 == 1 # True
# 9. Expression - Expression
1 != 1 # False
# 10. Expression - Expression
1 > 1 # False
# 11. Expression - Expression
1 < 1 # False

# PYTHON VARIABLES
# variables are containers for storing data values.
# variables are created when you assign a value to it.
# variables do not need to be declared with any particular type and can even change type after they have been set.
# the = operator is used to assign values to variables.
# 1. Variable - Variable
x = 1
# 2. Variable - Variable
y = 2
# 3. Variable - Variable
z = 3
# 4. Variable - Variable
a = 4
# 5. Variable - Variable
b = 5
# 6. Variable - Variable
c = 6

#  SRINGS IN PYTHON. a string is a sequence of characters and is enclosed in single or double quotes. 
# 1. String - String
"hello" # hello
# 2. String - String
'hello' # hello
# string concatenation
# 3. String - String
"hello" + "world" # helloworld
# 4. String - String
"hello" + " " + "world" # hello world
# 5. String - String
"hello" * 3 # hellohellohello
# 6. String - String
"hello"[0] # h
# 7. String - String
"hello"[1] # e
#  srings are immutable in python. this means that you cannot change the value of a string once it has been created.
# 8. String - String
"hello"[0] = "j" # TypeError: 'str' object does not support item assignment

# PYTHON STRING METHODS
# 1. String - String
"hello".capitalize() # Hello
# 2. String - String
"hello".upper() # HELLO
# 3. String - String
"hello".lower() # hello
# 4. String - String
"hello".title() # Hello
# 5. String - String
"hello".swapcase() # HELLO
# 6. String - String
"hello".casefold() # hello
# 7. String - String
"hello".center(20) #        hello

# PYTHON STRING FORMATTING
# 1. String - String
"hello {}".format("world") # hello world
# 2. String - String
"hello {0}".format("world") # hello world
# 3. String - String
"hello {name}".format(name="world") # hello world
# 4. String - String

# PYTHON STRING ESCAPE CHARACTERS
# 1. String - String
"hello \n world" # hello
# 2. String - String
"hello \t world" # hello    world
# 3. String - String
"hello \b world" # hello world
# 4. String - String
"hello \r world" # world
# 5. String - String
"hello \f world" # hello world
# 6. String - String
"hello \ooo world" # hello ooo world
# 7. String - String

# PYTHON STRING SCALING
# 1. String - String
"hello"[0:2] # he



# PYTHON DATA STRUCTURES
# data structures are containers that organize and group data types together in different ways. the following are called compound data types.
# 1. List - List
[1,2,3] # [1, 2, 3]
# 2. Tuple - Tuples are an ordered sequence. Tuples are written as comma-separated elements within parentheses.
# tuple concatinationa and repetition
# 3. Tuple - Tuple
(1,2,3) + (4,5,6) # (1, 2, 3, 4, 5, 6)
# 4. Tuple - Tuple
(1,2,3) * 3 # (1, 2, 3,
# 5. Tuple - Tuple
(1,2,3)[0] # 1
# 6. Tuple - Tuple
(1,2,3)[1] # 2
(1,2,3) # (1, 2, 3)
# 3. Set - Set
{1,2,3} # {1, 2, 3}
# 4. Dictionary - Dictionary
{"name": "John", "age": 30} # {'name': 'John', 'age': 30}
dict= {"A": 1, "B": 2, "C": [3,3,3], "D":(4,4,4), 'E':'name' 'John', 'age': 30}

# PYTHON DATA STRUCTURE METHODS
# 1. List - List
[1,2,3].append(4) # [1, 2, 3, 4]
# 2. List - List
[1,2,3].clear() # []
# 3. List - List

# CONDITIONS AND BRANCHING
# 1. Condition - Condition
if 1 == 1:
    print("yes") # yes
# 2. Condition - Condition
if 1 != 1:
    print("yes") # nothing printed
# 3. Condition - Condition
if 1 == 2:
    print("yes") # nothing printed
else:
    print("no") # no
# 4. Condition - Condition
if 1 == 2:
    print("yes") # nothing printed
elif 1 == 1:    
    print("no") # no
# 5. Condition - Condition
if 1 == 2:
    print("yes") # nothing printed
elif 1 == 3:
    print("no") # nothing printed
else:
    print("maybe") # maybe

# branching
# 6. Condition - Condition
if 1 == 2:
    print("yes") # nothing printed
elif 1 == 3:
    print("no") # nothing printed
elif 1 == 4:
    print("maybe") # nothing printed
else:
    print("yes")
# branching allows us to run different code depending on the conditions that are met.

age = 30
if age > 18:
    print("You are old enough to vote")
    print("You are not old enough to vote")

age = 30
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")

    # elseis statementes that are run when the if statement is false.

age = 30
if age >= 30:
    print("You are old enough to vote")
elif age == 18:
    print("You just started voting")
else:
    print("You are not old enough to vote")

# conditional statements are used to control the flow of the program.
# the if statement is used to run code if a condition is true.
# the elif statement is used to run code if the previous condition is false.
# the else statement is used to run code if the previous conditions are false.
album_year = 1983
album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
print("do something...")
# the code in the above example will run because the condition is true.
# the code in the else block will not run because the condition is false.
album_year = 1983
album_year = 1970
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("Album year is not greater than 1980")
print("do something...")
# the code in the above example will run because the condition is true.

# logical operators are used to combine conditional statements.
# the and operator is used to combine two conditions.
# the or operator is used to combine two conditions.
# the not operator is used to negate a condition.
album_year = 1980
if album_year > 1979 and album_year < 1990:
    print("Album year was in the 1980s")
# the code in the above example will run because the condition is true.
album_year = 1990
if album_year < 1980 or album_year > 1989:
    print("Album year was not in the 1980s")
# the code in the above example will run because the condition is true.
album_year = 1980
if not album_year == 1979:
    print("Album year is not 1979")
# the code in the above example will run because the condition is true.
# if else statement in continuation
# 7. Condition - Condition
if 1 == 2:
    print("yes") # nothing printed
elif 1 == 3:
    print("no") # nothing printed
elif 1 == 4:
    print("maybe") # nothing printed
else:
    print("yes")

    # Annie and jane were born in 1996 and 1999 respectively. write a code that will determine who is older.
Annie_born = 1996
Jane_born = 1999
if Annie_born < Jane_born:
    print("Annie is older than Jane")
else:
    print("Jane is older than Annie")
    # the code in the above example will run because the condition is true.
    # a code that will determine who was born in a leap year
Annie_born = 1996
Jane_born = 1999
if Annie_born % 4 == 0:
    print("Annie was born in a leap year")
elif Jane_born % 4 == 0:
    print("Jane was born in a leap year")

else:

    print("None of them was born in a leap year")

# in a school canteen, children under the age of 9 are only given molk porridge for breakfast. 
# those from 10 to 15 are given tea and those from 15 to 17 are given coffee. write a code that will determine what each child will be given for breakfast.
age = 10
if age < 9:
    print("milk porridge")

elif age >= 10 and age >= 15:
    print("tea")
elif age >=15 and age <= 17:
    print("coffee")
else:
    print("nothing")
    # the code in the above example will run because the condition is true.

# LOOPS
# 1. Loop - Loop
for i in range(5):
    print(i) # 0 1 2 3 4
# 2. Loop - Loop
for i in range(5):
    if i == 3:
        break
    print(i) # 0 1 2
# 3. Loop - Loop
for i in range(5):
    if i == 3:
        continue
    print(i) # 0 1 2 4
# 4. Loop - Loop
for i in range(5):
    if i == 3:
        pass
    print(i) # 0 1 2 3 4


# for loop examples
# 1. Loop - Loop
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])
# 2. Loop - example of a for loop to loop through a list
dates = [1982,1980,1973]
for year in dates:
    print(year)
# 3. Loop - Loop
for i in range(0, 8):
    print(i)

    # using the for loop to change the elements in the list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

    # using the for loop to iterate the elements in the list

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

    # Loop through the list and iterate the elements in the list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

#  solving if the real world problems using the for loop.
#  to will print the multiplication table of both 6 and 7
print ("Multiplication table of 6")
for i in range(1,11):
    print ("6 *", i, "=", 6 * i)
    
print ("Multiplication table of 7")
for i in range(1,11):
    print ("7 *", i, "=", 7 * i)


    # A for loop is used to iterate when there is a controlled flow of repetition
    # A for loop is used when you know how many times you want to repeat

    # while loop examples
    # in a while loop, the condition is checked before the block is executed.
    #  If the condition is true, the block is executed and then the condition is checked again. This process continues until the condition is false.
    # 1. Loop - Loop
i = 0
while i < 5:
    print(i)
    i += 1
    # 2. Loop - Loop
    count = 1
    while count <=5:
        print(count)
    count += 1
    # 3. Loop - Loop
    dates = [1982, 1980, 1973, 2000]
    i = 0
    year = dates[i]
    while i < len(dates):
        print(dates[i])
        i += 1

        # using the while loop to change the elements in the list
        dates = [1982, 1980, 1973, 2000]
        i = 0
        year = dates[0]

        while(year !=1973):
            print(year)
            i += 1
            year = dates[i]
        print("It took ", i ,"repetitions to get out of loop.")

#  a while loop to print the animals whose names are made of 7 characters. 
Animals = ["Lion", "Giraffe", "Gorilla", "Parrots", "Crocodile", "Elephant", "Monkey", "Tiger", "Zebra", "Kangaroo"]
New = []
i = 0
while i < len(Animals):
    if len(Animals[i]) == 7:
        New.append(Animals[i])
        i += 1
        print(New)


        

A = [1,2,3]
for a in A:
    print(2*a)


A = ['1','2','3']
for a in A:
    print(2*a)

x = 3
y = 1
while (y!=x):
    print(y)
    y = y + 1
