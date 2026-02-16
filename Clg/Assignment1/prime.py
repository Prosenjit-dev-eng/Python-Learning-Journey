limit = int(input("Generates primes up to: "))
def primegen(limit):
    for num in range(2,limit + 1):
        isP = True
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                isP = False
                break
        if isP:
            yield num
x = primegen(limit)
print(list(x))
