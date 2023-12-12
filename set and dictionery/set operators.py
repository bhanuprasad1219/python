#membership oerator in the set
set1 = {1,2,3,4,"hello"}
print(6 in set1)  #here in is the membership operator in the set
print(set1)
#output
#False
#{1, 2, 3, 4, 'hello'}

#add operator in the set
set1 = {1, 2, 3, 4, 'hello'}
set1.add("maruthi")
print(set1)

#output
#{'hello', 1, 2, 3, 4, 'maruthi'} here we can add the lements in the set by using the add operator

#remove operator in set
set1 = {'hello', 1, 2, 3, 4, 'maruthi'}
set1.remove(2)
print(set1)
#output
#{'maruthi', 1, 3, 4, 'hello'}
#here we can remove the element by using the remove operator

#union operator in set
set1 = {'maruthi', 1, 3, 4, 'hello'}
set2 = {"shyam",7}
set1 = set1|set2
print(set1)
#output
#{'maruthi', 1, 3, 4, 7, 'hello', 'shyam'}
#here we can union the two sets by using union operator
#note: union symbol is |

#clear operator in the set
set1 = {'maruthi', 1, 3, 4, 7, 'hello', 'shyam'}
set1.clear()
print(set1)
#output
#set()
#here the clear function will clear all the elements in the set1.

#intersection operator in the set
set1 = {'maruthi', 1, 3, 4, 7, 'shyam', 'hello'}
set2 = {'maruthi', 1, 3, 4, 'hello'}
set1 = set1 & set2
print(set1)
#output
#{1, 3, 4, 'maruthi', 'hello'}
#here we can get the output as the intersect by using of the intersection method here we can get the commonn values.

#difference operator in the set
set1 = {1, 3, 4, 'maruthi', 'hello'}
set2 = {1, 3, 4, 'hello', 'shyam', 7, 'maruthi'}
#set1 = set1 - set2
set2 = set2 - set1
#print(set1)
print(set2)
#output
#set()
#{'shyam', 7}
#here the set1 containg eements as equal in set2 then it will does not have the difference in both.
#here the set2 containing two elements as differed  by the set1.

#symmetric difference
set1 = {1, 3, 4, 'hello', 'maruthi'}
set2 = {1, 3, 4, 'hello', 7, 'shyam', 'maruthi'}
set1 = set2 ^ set1
print(set1)

#output
#{7, 'shyam'}
#here we can get the output as the difference between the set2 Nand set1 and the final responce will not having elemnts in setg 1.

#size
set1 = {1, 3, 4, 'maruthi', 'hello'}
print(len(set1))
print(len(set2))
#output
#5
#7
#here we can get the elementxs as the 5 and 7 by using of the len instead of size.


#copy

set1 = {1, 2, 3, 4, 'hello', 'maruthi'}
set2 = {1, 7, 3, 5, 'hello', 'maruthi'}

set2 = set1.copy()
print(set2)

#output
#{1, 2, 3, 4, 'hello', 'maruthi'}
#here we gwt the results as the the whole elements as copy to the next set then that set containing values must be cleared.










