# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
password = input("Enter Password: ")
length = len(password)
print(length)
if (length <= 5):
    print("Invalid")
elif (length < 6):
    print("Weak")
elif(length >= 6 and length<10):
    print("Medium")
else:
    print("Strong")