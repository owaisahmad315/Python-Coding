def new_func():
    ss = "Sammy Shark!"
    return ss

ss = new_func()
print(len(ss))
print(ss[6:11])
print(ss[:4])
print(ss[4:])

print(ss[-4:-1])
# stride 
print(ss[0:12:2])
print(ss[::-2])