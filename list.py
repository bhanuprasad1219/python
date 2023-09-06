thislist = ["apple", "banana", "cherry"]
print(thislist[0])     #retuens the apple index 0 object
print(thislist[0:2])   #returns the  apple and banana index 0 included and 2 excluded
print(thislist[1:2])   #returns the banana
print(thislist[-1])    #returns the cherry
print(thislist[-1:])   #returns the cherry in the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])   #returns index 2 included 5 excluded
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])   #returns index 2 to end
print(thislist[ :6])  #returns the includidng 0 to excluding 6
print(thislist[ : ])  #returns the including 0 to end
if "apple" in thislist: #returns yes we should apllying if statement condition
  print("Yes, 'apple' is in the fruits list")
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

  thislist[1:3] = ["blackcurrant", "watermelon"]

  print(thislist) #returns the index 1 replace with blackurrant 2 replace with watermilon

  thislist = ["apple", "banana", "cherry"]

  thislist[1:3] = ["blackcurrant", "watermelon"]

  print(thislist) #returns the 1,and 2 replace with blackcurrant and watermilon

  thislist = ["apple", "banana", "cherry"]

  thislist[1:2] = ["watermelon"]

  print(thislist)   #returns the 1 replace with watermilon                                              ``  ````````````````

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)   #returns the removing bananq in the list

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)   #returns the insering orange in index of 1 place and output gives all

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)   #returns append will add the object at end

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)   #pop will remove the index 1 position object

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
for x in thislist:
    print(x)     #returns the all objects when for loop is applying

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1     #applying while loop it will returns the all objects one by one

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]   #iusing comprehension list we get the all objects one by one


