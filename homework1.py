# controls
from operator import add,sub
from doctest import testmod
# https://inst.eecs.berkeley.edu/~cs61a/fa21/hw/hw01/
# Q2: A Plus Abs B
# Fill in the blanks in the following function for adding a to the absolute value of b, without calling abs. You may not modify any of the provided code other than the two blanks.
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

# testmod()

# Q3: Two of Three
# Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers. Use only a single line for the body of the function.
def square(x):
    return x * x

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return min(add(square(x), square(y)), add(square(x), square(z)), add(square(y), square(z)))
    # return  add(square(x), square(y)) if max(x,y,z) == z  else add(square(x), square(z)) if max(x,y,z) == y else add(square(y), square(z))
# Hint: Consider using the max or min function:


# >>> max(1, 2, 3)
# 3
# >>> min(-1, -2, -3)
# -3


# Q4: Largest Factor
# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    def findPrime(num):
        n = 1
        k = num/n
        if(num % n != 0):
          n + 1
        return k

    while n > 1:
        k = findPrime()

#     "*** YOUR CODE HERE ***"
# Hint: To check if b evenly divides a, you can use the expression a % b == 0, which can be read as, "the remainder of dividing a by b is 0."