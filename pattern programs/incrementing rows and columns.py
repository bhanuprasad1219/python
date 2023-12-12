num = int(input("enter a number"))
for i in range(1,num+1):                         #i is iterating in range from  to num
    for j in range(1,i+1):                     #j is iterating in range from 1 to i+1 because its add another one in it.
        print("*",end = " ")                   #print will print * and takind space for the end.
    print()                                    #this print wil do next line for printing values.

#output
""" 
enter a number6
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *
"""


