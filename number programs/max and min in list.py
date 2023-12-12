list1 = [1,24,546,65,3]
list2 = [1,34,63,765,7]
if max(list1) > max(list2):
    print(max(list1))
elif max(list1) == max(list2):
    print(max(list1))
else:
    print(max(list2))

if min(list1) > min(list2):
    print(min(list1))
elif min(list1) == min(list2):
    print(min(list1))
else:
    print(min(list2))

#test cases
#1:positive numbers
#2:negative numbers
#3:mixed numbers
#4:empty number
#5:floating numbers
#6:single element
#7:duplicates
