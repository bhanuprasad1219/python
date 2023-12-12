#2 number lcm
def compute_LCM(n1,n2):
    if n1 > n2:
        higher = n1
    else:
        higher = n2
    value = higher
    while True:
        if higher % n1 == 0 and higher % n2 == 0:
            print(higher)
            break
        else:
            higher = higher + value
n1 = int(input("enter a number:"))
n2 = int(input("enter a number"))
compute_LCM(n1,n2)


#lcm of 3 numbers

def compute_LCM(n1,n2,n3):
    if n1>n2 and n2>n3:
        higher = n1
    elif n2>n1 and n3>n1:
        higher = n2
    else:
        higher = n3

    value = higher

    while True:
        if higher % n1 == 0 and higher % n2 == 0 and higher % n3 == 0:
            print(higher)
            break
        else:
            higher = higher + value
n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
n3 = int(input("enter a number:"))
compute_LCM(n1,n2,n3)



#first we should check the numbers if its which number is greater
#after the greater value assigned to the variable
#and then after the greater value should divisible by values we have to check
#if its get 0 then it should be print else add the value of a greter variable to greater value
#then after enter numbers and call the fuction

#test cases
#1: if it prime numbers it will directly multiply with another
#2: if a number get 0 then lcm will get 0
#3:normal factors like 2, 4, 6 lcm is 12