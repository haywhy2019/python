# python3 -i lecture1.py
from urllib.request import urlopen
from doctest import testmod
# from doctest import run_docstring_examples
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

# doc string

def pressure(v,t,n):
    """Compute the pressure in pascals of an ideal gas.
    Applies the ideal gas law
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particules of gas
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v
    """

# help(pressure)

def square(x):
    return x * x

def sum_naturals(n):
    """Return the sum of the first n natural numbers
    
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total
    
testmod()
# run test globally[all test in the file]
# When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

# python3 -m doctest <python_source_file>

# run_docstring_examples(sum_naturals, globals(), True)
