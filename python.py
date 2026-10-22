# Python standard library 
import math as m 
print(m.factorial(6))
list_a = ['pow', 'sqrt', 'cbrt', 'exp', 'exp2', 'expm1', 'log', 'log2', 'log10', 'log1p']

'''Collection of predefined utilites is called the Python standard library. It includes modules 
for various tasks such as mathematics, file I/O, system calls, and more. The `math` module, 
for example, provides functions for mathematical operations like factorial, power, square root, 
and logarithms.'''
a = int(input('Enter a number: '))
fact = 1
for i in range(1,a+1):
    fact *= i 
print(fact)