#sorting is having two in it built in function and without built in function.
#here built in function will have sort and without built in function will have sorted.
list1 = [1,2,3.4,5.6,0.7,0.4]
list1.sort()
print(list1)

#
num = ["bhanuprasad","aprasad"]
num.sort()
print(num)

#
name = ["dd","eeee","b","ccc","aaaaaa"]
name.sort(key=len)
print(name)

#
l = [383,363,873,23,2,33.333,4.233,4.44]
#l.sort(reverse=True)
#print(l)

#
m = [[1.023,1.233],[1.003,1.230]]      #[1.013,1.023],[1.230,1.003]
if m[0][1] > m[1][1]:
    m[0],m[1] = m[1],m[0]
else:
    print(m)
print(m)
