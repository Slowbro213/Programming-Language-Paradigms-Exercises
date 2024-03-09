from math import sqrt

def perfect_abundant_deficient(n):
    if n == 1:
        return False
    sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            sum += i + n / i

    if sum>n:
        return "abundant"
    elif sum==n:
        return "perfect"
    else:
        return "deficient"


number = 28
print(perfect_abundant_deficient(number))
number = 20
print(perfect_abundant_deficient(number))
number = 14
print(perfect_abundant_deficient(number))