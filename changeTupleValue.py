#Convert the tuple into a list to be able to change it:


x =("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)
print(y)