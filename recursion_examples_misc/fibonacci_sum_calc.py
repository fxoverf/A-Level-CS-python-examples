def fibonacci(n):
    if n <= 0:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result
result = fibonacci(5)
print(result - 1)
