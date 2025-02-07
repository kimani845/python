
# functions
# functions are a block of code that only runs when it is called.
# you can pass data, known as parameters, into a function.
# a function can return data as a result.
# 1. Function
def my_function():
    print("Hello from a function")
# 2. Function
def my_function():
    return "Hello from a function"
# 3. Function
def my_function():
    pass
#  the len function returns the length of an object.
# 4. Function
def my_function():
    return len("hello")
# 5. Function
def my_function():
    return len([1,2,3])
# 6. Function
def my_function():
    return len((1,2,3))
# sorting
# 7. Function
def my_function():
    return sorted([3,6,8,10,1])
# 8. Function
album_rating = {"Thriller": 5, "Back in Black": 4, "The Dark Side of": 3 }
sorted_album_rating = sorted(album_rating) #in this case there is no diff in the album album_rating
# 9. Function
def my_function():
    return sorted(album_rating, key=lambda x: x[1], reverse=True)

# the following sort() function sorts the album by rating in descending order
# 10. Function
album_rating = {"Thriller": 5, "Back in Black": 4, "The Dark Side of": 3}
sorted_album_rating = dict(sorted(album_rating.items()))
print(sorted_album_rating)

# Sorting by using values

sorted_by_rating = dict(sorted(album_rating.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_rating)

# making a function
# 11. Function
def album_rating(ratings):
    return sorted(ratings, key=lambda x: ratings[x], reverse=True)

# Example usage
ratings = {"Thriller": 5, "Back in Black": 4, "The Dark Side of": 3}
sorted_ratings = album_rating(ratings)
print(sorted_ratings)

# an example of a scope local variable

def Thriller():
    Date = 1982
    return (Date)
Date = 2017
print(Thriller()) # prints 1982
print (Date) # prints 2017

# an example of a global scope

    # can either be defined here or before the return type (ClaimedSales = 100)  # Define the global variable can 

def PinkFloyd():
    global ClaimedSales
    ClaimedSales = 100  # Define the global variable
    return ClaimedSales

PinkFloyd()
print(ClaimedSales)  # prints 100

# an example of a nonlocal scope
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        inner()
# examples
def f (a, b):
    return a * b # returns the product of a and b

a = 5
b = 3
if a*b == f(a, b):
    print("The product of a and b is correct") # prints "The product of a and b is correct
else: 
    print("The product of a and b is incorrect") # prints "The product of a and b is incorrect

# a function of g such that
def g (x):
    return sum(x) # returns the sum of the elements in the list x
# examples
x = [1, 2, 3, 4, 5]
if sum(x) == g(x):
    print("Correct")
else:
    print("Incorrect")

# function to add 1 to a and store as b
def add_one(a):
    b = a + 1
    print (a, "if you are", b)
    return (b)
#  a function to multiply two numbers
def multiply(a, b):
    c = a * b
    return c
print ("This is not printed")
result =multiply (5, 6)
print(result) # prints 30


# Variables. 
#  a function that is called inside a function is called a local variable. the parameter only exists within the function.
# A variable that is declared outside a function definition is a global variabme and its value is accessible and modifiable throughout the program
def square():
    # local variable
    b =1 
    c = b * b + a 
    print (b, "if you square + 1", a)
    return a

# initializes a global variable

x = 3
# makes the function call and return a y
y = square(x)
y

def MJ():
    print('The King of Pop is ' + MJ)

def MJ1():
    print ('The King of Pop is ' + MJ1)

    return (None)
print (MJ())
print (MJ1()) # prints None
#  functions makes things simpler. consider block 1 and block 2 below
#  a and b  calculation module

# block 1:

a1 = 4
a2 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if (c1< 0):
    c1 = 0

else: 
    c1 = 5
c1 

# block 2:

a2 =0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if (c2 < 0):
    c2 = 0
else:
    c2 = 5
c2
# a function can be used to replace the lines of code.  A function combine many instructions to a single line of code.
# once a function is called, it can be used repeatedy. you can invoke the same functiob many times in your program. you can also save your function and use it in another program.

#  make a function for the calculation above.
def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if (c < 0):
        c = 0
    else:
        c = 5
        return c # this function takes two inputs and then applies several operations to return c. you can call this function multiple times in your program.

# Using the if/else statementts and loops in Functions
# function example
def type_of_album(artist, album, year_released):
    print (artist, album, year_released)
    # calling the function
    if year_released > 1980:
        return "Modern"
    else:
        return "Classic"
    x = type_of_album("Michael Jackson", "Thriller", "1980")
    print (x) # prints Classic

# print using the for loop
def printList(the_list):
    # impplementation of the element function
    printList (['1', 1, 'the man', "abc"])
    for element in the_list:
        print(element)
# String comparison in functions
# compare two strings usin in operator

# add string

# define a function
string = "Michael Jackson is the best"

def check_string(text):

    # using the if/else statement and in operator to compare the strings
    if text in string:
        return 'String Matched'
    else:
        return 'String Not Matched'

print(check_string("Michael Jackson is the best"))

# comparing two springs using the == operator
def compareStrings (x,y):
    if x==y:
        return 1
    string1 = "Michael Jackson is the best"
    string2 = "Michael Jackson is not the best"
    # declare a variable to store the results after comparing the strings
    check = compareStrings(string1, string2)
    # comparing the string using the if else statements
    if check == 1:
        print ('\nString Matched')
    else:
        print('\nString not Matched')

        # this line of code shoul have an output but it doesnot have one 

# PYTHON PROGRAM TO COUNT WORDS IN A STRING USING A DICTIONARY
def freq (string):
    # step1: a list vaviable is declared and initialized to an empty 
    words =[]
    # step2: break the string into a  list of words
    words = string.split() # or string.lower().split
    # step3: declare a dictionary
    Dict = {}
    # step4: use the for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        # step5: print the dictionary
    print ("The Frequency of words is:", Dict)
# step6: call a function and pass in it
freq("Mary had a little lamb little lamb, little lamb Mary had a little lamb. its fleece was white as snow and everywhere that Mary went Mary went , Mary went \ Everywhere that Mary went The Lamb was sure to go")

#  setting default argument values in your custom function
# example for setting param with default value
def isGoodRating(rating=4):
    if rating >= 4:
        print ("this album sucks it's rating is", rating)

    else: 
        print ("this album is good it's rating is", rating)

# GLOBAL VARIABLES
# example of using global variable
artist = "Michael Jackson"
def printer1 (artist):
    global internal_var1 # introduction of a global variable
    # internal_var1 = artist
    internal_var1 = "Michael Kimani"
    print(artist, "is the best artist")
printer1 (artist)
printer1 (internal_var1)

# SCOPE OF A VARIABLE
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 5.0
    else:
        return 0.0
    
print ("AC/DC's ratings is:", getBandRating("AC/DC"))
print ("Deeep Purple's ratings is:", getBandRating("Deep Purple"))
print ("My favourite band is:", myFavouriteBand)

# deleting variable 'myfavouriteband ' from the previous example demonstrates an example of a local variable
del myFavouriteBand
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 5.0
    else:
        return 0.0
    
print ("AC/DC's ratings is:", getBandRating("AC/DC"))
print ("Deeep Purple's ratings is:", getBandRating("Deep Purple"))
print ("My favourite band is:", myFavouriteBand)
# 
# example of a global and local variable with the same name
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    myFavouriteBand = "Deep Purple" # local variable
    if bandname == myFavouriteBand:
        return 5.0
    else:
        return 0.0
    
print ("AC/DC's ratings is:", getBandRating("AC/DC"))
print ("Deeep Purple's ratings is:", getBandRating("Deep Purple"))
print ("My favourite band is:", myFavouriteBand)

# COLLECTIONS AND ARGUMENTS
def printAll (*args): # *args is a variable number of arguments. all arguments are 'packed' into args and treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
        # PrintAll with three arguments
        printAll("Hello", "World", "Python", "Programming")
        #printAll with four arguments
        printAll("Hello", "World", "Python", "Programming", "is", "fun") # this code is not displaying the output but it is supposed to 
#  the arguments can be also packed in a dictionary
def printDictionary(**args):
    for key in args:
        print(key, ":", args[key])
    printDictionary (name="John", age=30, city="New York") # this code is not displaying the output but it is supposed to

# functions can be incredibly powerful and versatile. they can accept (and return) data types, objects and even other functions as arguments
def addItems(list):
    list.append("Apple")
    list.append("Banana")
myList = ["Orange", "Mango"]
addItems(myList)
print(myList) # this code is displaying the output as it is supposed to
#  the con function is used to add two integers or strings together
def con (a, b): # con is short for concatenate
    return a + b 
# it can  also be used to add lists and also tuples
con (['a', '3'], ('b', '4'))