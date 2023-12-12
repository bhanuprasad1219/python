num = float(input("enter a number"))
result = 0
while num > 0:
    digits = num % 10
    result = result + digits
    num = num // 10
print(result)


#1: we have to take one number
#2: then after the we have to find the digits in that number
#3: after  that that digits will add to the result here initially result value 0 we take
#4: then we have to truncate division the number becouse we remove the digits one by one

#test cases
#1:positive integer
#2:single digit number
#3:large number
#4:number 0
#5:floating point