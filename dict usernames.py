# define orignal dictionary

usernames =  {'Sammy': 'sammy-shark', 'Jamie':
'mantisshrimp54'}

# Set up while loop to iterate
while True:
    print("Enter a name: ")

    name = input()

    if name in usernames:
        print(usernames[name] + "is the username of " + name)
    else:
        print("i don't have " + name + " username in")

    print("Enter a name: ")

    username = input()
    usernames[name] = username
    print("Data Updated")



