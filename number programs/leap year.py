def leap(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return "it's a leap year"
    else:
        return "not a leap year"


print(leap(1994))
print(leap(1996))
print(leap(2000))


# test cases
# 1:leap yer will be divisible by 4 and 400 and 100
# 2:leap yera have the 366 days rotaion of every 4 years
# 3:leap year will not have a 365 days
