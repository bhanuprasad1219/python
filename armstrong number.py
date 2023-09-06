"""
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)

    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits
    return total == num

num = int(input("enter a number"))
if is_armstrong_number(num):
    print(f"yes")
else:
    print(f"no")

"""

#or
for i in range(1001):
    num = i
    n = len(str(i))
    result = 0
    while(i!=0):
        digit = i%10
        result = result + digit ** n
        i = i//10
    if num == result:
        print(num)