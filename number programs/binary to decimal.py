"""def find(dec_num):
    if(dec_num == 0):
        return
    else:
        #print(dec_num % 2, end="")
        find(int(dec_num/2))
        print(dec_num%2,end="")
        return  dec_num
print(find(67))
print(find(32))
print(find(9))"""


#without recursion
def binary_to_decimal(num):
    if num == 0:
        return 0
    result = ""
    while num > 0:
        r = num%2
        num = num // 2
        print(num,)
        result = str(r) + result


    return result
print(binary_to_decimal(89))
print(binary_to_decimal(6))

#here find is a recursive function and its call it self by solving the problem

#test cases
#1:basic test cases like 0,1,2,3,,10
#2:larger decimal number like 255 400
#3:decimal numbers with leading zeros like 0023, 045,003
#4:decimal numbers are not converts negetive and fractional numbers like -5,-6, 6.45,7.45
#5:decimal not converts non numeric and empty like "hi",_,
#6:a very large decimal numbers like 10^7,10^4

