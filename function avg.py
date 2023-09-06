def avg(n1,n2,n3):
    return (n1+n2+n3)/3.0    #here the arguments are added and devide with 3.0
result1 = avg(10,20,30)      #here the result  will assign the  n1,n2,n3 and call to the function
result2 = avg(1,2,3)         #here the result  will assign the  n1,n2,n3 and call to the function
result3 = avg(2.3,4.5,3.2)   #here the result  will assign the  n1,n2,n3 and call to the function
print(result1)
print(result2)
print(result3)



#non return functions

def display():                 #this is the function name with formal parameters
    print("welcome")           #this some task
    print("have a nice day")
display()                     #its simply call to the function with actual parameters
#this is not return any values
#keyword & default

def avg(n1,n2,n3=6):
    return (n1+n2+n3)/3.0
num1 = int(input())
num2 = int(input())
#num3 = int(input())
result = avg(num1,num2)   #function call
print(result)

#local&global variable

n = 10                #here n is global variable which use foe whole program
def function1():      #defining the function
    print(n)          #printing n value of function1
def function2():      #defining the function2
    n = 20            # n is a local variable which use only with in the function
    print(n)          #printing the n value
    function1()       #call to the function1
function2()           #calling function2

#a variable is referenced within a function, Python first looks for that variable within the local scope of the function,
# and if it's not found, it then looks in the global scope.

#global variable

n = 10           #the global variable n
def func1():
    global n     #we should write as a keyword global for making value n as global here we dont mention global then its taken as local but we didnot assign value of n as local
    n = n+1      #we should do some operations
    print(n)     #printing the value of global
func1()          #calling the function


#anonymous function/ lambda function
#anonymous function is nothing but we don't use any function and defining a function we use lambda keyword to do some task.
sum = lambda var1,var2:var1+var2  #here we didn't mention any function name we use lamda keyword to perform the task
print(sum(10,20))                 #sum will pass the values to the variable 1&2 then it perform task and given the output


#variable length arguments
def func1(*mylist):         #here * is used for the taking number of parameters length
    for num in mylist:      #iterating the num value in mylist
        print(num)          #printing num values
    return                  #return will avoid none
func1(10,20,30)             #giving the function call with 3 parameters
func1(9,70)                 #giving the function call with 2 parameters
func1(2.3,4.7,5.9,6)        #giving the function call with 4 parameters

#test cases
#1:empty list
#2:with integer values
#3: with float values
#4:with negative values
#5:with single value and duplicate values
#6: non numeric values  (alphabetic)
#7:with none values like none,2,5,6