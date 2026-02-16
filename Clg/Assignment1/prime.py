limit = int(input("Generates primes up to: "))
def primegen(limit):
    for num in range(2,limit + 1):
        isP = True
        for i in range(2, num):
            if num%i == 0:
                isP = False
                break
        if isP:
            yield num
x = primegen(limit)
print(list(x))
