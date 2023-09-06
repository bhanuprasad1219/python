def compute_GCD(a,b):
    if b == 0:
        return a
    else:
        return compute_GCD(b,a%b)
n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
print(compute_GCD(n1,n2))


#test cases
#1:if normal factor of gcd
#2: if any number in gcd is 0 it will get remain number
#3:relatively prime numbers
#4:negative numbers
