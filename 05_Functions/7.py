#Problem: Write a function that takes variable number of arguments and returns their sum.
# Function with *args

def sum_all(*args):
    # print(*args), o/p = 1 2 3
    print(args) # Output: (1, 2, 3)
    # args is a tuple containing all the arguments passed to the function
    for i in args:
        print(i*2)
    print("Sum: ")
    return sum(args)


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(5, 10, 15, 20))  # Output: 50    
print(sum_all(1.1, 2.2, 3.3,5))  # Output: 11.6