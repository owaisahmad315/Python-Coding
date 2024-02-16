class Myclass:
    x = 5
print(Myclass)

# create object
p1 = Myclass()
print(p1.x)

# The __init__() Function
'''
Use the __init__() function to assign values to object properties, 
or other operations that are necessary to do when the object is being created:
'''

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('owais', 24)
print(p1.name)
print(p1.age)


# The __str__() Function

"""
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"{self.name}({self.age})")

p1 = Person("owaiss", 33)
print(p1)


# Object Methods

"""
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
"""      

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()