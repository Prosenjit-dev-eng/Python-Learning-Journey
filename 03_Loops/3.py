# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
n = input("Please give a number: ")
n_in_int = int(n)
for i in range(1,n_in_int+1):
    # bcz it is [1,n]
    if(i == 5): continue;  # Skip the fifth iteration
    multiply = n_in_int*i
    print(n_in_int, " * ", i, " = ", multiply)

