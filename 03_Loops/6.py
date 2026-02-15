# Problem: Compute the factorial of a number using a while loop.
n = input("Please give me a number: ")
n_in_int = int(n)
fact = 1
while n_in_int>0:
    fact*=n_in_int
    n_in_int-=1


print("Factorial",fact)