# Converting to Tuples
'''
You can use the methods list() and tuple() to convert the values
passed to them into the list and tuple data type respectively. In Python: -
a list is a mutable ordered sequence of elements that is contained within
square brackets [ ]. - a tuple is an immutable ordered sequence of
elements contained within parentheses ( ).
'''
print(tuple(['pull request', 'open source', 'repository', 'branch']))
sea_creatures = ['Shark', 'CuttleFish', 'squid', 'mantis shrimp']
print(tuple(sea_creatures))

# Converting to lists
print(list(('blue coral', 'staghron coral', 'piller colar')))
# or use variable for the tuple values
coral = ('blue coral', 'staghron coral', 'piller colar')
print(list(coral))
# We can convert strings to list as well
print(list("shark"))