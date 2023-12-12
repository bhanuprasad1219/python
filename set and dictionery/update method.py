#update method in the dictionery
dict1 = {1:"ram",2:"raj",3:"raghu"}
dict2 = {4:"ravan"}
dict1.update(dict2)
print(dict1)

#output
#{1: 'ram', 2: 'raj', 3: 'raghu', 4: 'ravan'}
#here the dict1 and dict2 concatinate with the method of update.the dict2 values will be added to the end of the dict1.

dict1 = {1:"ram",2:"raj",3:"raghu"}
list1 = [5,"rakesh"]
dict1.update({list1[0]: list1[1]})
print(dict1)

#output
#{1: 'ram', 2: 'raj', 3: 'raghu', 5: 'rakesh'}
#here we get the output by cancatinating the dictionery with list by using update method

dict1 = {1: 'ram', 2: 'raj', 3: 'raghu', 5: 'rakesh'}
dict2 = {2:"arjun"}
dict1.update(dict2)
print(dict1)

#output
#{1: 'ram', 2: 'arjun', 3: 'raghu', 5: 'rakesh'}
#here we get the the updating the element in 2 position value as arjun by instead of raj.

dict1 = {1: 'ram', 2: 'arjun', 3: 'raghu', 5: 'rakesh'}
dict1.update({6:"x",7:"y",8:"z"})
print(dict1)
#output
#{1: 'ram', 2: 'arjun', 3: 'raghu', 5: 'rakesh', 6: 'x', 7: 'y', 8: 'z'}
#here we get the dictionery elements in the dictionery by using update method with in the function we can perform the operation.