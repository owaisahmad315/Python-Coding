# Converting Numbers to Strings
'''
 To convert the integer 12 to a
string value, you can pass 12 into the str() method:
'''
num = 12
str(num)
print(type(12))


user = "Sammy"
lines = 50
print("Congratulations, " + user + " you wrote " + str(lines) + " lines of code.")


#Converting Strings to Numbers

lines_yesterday = "50"
lines_today = "108"

lines_more = int(lines_today) - int(lines_yesterday)
print(lines_more)
