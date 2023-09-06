#sequences of tuple
#here string ,list and tuple these are the sequences in the python
#length of the string and tuple and list
name = "bhanuprasad"
me = len(name)
print(me)
list1 = ["amul",1,1.3,34]
list2 = len(list1)
print(list2)
n = (10,23.4,34,1.3)
m = len(n)
print(m)
animal = ("bird","cat","dog","zebra")
anim = len(animal)
print(anim)

#select in sequence

print(n[0])
print(animal[3])
print(list1[2])
print(name[7])

#slice sequence

print(name[:11])
print(animal[0:])
print(n[1:3])
print(list1[:])

#count in sequence

print(name.count('a'))
print(list1.count(1))
print(n.count(3))
print(animal.count('dog'))

#index


print(name.index('a'))  #question.how to print duplicate values as using index operation
print(list1.index(1))
print(n.index(23.4))
print(animal.index('dog'))

#membership operation

if 'a' in name:
    print("True")
#other
if 'a' not in name:
    print("False")

#concatenation operation
name2 = " myadari"
#neme2 = [12,34]      #here the string not concatenate with the list
#neme2 = (12,340)      #here the string not concatenate with the tuple
s = name+name2
print(s)


list3 = [12.3,32,34.2,33.8]
#list3 = " introvert"          #here the list not concatenate with the string
#list3 = (12,23.4,43)          #here the list not concatenate with the tuple
l4 = list1+list3
print(l4)


n2 = (12,23.4,43,"amul")
#n2 = [12,23.4,43,"amul"]     #here the tuple not concatenate with the slist
#n2 = " introvert"            #here the tuple not concatenate with the string
n3=n+n2
print((n3))

#min value in tuple
print(min(n))
#print(min(list1))  # it is not supported int and string in list and tuple.
k=[1,2,3,4,5,0.6,7,0.1]
print(min(k))
print(min(name))

#max value
print(max(n))
#print(max(list1))  # it is not supported int and string in list and tuple.
k=[1,2,3,4,5,0.6,7,0.1]
print(max(k))
print(max(name))

#sum in sequence

#print(sum(name))    #in this we have sum is not operated because it not caluculated int and string in one .
print(sum(list3))
print(sum(n))
print(sum(k))

#copy in sequence

tuple = (1,2,3,4,5)
tuple1 = tuple
print(tuple)
#tuple1[0] = "bhanu"  #here tuple can't allow strings in it.
print(tuple[0])

list1 = [1,2,3,4,5,6]
print(list1)
list9 = list1
list9[0] = "amul"
print(list9)
list9[0]=0
print(list9)




#
var = [12,2.3]
print(dir(var))



