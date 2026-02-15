# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = input("Enter your age: ")
# python always gives string input
# convert to int
age_in_int = int(age)
price = 0
day = input("Day: ")
if age_in_int >= 18:
    price = 12

else: 
    price = 8

if(day == "Wednesday"): price-=2
print("The price in $: ", price)
# Shortcut
# price = 12 if age >= 18 else 8

