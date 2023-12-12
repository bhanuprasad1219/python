set1 = {1,2,3,4}
print(set1)
print(type(set1))
#output
#{1, 2, 3, 4}
#<class 'set'>
#herte we can get the data type of the set.

set1 = {}
print(type(set1))
#output
#<class 'dict'>
#here the empty {} describes the empty dictionery we can add the elements to it.

set1 = {"apple","banana","mango"}
set1.add("berry")
print(set1)
#output
#{'mango', 'banana', 'apple', 'berry'}
#here we can get the berry by using of add function
#this set function immutable and unorderd,cannot  contain duplicate values.

set1 = {'mango', 'banana', 'apple', 'berry','mango','banana'}
print(set1)
#output
#{'apple', 'berry', 'banana', 'mango'}
#here we get the non duplicated values as output.


