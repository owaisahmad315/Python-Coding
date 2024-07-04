mytuple = ('1','2','3')
mytuple2 = ('4','5','6')
print(mytuple + mytuple2)

print(mytuple[-3:-1])

 # stride
coral = ('blue coral', 'staghorn coral', 'pillar','coral', 'elkhorn coral')
print(coral[-3:-1])
print(coral[1::2]) 



numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(numbers[1:11:2]) # stride 

# concatenation and multiplication
kelp = ('wakame', 'alaria', 'deep-sea tangle','macrocystis')
coral_kelp = (coral + kelp)
print(coral_kelp)

# multiply
multiplied_coral = coral * 2
print("multiplied coral", multiplied_coral)
multiplied_kelp = kelp * 3
print("multiplied kelp", multiplied_kelp)


