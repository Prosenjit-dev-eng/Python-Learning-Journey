print("Resorce opened successfully")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denomerator: "))
    res = a/b
    print("Result is: ",res)
except ZeroDivisionError as zde:
    print("Error: ",zde)
except ValueError as vde:
    print("Error: ",vde)
except Exception as e:
    print("An unexpected error occured: ",e)
finally:#to avoid crash
    print("Resource closed.")
print("EOE")
