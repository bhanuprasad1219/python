#data structures:-
#data structure is nothing but to store the data and oragnising the data so ghat it can be accessed effectively.
#data structures are 2 types one is built in data structures and another one is user defined data structures.
#lifo in stack
#in this stack lifo we can have the append used for add the element instead of push.
#the pop will remove the element in lifo

stack = []
stack.append(12)
stack.append(13)
stack.append(16)
stack.append(11)
print(stack)

#by using the append function in stack we can add the elements in the stack of list.

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

#here we can remove the elements in the stack of list by using of the pop function then this type of action is called lasy in first out.
#it means the append will add the elements and pop will remove the last added element by default.


stack = []                            #here we ca create the empty list because of push and pop operation will applied.
def push():                           #defining the push operation.
    if len(stack) == n:               #this line will describe the length of the stack will equal to the given limit checking.
        print("stack is full")        #if its equal then print function will exxicute.
    else:
        element = int(input("enter a element:"))   #here we can assingn a  new element.
        stack.append(element)                      #append function will add the element in to the stack.
        print(stack)                               #if its added element then it will print the stack.
def pop_element():                                 #defining the pop operation.
    if not stack:                                  #in this we can get the no element present in the stack .
        print("stack is empty")                    #then printing the stack is empty.
    else:
        e = stack.pop()                            #here we caj assign a new variable e to the pop of the stack.
        print("stack is removed one element",e)    #here the removing element will print the element of stack.
        print(stack)                               #here we print the stack.
n = int(input("limit of stack"))                   #here we can assign the limit for the stack.
while True:                                        #while true will describe the loop operation.
    print("choose any option 1.push ,2.pop ,3.quit")  #here we can select the option for doing operation.
    choice = int(input())                           #here the option will having the number.
    if choice == 1:                                 #here the choice is equal to the 1 then its get pushed a element.
        push()
    elif choice == 2:                               #here the choice is 2 the elelment will get poped.
        pop_element()
    elif choice == 3:                               #here the choice is 3 then its get quit.
        break                                       #the break statement will break the loop.
    else:
        print("select currect option")              #here print the currect option.


#output
""""limit of stack 3
choose any option 1.push ,2.pop ,3.quit
1
enter a element:10
[10]
choose any option 1.push ,2.pop ,3.quit
1
enter a element:20
[10, 20]
choose any option 1.push ,2.pop ,3.quit
1
enter a element:30
[10, 20, 30]
choose any option 1.push ,2.pop ,3.quit
1
stack is full
choose any option 1.push ,2.pop ,3.quit
2
stack is removed one element 30
[10, 20]
choose any option 1.push ,2.pop ,3.quit
20
select currect option
choose any option 1.push ,2.pop ,3.quit
2
stack is removed one element 20
[10]
choose any option 1.push ,2.pop ,3.quit
2
stack is removed one element 10
[]
choose any option 1.push ,2.pop ,3.quit
2
stack is empty
choose any option 1.push ,2.pop ,3.quit
3
"""








