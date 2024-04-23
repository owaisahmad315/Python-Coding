'''
Formatters work by putting in one or more replacement fields or
placeholders — defined by a pair of curly braces {} — into a string and
calling the str.format() method. You’ll pass into the method the
value you want to concatenate with the string. This value will be passed
through in the same place that your placeholder is positioned when you
run the program.
'''

print("Sammy has {} ballons.".format(5))

'''
We can also assign a variable to be equal to the value of a string that
has formatter placeholders:
'''
open_string = "Sammy loves {}"
print(open_string.format("open source"))


#Specifying Type
'''
We can include more parameters within the curly braces of our syntax.
We’ll use the format code syntax {field_name:conversion}, where
field_name specifies the index number of the argument to the
str.format()
'''
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))

# Padding Variable Substitutions
print("Sammy has {0:<4} red {1:^19}!".format(5, "balloons"))