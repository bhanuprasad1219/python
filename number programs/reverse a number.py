
""""num = input("enter a number:")
num_string_reversed = num[::-1]
print(num_string_reversed)"""


n = 153
result = 0
while n>0:
    r = n%10
    result = result * 10 + r
    n = n//10
print(result)