# Problem: Calculate the sum of even numbers up to a given number n.
n = input("Please give a number: ")
n_in_int = int(n)
sum_even = 0;
for i in range(1,n_in_int+1):
    # bcz it is [1,n]
    if(i%2 == 0): sum_even+=1;

print("Sum = ",sum_even)
