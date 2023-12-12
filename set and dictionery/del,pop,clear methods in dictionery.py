dict1 = {1: 'ram', 2: 'arjun', 3: 'raghu', 5: 'rakesh', 6: 'x', 7: 'y', 8: 'z'}
del dict1[3]  #hhere we can use [] by instead of () because the the elemnts should be accessed by key.
print(dict1)
#output
#{1: 'ram', 2: 'arjun', 5: 'rakesh', 6: 'x', 7: 'y', 8: 'z'}
#here the del method will del the one key value pair in the dictionery
#note: here we can perform del operation while using the []braces.

dict1 = {1: 'ram', 2: 'arjun', 5: 'rakesh', 6: 'x', 7: 'y', 8: 'z'}
dict1.pop(6)  #here pop function will get the value by removing of the key but here both will deleted by pop method.
print(dict1)
#output
#{1: 'ram', 2: 'arjun', 5: 'rakesh', 7: 'y', 8: 'z'}
#here the key and value should be deleted by using of the pop method

dict1 = {1: 'ram', 2: 'arjun', 5: 'rakesh', 7: 'y', 8: 'z'}
dict1.clear()  #here we donot mention the any dict1 names in the clear function
print(dict1)
#output
#{}
#here we can directly clear all the data from the dictionery.


