import re
exp = input("Enter a string: ")
x = re.fullmatch("\d{10}", exp)
if x:
    print("This is a phone number")
else:
    print("This is not a phone number")