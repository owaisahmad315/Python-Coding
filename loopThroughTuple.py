thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)


""" 
 Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable. 
"""

thisTuple = ("apple", "banana", "cherry")
for i in range(len(thisTuple)):
    print( "looping using index numbers " + thisTuple[i])



# Using a While Loop
thisTuple = ("apple", "banana", "cherry")
i = 0
while i < (len(thisTuple)):
    print("using while loop " + thisTuple[i])
    i += 1