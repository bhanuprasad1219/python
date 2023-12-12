n = 5
for i in range(n,0,-1):           #here i(row)starts at 1 up to n  and -1 will do for decrementing n value.
    for j in range(1,i+1):        #here j(column)starts at 1 to row +1
        print(j,end="")           #here printing column value with same line
    print()                       #this print will new line.
#
##output
"""
12345
1234
123
12
1
"""

n = 6
for i in range(n,0,-1):          #here i(row)starts at 1 up to n  and -1 will do for decrementing n value.
    for j in range(1,i+1):       #here j(column)starts at 1 to row +1
        print(i,end="")          #here printing row value with same line
    print()                      #this print will new line.

##output
"""
666666
55555
4444
333
22
1
"""