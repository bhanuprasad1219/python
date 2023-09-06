#replace operation in list

list = [20,20.7,"bhanu"]  #here the list variables int, float,string
list[2] = 29              #we replace the value at 2 position with int 29
list[1] = "prasad"        #we replace the value at 1 position with string prasad
list[0] = 46.8            #we replace the value at 0 position with float 46.8
print(list)

#insert operation in list

#list.insert(2,"prasad")
list.insert(0,20.4)        #we insert the value at 0 position with float 20.4
list.insert(1,"bhanu")     #we insert the value at 1 position with string bhanu
list.insert(2,"prasad")    #we insert the value at 2 position with string prasad
print(list)                #here printing the values

#sort operation in list
# the sort operatiion used when similar type of data is present in the list otherwise we can't sorted the list it shows error
#like numbers are present in the list it will re arranged like mixed numbers int and float but we vcannot arranged strings with numbers.
#this sort will sorted as ascending order or alphabetic order

animals = ["monkey","fox","elephant","cat","zebra"]
num = [10,34,2,4.5,6,78,1.3]  #here we can ascending numbers or alphabetic here we give the numbers like int and float it will arranged as ascending.
animals.sort()   #this sort will arrange the variables like alphabetic and gives the output as sorted.
num.sort()
print(animals)
print(num)

#append operation in lists
#here append will do add the instances  at the last of the list.

animals.append('donkey')
print(animals)

#reverse operation in lists
#here the the reverese operation is to do the reverese the elements when last to first.

animals.reverse()
print(animals)

#delete operation
#here delete operation will do the delete the elements

#del animals[0]    #here the del operation will delete perticular value in the list.
del animals[:]     #here the del operation and slicing will delete all the elements in the list.
print(animals)


## here printing the duplicate value position
W = ["b","h","a","n","u","p","r","a","s","a","d"]
g = 0
for i in range(len(W)):
    if W[i] == "a":
        print(i)
    g = g+1

##
z = ["bhanuprasad"]
string = z[0]
for i in range(len(string)):
    if string[i] == "a":
        print(i,end=" ")
    i = i+1
print()





