def fib(n):
    a, b = 0, 1
    cnt = 0
    while cnt < n:
        yield a
        # every time we only print a
        a, b = b , a + b
        cnt+=1
f = fib(7)
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 
print(next(f)) 

