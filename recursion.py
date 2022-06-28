def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


# 5 * (4 * (3 * (2 * (1)))) = 120
print(factorial(5))
