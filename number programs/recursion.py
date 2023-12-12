#recursion is nothing but a function calling itself with in the function/ a function call to the same fuction with same name
#example
def recursion_r():
    print("hello")
    recursion_r()  #it will give the multiple times hello printed
recursion_r()      #it will call the function call only once.

#it will call the function and that function will go to the print after the print it will go the recursion r function and that will go to the def recursion r
# and finally the recursion will be print hello multiple times and finally gives error.

