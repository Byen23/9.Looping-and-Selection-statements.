# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 2019

@author: Byen23
"""


#9th Program to be uploaded to Github

# Specifying the steps in the range.

""" The count-controlled loops we have seen thus far count through consecutive numbers in a series. However, in some programs we might want a loop to skip some numbers, perhaps visiting every other one or every third one. """

list(range(1, 6, 1)) # Same as using two arguements

list(range(1, 6, 2)) # Use every other number 

list(range(1, 6, 3)) # Use every third number

# Now suppose you had to complete the sum of the even numbers between 1 and 10

theSum = 0 
for count in range(2, 11, 2):
	theSum += count
	
print(theSum)

# Looks that count own

for count in range(10, 0, -1):
	print(count, end = " ")
	
print("\n",list(range(10, 0, -1)))
print(69*"-")

# Short Circuit Evaluation

"""Likewise, in the expression A or B, if A is true, then so is the expression, and again there is no need to evaluate B. This approach, in which evaluation stops as soon as possible, is called short-circuit evaluation. """


count = int(input("Enter the count: "))
theSum = int(input("Enter the sum: "))
if count > 0 and theSum > 10:
	print("Average > 10")
else:
	print("count = 0 or average <= 10")
	