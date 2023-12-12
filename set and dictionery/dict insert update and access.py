my_dict = {1:"apple",2:"banana",3:"mango"}
print(my_dict[1])    #here we get the output as apple

#print(my_dict["apple"])  #here we didnot get the output becouse the value doesnot allow to get the output it will contain get() method

print(my_dict.get(1))
#apple

print(my_dict.keys())
#dict_keys([1, 2, 3])

print(my_dict.values())
#dict_values(['apple', 'banana', 'mango'])

my_dict[1] = "carret"
print(my_dict)
#{1: 'carret', 2: 'banana', 3: 'mango'} here we can update the values as carret

my_dict[4] = "morris"
print(my_dict)
#{1: 'carret', 2: 'banana', 3: 'mango', 4: 'morris'}  here we can insert6 the one new key value pair in the dictionery

print(my_dict)
#{1: 'carret', 2: 'banana', 3: 'mango', 4: 'morris'} here we can access the all the keys and values in the list