#join lists
list1 = ['apple', 'banana', 'peach', 'cherry', 'cherry']
list2 = ['jam', 'kheer', 'sweet', 'desert', 'dish']
joinLists = list1 + list2
print(joinLists)

#output = ['apple', 'banana', 'peach', 'cherry', 'cherry', 'jam', 'kheer', 'sweet', 'desert', 'dish']

#join lists using loop

list1 = ['apple', 'banana', 'peach', 'cherry', 'cherry']
list2 = ['jam', 'kheer', 'sweet', 'desert', 'dish']

for x in list2:
  list1.append(x)
print(list1)