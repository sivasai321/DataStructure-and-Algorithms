def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 10
print("The factorial of", num, "is", factorial(num))