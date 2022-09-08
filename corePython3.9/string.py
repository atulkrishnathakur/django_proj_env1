# Single quotes string
message1 = 'This is a string in Python'
print(message1)

# String in double quotes
message2 = "This is also a string"
print(message2)

# If a string contains a single quote, you should place it in double-quotes like this
message3 = "It's a string"
print(message3)

# When a string contains double quotes, you can use the single quotes
message4 = '"Beautiful is better than ugly.". Said Tim Peters'
print(message4)

# To escape the quotes, you use the backslash (\). For example
message5 = 'It\'s also a valid string'
print(message5)

# The Python interpreter will treat the backslash character (\) special. If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote. For example
message6 = r'C:\python\bin'
print(message6)

# Creating multiline strings
message7 = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
print(message7)

# Using variables in Python strings with the f-strings
name = "Atul"
message8 = f"Hi {name}"
print(message8)

# Concatenating Python strings
greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

# Accessing string elements
str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

# Getting the length of a string
str = "Python String"
str_len = len(str)
print(str_len)

# Slicing strings
str = "Python String"
print(str[0:2])

# Python strings are immutable. It means that you cannot change the string. For example, you’ll get an error if you update one or more characters in a string:
str = "Python String"
str[0] = 'J'

