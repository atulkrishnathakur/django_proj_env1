# ******** "is" Returns True if both variables are the same object **********

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x == y)


# ******** "is not" Returns True if both variables are not the same object *********

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns False because z is the same object as x
print(x is not z)

# returns True because x is not the same object as y, even if they have the same content
print(x is not y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print(x != y)
