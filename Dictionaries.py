sammy = {'username': 'sammy shark', 'online': True, 'followers': 999}
print(sammy)

# Accessing Dictionary Elements
'''
Because the dictionary data structure is unordered, we cannot call its
values by an index number, as we can with lists and tuples. We can,
however, call its values by referencing the related keys.
'''

# 1 Accessing Data Items with Keys
print(sammy['username'])

# 2 Using Functions to Access Elements
print(sammy.keys()) # return keys
print(sammy.values()) # return values
print(sammy.items()) # return items
 


jesse = {'username': 'JOctopus', 'online': False,
'points': 723}
 
for common_keys in sammy.keys() & jesse.keys():
    print(sammy[common_keys], jesse[common_keys])


# getting key and value

for key, value in sammy.items():
    print(key, "is The key for the value ", value)