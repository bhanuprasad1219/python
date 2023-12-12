"""
write a program to print 1, to 10 numbers in same line
write a python program to check a number positive or negative
you are given two numbers. write a python program to print greatest number
write a program to check given number is even or not
write a program to check given number is armstrong number or not
"""

def same_line(num):
    for i in range(1,num + 1):
        print(i, end=" ")
print(same_line(10))

##
def pos_neg(n1):
    if n1 == 0:
        print("zero")
    elif n1 > 0:
        print("positive")
    else:
        print("negative")
pos_neg(0)
pos_neg(7)
pos_neg(-6)


##
def greatest(n1,n2):
    if n1 > n2:
        print("n1 greater than n2")
    else:
        print("n2 greater than n1")


greatest(18,34)
greatest(32,23)
greatest(23,23)

##
def even_odd(n1):
    if n1%2 == 0:
        print("even number")
    else:
        print("odd number")

even_odd(5)
even_odd(8)
even_odd(0)

##
def arms_num(n):
    org = n
    result = 0
    b = len(str(n))
    while n > 0:
        r = n%10
        result = result + r ** b
        n = n//10
        # return result
    if result ==  org:
        print("armstrong number")
    else:
        print("not an arstrong number")
arms_num(153)
arms_num(123)