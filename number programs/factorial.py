# recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  #it will nold the n value until it 0 and print the value

num = 6
result = factorial(num)
print(result)

# loop iterative

def factorial(n):
    result = 1
    for i in range(1, n + 1):  # the range will gives the value of n
        result *= i
    return result
num = 6
fact = factorial(num)
print(fact)

#while loop

def factorial(n):
    result = 1
    while n > 1:
        result *= n  # it will multi[plying and n value should be decresing
        n = n - 1
    return result
num = 4
fact = factorial(num)
print(fact)

#libruary functions

import math

n = 7
fact = factorial(n)
print(fact)

#test cases:
#1: the given number should be positive number
#2: the given number is 0 or 1 it should be return 1
#:the given number not having any negative value