from math import sqrt

def Value_of_a_func1on(n):
    return format(Value_of_a_func1onhelper(n,1),'.3f')


def Value_of_a_func1onhelper(n,m):
    if(n==m):
        return sqrt(m*m*m)

    return sqrt(m*m*m + Value_of_a_func1onhelper(n,m+1))

n=3
print(Value_of_a_func1on(n))
