list1 = [24,1,13,54,23,6,0]                            #list will having elements
print(list1)                                           #we printing original list elements
for i in range(len(list1)):                            #taking the for loop and i will iterating in list
    min_val = min(list1[i:])                           #assigning the min index of the list value to the min_val
    min_ind = list1.index(min_val)  #assigning the index of the min value to the min_ind
    min_ind = list1.index(min_val,i)                   #it will get the duplicate values to be sorted as ascending order
    list1[i],list1[min_ind] = list1[min_ind],list1[i]  #swaping the min values in the list became a ascending order.
    print(list1)                                       #printing the how its swapping
print(list1)                                           #printing ofter the swaping ascending order list.


#descending order selection sort
list = [6,5,3,6,0]
#list = [7,7,7,7,7,7]
#list = [1,2,3,4,5,6,7]
#list = [9,8,7,6,5,4,3,2]
#list = [2,33,46,645,664,44,9,0]
print(list)
for i in range(len(list)):
    max_val = max(list[i:])
    max_ind = list.index(max_val,i)
    #if list[i] == list[max_ind]:                        #this if value will do the element which is in crt position then no need to swap then that time this will work
       #  list[i],list[max_ind] = list[max_ind],list[i]
    list[i], list[max_ind] = list[max_ind], list[i]
    print(list)
print(list)


#test cases:
#1:
