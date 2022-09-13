# if example:
v1 = 18
if(v1 >= 18):
    print("You are eligile to vote")
    print("Let's go and vote")

# If you don’t use the indentation correctly, the program will work differently. For example:
# last statement will always execute because it is not in if block
age = 15
if int(age) >= 18:
    print("You're eligible to vote.")
print("Hello India")

# if_else example:
age = 14
if int(age) >= 18:
    print("You're eligible to vote........")
else:
    print("You're not eligible to vote.......")

# if_elif_else example:
your_age = 9
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# show the ticket price
print(f"You'll pay Rs. {ticket_price}/- for the ticket")
