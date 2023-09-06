n = 1
while n <= 10:
    if n == 5:
        print(n)
        break
    else:
        print(n)
        n = n+1
print("thank you")

#
m = 1
for m in (1,2,3,4,5,6,7):
    if m == 5:
        print(m)
        break
    else:
        print(m)
        m = m+1
print("thankyou")


#continue statement

var = 10
while var > 0:
    var = var - 1
    if var == 6:  #here the var value is 6 then it will pass to next variable
        continue  #this continue variable pass the variable to next statement
    print(var)
print("thankyou")

