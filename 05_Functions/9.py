# Problem: Write a generator function that yields even numbers up to a specified limit.
def even_gen(limit):
    """Generator function that yields even numbers up to a specified limit."""
    for num in range(2, limit + 1, 2):
        yield num

print("Even numbers up to 10:")
for num in even_gen(10):
    print(num, end=' ')  # Output: 2 4 6 8 10