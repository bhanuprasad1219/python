n = 9
for i in range(1,n+1):
    for j in range(1,i+1):
        print(format(j,"<3"),end="")
    i = i+1
    print()

##
n = 8
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(format(j,"<3"),end="")
    i = i+1
    print()

##
