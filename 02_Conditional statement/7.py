# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
order_Size = input("Enter your order: ")
extra_shot = True

if extra_shot:
    coffee =  order_Size + " coffee with an expresso"
else: 
    coffee = order_Size + " coffee"
print("Order: ",coffee)