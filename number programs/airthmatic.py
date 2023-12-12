print("Hello World")

x= 10
y= 20
#airthmatic operators

print(x+y)  #10+20=30
print(x-y)  #10-20=-10
print(x*y)  #10*20=200
print(y%x)  #20%10=0 it will take rem9nder value
print(x/y)  #10/20=0.5
print(x//y) #10//20=0  it will take only int value
print(x**y) #10**20=1000000000000000000000 it will print pover of 10

#comparision operators

print(x>y)  #false
print(x<y)  #true
print(x>=y) #false
print(x<=y) #true
print(x==y) #false
print(x!=y) #true0.

#logical operatiors

print(x<y and y>x)       #returns true when both statements are true
print(x<y or y>x)        #returns true when one statement will true
print(not(x<y and y>x))  #returns false when both are true but not represents false

#membership operators

a = ['bhanu']
b = ['prasad']
print('bhanu' in a)      #returns the true because bhanu is there in a
print('bhanu'  not in b) #returns true because bhanu not in a
print('bhanu'  not in a) #returns false because bhanu in a
print('bhanu' in b)      #returns false because bhanu not in b

#assignment operators

m = 6
n = 4
m += n
print(m)
m -= n
print(m)
m *= n
print(m)
m %= n
print(m)
m /= n
print(m)
m = 6 <= 3
print(m)
m = 6 >= 3
print(m)
m = 2
m **= 3
print(m)
m &= 4
print(m)

#identity operator

x = ["bhanu","prasad"]
y = ["bhanu","prasad"]
z = x
print(x is z)     #returns the true because x having same objects in z
print(x is not y) #returns true because x and y not having same objects
print(y != x)     #returns the false because != is comparision returns the false because x is equal to y

#bitwise operator

x = 10
y = 20

print(10 & 3)
print(10 | 3)
