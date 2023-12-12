num = int(input("enter a number"))
k = 1                                       #here k value for incrementing odd values in column.
for i in range(1,num+1):                   #i iterating in loop in range of 1 to num
    for j in range(1,k+1):                 #j is for column itertaion with in range of the 1 to k+1 value
        print("*",end = " ")               #here *will printing and with space.
    k = k+2                                #k =1 and 1= 1+2 =3
    print()                                #print for new line.
#output
"""
enter a number5
* 
* * * 
* * * * * 
* * * * * * * 
* * * * * * * * * 
"""
