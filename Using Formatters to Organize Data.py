for i in range(3,13):
    print(i, i*i, i*i*i)

# Let’s use formatters to give more space to these numbers:
for i in range(3, 13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))