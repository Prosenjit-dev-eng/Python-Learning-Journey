#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()
for fruits in items:
    if(items.count(fruits)>1):
        print("The duplicate fruit is: ",fruits)
        break
    else:
        unique_item.add(fruits)
