def factorial(n):
    print(n)
    if n == 0:
        return 1

    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
fact = factorial(5)
print(fact)
