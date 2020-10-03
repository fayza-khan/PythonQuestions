# Sum of digits of a number
"""
def count_number(x):
    list1 = [y for y in x]
    for i in list1:
        sum1 = 0
        sum1 += list1[i]
        return sum1


print(count_number(237))
"""


def get_sum(n):
    sum1 = 0
    while n != 0:
        sum1 += n % 10
        n = int(n / 10)
    return sum1


print(get_sum(237))
print(get_sum(8907))
print(get_sum(23157))


# Sum of squares of digits of a number


def sum_of_squares(x):
    sum2 = 0
    while x != 0:
        sum2 += (x % 10)**2
        x = int(x/10)
    return sum2


print(sum_of_squares(12))
print(sum_of_squares(33))


# Prime number

def check_prime(x):
    sum3 = 0
    for i in range(1, x):
        if x % i == 0:
            sum3 += 1
    if sum3 == 1:
        sum3 = 0
        return x
    else:
        return False


print(check_prime(23))
print(check_prime(22))


# factorial of a number
def is_factorial(w):
    prod = 1
    for i in range(1, w+1):
        prod *= i
    return prod


print(is_factorial(3))
print(is_factorial(5))


def is_fact(x):
    prod = 1
    y = []
    while x != 0:
        n = x % 10
        x = int(x / 10)
        y.append(n)
    for i in y:
        for k in range(1, i+1):
            prod *= k
    return prod


print(is_fact(23))
print(is_fact(65))


def get_count(n):
    y = []
    while n != 0:
        sum1 = n % 10
        n = int(n / 10)
        y.append(sum1)
    return y[::-1]


print(get_count(531))





