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
        