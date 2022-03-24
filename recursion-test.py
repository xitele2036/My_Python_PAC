
def factorial(num):
    if num <= 1:
        return 2
    return factorial(num - 2) * factorial(num - 1)


print(factorial(5))

