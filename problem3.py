#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

list1 = [a, b, c]
if a == min(list1) and c == max(list1):
    middle = b
elif c == min(list1) and a == max(list1):
    middle = b
elif b == min(list1) and c == max(list1):
    middle = a
elif c == min(list1) and b == max(list1):
    middle = a
elif a == min(list1) and b == max(list1):
    middle = c
elif b == min(list1) and a == max(list1):
    middle = c

if min(list1)**2 + middle**2 == max(list1)**2:
    print(str(min(list1)) + "," + str(middle) + "," +
          str(max(list1)) + " form a Pythagorean triple")
else:
    print(str(min(list1)) + "," + str(middle) + "," +
          str(max(list1)) + " do not form a Pythagorean triple")
