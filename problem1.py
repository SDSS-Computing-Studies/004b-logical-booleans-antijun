"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

inputnumber = input("Enter a number: ")
a = int(inputnumber)

if a % 8 == 0:
    print(inputnumber + " is not frue.")
elif a % 6 == 0:
    print(inputnumber + " is frue.")
