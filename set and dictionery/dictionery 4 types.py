#using curly braces
my_dict = {1:"apple",2:"banana",3:"mango"}
print(my_dict)

#output
#{1: 'apple', 2: 'banana', 3: 'mango'}

#create empty dictionery
my_dict = {}
my_dict[1] = "sun"
my_dict[2] = "mon"
my_dict[3] = "tue"
print(my_dict)

#output
#{1: 'sun', 2: 'mon', 3: 'tue'}

#using dict connstructor
d = dict([(1,"apple"),(2,"banana"),(3,"mango")])
print(d)

#using two parellel list
a = [1,2,3,4]
b = ["äpple","banana","mango","berry"]
my_dict = {}
for i in range(len(a)):
    my_dict[a[i]] = b[i]
print(my_dict)

#output
#{1: 'äpple', 2: 'banana', 3: 'mango', 4: 'berry'}

