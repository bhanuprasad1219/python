list = [23,4,21,8,3,0]
print(list)
for j in range(len(list)-1):
    for i in range(len(list)-1-j):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
            print(list)
    print()
print(list)