# a class has instances and attributes that makes it a class
# an instace of an object is the realization of a class
# an attribute is a property of an object
# a method is a function that belongs to an object
# a class is a blueprint or a template for creating objects
# a class can have methods and attributes
# a class can inherit from another class
# a class can have multiple inheritance
# a class can have polymorphism
# a class can have encapsulation
# a class can have abstraction
# methods in a class will give a way to change an object and also the interaction of that object. they are typically functions that interact with the objects.

# creating a class
# import matplotlib.pyplot as plt
# % matplotlib inline 

# create a class Circle
class Circle(object):
    # constructor
    def __init__(self, radius = 3, color = 'red'):
        self.radius = radius
        self.color = color
    # method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius
    # method
    def drawCircle(self):
        plt.gca().add.patch( plt.Circle((0,0), radius=self.radius, fc =self.color))
        plt.axis('scaled')
        plt.show()    
        
# creating an instance of a class
RedCircle = Circle(10, 'red')
# methods that can be used on the object RedCircle.
dir(RedCircle)
RedCircle.radius # print the radius
RedCircle.color # print the color
# set the object attribute radius
RedCircle.radius = 1
RedCircle.radius
# calling the method DrawCircle
RedCircle.drawCircle()


# use method to change the object attribute radius
print('Radius of object:' , RedCircle.radius)
RedCircle.add_radius(2)
print ('Radius of object after calling method add_radius(2):' , RedCircle.radius)
RedCircle.add_radius(5)
print ('Radius of object after calling method add_radius(5):' , RedCircle.radius)
RedCircle.drawCircle
# CLASS RECTANGLE

class Rectangle(object):
    # Constructor
    def __init__(self, width=2, height=3, color= 'r'):
        self.height = height
        self.width = width
        self.color = color
    # method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), width=self.width, height=self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()
# create a new object of Rectangle class
SkinnyBlackRectangle = Rectangle(2, 3, 'black')   \
    # the attributes of the new class     
SkinnyBlackRectangle.height 
SkinnyBlackRectangle.width
SkinnyBlackRectangle.color

# drawing the rectangle
SkinnyBlackRectangle.drawRectangle()

# create a new object rectangle
FatYellowRectangle = Rectangle(242, 112, 'yellow')
FatYellowRectangle.height
FatYellowRectangle.width
FatYellowRectangle.color

FatYellowRectangle.drawRectangle()