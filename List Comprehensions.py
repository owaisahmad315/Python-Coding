# List Comprehensions
# list_variable = [ x for x in iterable ]

shark_letters = [ letter for letter in "shark"]
print(shark_letters)

shark_letters = []
for letter in 'shark':
    shark_letters.append(letter)
print(shark_letters)