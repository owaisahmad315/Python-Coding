fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

# another example

number_list = [ x**2 for x in range(10) if x % 2 == 0]
print(number_list)

# another nested if

number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)

# another example
my_list = []
for x in [20, 40, 60]:
    for y in [2,4,6]:
        my_list.append(x * y)
print(my_list)

# using list comprehension

my_list = [ x * y for x in [20, 40, 60] for y in [2,4,6]]
print(my_list)


mytuple = ('1','2','3')
mytuple2 = ('4','5','6')
print(mytuple + mytuple2)

print(mytuple[-3:-1])


coral = ('blue coral', 'staghorn coral', 'pillar','coral', 'elkhorn coral')

print(coral[-3:-1])
print(coral[1::2])  # stride


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(numbers[1:11:2]) # stride 
