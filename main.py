# Advanced Problem Set: Delving Deeper with Numbers in Python

#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.
print("reptest")
the3=3
the6=6
the5=5
the4=4
the7=7
result=(5+4)
print(the3+the6*result/the3-the7)
# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
the145=145
the12=12
print(145%12)
# Task 3: Raise 7 to the power of 3 and print the result.
the7=7
the3=3
print(the7**the3)
#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.
print(max(numbers))
print(min(numbers))
# Task 5: Round the number 12.5678 to 2 decimal places.
the12smthn=12.5678
print(round(the12smthn, ndigits=2))
# Task 6: Find the absolute value of -45.
neg45=-45
print(abs(neg45))
#################### PROBLEM 3: Advanced Math Functions ####################
import math

# Task 7: Using the math library, find the floor value of 15.7.
the15smthn=15.7
print(math.floor(the15smthn))
# Task 8: Find the ceiling value of 15.2.
the15pt2=15.2
print(math.floor(the15pt2))
# Task 9: Calculate the square root of 625.
the625=625
print(math.sqrt(the625))
#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
prices = [34.56, 45.78, 23.89, 12.34, 78.90]
quantities = [3, 5, 2, 4, 6]
# Calculate the total cost for each item (price multiplied by quantity).
print(sum(prices)+sum(quantities))
# Then, find the average cost of all items after rounding it to 2 decimal places.
cost=sum(prices)+sum(quantities)
print(round(cost, ndigits=2)/5)
#################### END OF ADVANCED PROBLEM SET ####################
