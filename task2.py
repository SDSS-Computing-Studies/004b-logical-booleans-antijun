#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

a = int(input("Enter a number: "))
b = math.sqrt(a)
c = a ** 1/3

if int(b + 0.5) ** 2 == a and a ** 1/3 == c:
    print(str(a) + " is both a perfect square and a perfect cube.")
elif int(b + 0.5) ** 2 == a:
    print(str(a) + " is only a perfect square.")
elif a ** 1/3 == c:
    print(str(a) + " is only a perfect cube.")
